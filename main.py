from flask import Flask

import mainV1


app = Flask(__name__)


# 装饰器
@app.route("/show")
def show():

    return mainV1.show()


@app.route("/Getclasses")
def get():
    return mainV1.Getclasses()


app.run(host='0.0.0.0', port=444, ssl_context=('key/secret.pem', 'key/secret.key'))

# flask添加https支持，只需要在app.run中添加ssl_context参数。
