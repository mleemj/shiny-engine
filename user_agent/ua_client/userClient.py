import requests


class UserClient(object):
    def login(self):
        url = 'http://localhost:8080/csrf/greeting'
        s = requests.session()
        csrf = s.get(url).cookies['smartcookie']
        s.headers.update({'smartheader': csrf})
        s.auth = ('user', 'password')
        payload = {'name': 'Click and Clack'}
        response = s.get(url, params=payload)
        print(response.content)


if __name__ == '__main__':
    uc = UserClient()
    uc.login()
