from flask import Flask, request, render_template, redirect, url_for, make_response, jsonify

import os
import mainV1


app = Flask(__name__)


# 装饰器
@app.route("/get_classes", methods=['GET'])
def get():
    classes = mainV1.get_classes()
    options = ""
    for i in classes:
        option = f'<option value="{i}">{classes[i]}</option>'
        options += option
    print(options)
    return render_template('get_classes.html',
                             classes = classes,
                             options = options)


user_cookie = '123'

#设置允许的文件格式
ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])

def upload():
    if request.method == 'POST':
        f = request.files['file']

        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "请检查上传的文件类型，仅限于xls,xlsx"})
        
        os_path = os.getcwd()
        upload_path = os_path + '/upload/' + user_cookie + '.xlsx'
        f.save(upload_path)
        return redirect(url_for('show'))

    return render_template('upload.html')


@app.route("/show", methods=['GET'])
def show():
    return mainV1.show()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=444, ssl_context=('key/secret.pem', 'key/secret.key'))

# flask添加https支持，只需要在app.run中添加ssl_context参数。
