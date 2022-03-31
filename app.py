from flask import Flask, request, render_template, redirect, url_for, session


import os
import mainV1
import time

app = Flask(__name__)

app.secret_key = b'Z\x8e\xbdp\xd7\xe0\x8a\xec5\xc1\x8a\xa1\x19m\x11\x9a'

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# 装饰器
@app.route("/", methods = ['GET'])
def index():
    return redirect(url_for('get_classes'))

@app.route("/get_classes", methods=['GET'])
def get_classes():
    session['user'] = str(int(time.time()))

    classes = mainV1.get_classes()
    options = ""
    for i in classes:
        option = f'<option value="{i}">{classes[i]}</option>'
        options += option
    return render_template('get_classes.html',
                             classes = classes,
                             options = options)


#设置允许的文件格式
ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    session['chosed_class'] = request.args.get('class', '')

    if request.method == 'POST':
        f = request.files['file']

        if not (f and allowed_file(f.filename)):
            # errorinfo = {"error": 1001, "msg": "请检查上传的文件类型，仅限于xls,xlsx"}
            return "请检查上传的文件类型，仅限于xls,xlsx"
        
        os_path = os.getcwd()
        upload_path = os_path + '/upload/' + session['user'] + '.xlsx'
        f.save(upload_path)
        # return redirect(url_for('upload'))
        return render_template('upload_success.html', show = show())
    return render_template('upload.html')





@app.route("/show", methods=['GET'])
def show():
    chosed_class = session['chosed_class']
    username = session['user']
    return mainV1.show(chosed_class, username)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=450, ssl_context=('key/secret.pem', 'key/secret.key'))
    
# flask添加https支持，只需要在app.run中添加ssl_context参数。
