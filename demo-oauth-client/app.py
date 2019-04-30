import os

from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
from requests_oauthlib import OAuth2Session

app = Flask(__name__)
app.config.update(SECRET_KEY=os.urandom(16))

# Register client using authorization code grant type.
client_id = "client-id"
client_secret = "client-secret"
# For demo purposes, register with a local OAuth provider
authorization_base_url = "http://localhost:8000/o/authorize"
token_url = "http://localhost:8000/o/token/"

@app.route("/")
def demo():
    provider = OAuth2Session(client_id)
    authorization_url, state = provider.authorization_url(authorization_base_url)
    session["oauth_state"] = state
    return redirect(authorization_url)


# redirect-uri = http://127.0.0.1:5000/callback
@app.route("/callback")
def callback():
    """
    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """
    provider = OAuth2Session(client_id, token=session["oauth_state"])
    token = provider.fetch_token(
        token_url=token_url,
        client_secret=client_secret,
        authorization_response=request.url,
    )

    # At this point you can fetch protected resources but lets save
    # the token and show how this is done from a persisted token
    # in /profile.
    session["oauth_token"] = token

    return redirect(url_for(".apiendpoint"))


@app.route("/apiendpot")
def apiendpoint():
    """Use access token to get blogger's profile using pk=1"""
    provider = OAuth2Session(client_secret, token=session["oauth_token"], scope="read")
    return jsonify(provider.get("http://127.0.0.1:8000/diy/api/profile/1").json())


if __name__ == "__main__":
    # This allows us to use a plain HTTP callback.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    # Export variables if running Flask from command line
    # export FLASK_APP=app.py
    # export OAUTHLIB_INSECURE_TRANSPORT=1
    app.run(debug=True)

# Start demo to get authorization code
# 127.0.0.1 - - [30/Apr/2019 10:56:49] "GET / HTTP/1.1" 302 -
# 127.0.0.1 - - [30/Apr/2019 10:57:07] "GET /callback?code=<AUTHORIZATION_CODE>&state=<OAUTH_STATE> HTTP/1.1" 302 -
# 127.0.0.1 - - [30/Apr/2019 10:57:07] "GET /apiendpot HTTP/1.1" 200 -
