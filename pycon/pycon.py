from flask import Flask

import os, re

# app's default instance path works when running from command-line

# app = Flask(__name__)

# absolute path has to be provided when running application from PyCharm

app = Flask(__name__, instance_path='/Users/matthewlee/zulu/pycon/instance')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':

    print(app.instance_path)

    filename = os.path.join(app.instance_path, 'mt101.txt')

    print(filename)

    with app.open_instance_resource('mt101', mode='rt') as f:

        sample = f.read()

    p1 = re.compile('{\d:')

    for sbj in re.split(p1, sample):
        sbj = sbj.strip()

        print(sbj[0:len(sbj) - 1])

        print('++++++++++++++++++++++++')

    with app.open_instance_resource('braces', mode='rt') as f:

        sample = f.read()

    p2 = re.compile('(?s){(.*?)}')

    for sbj in re.split(p2, sample):
        sbj = sbj.strip()

        print(sbj)

    # app.run()