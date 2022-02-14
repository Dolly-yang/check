# classes = {0: '1班.xlsx', 1: '2班.xlsx', 2: '名单.xlsx'}
# import mainV1

# classes = {mainV1.get_classes()}
# print(type({mainV1.get_classes()}))
# print(type(classes))
# for i in classes:
#     print(i)
#     print(classes[i])
#     options = '<option value="' + i + f'>{classes[i]}</option>'
#             <option value="volvo">Volvo</option>
#     print(options)



# import json
# from flask import Flask, render_template
 
# app = Flask(__name__)
 
# @app.route("/")
# @app.route("/index.html")
# def index():
#         options = "<option value='volvo1'>Volvo1</option><option value='volvo2'>Volvo2</option>"
    
#         flask_data = 'Hello Flask!'
#         return render_template('test.html', options=options, flask_data=flask_data)
 
# if __name__ == '__main__':
#     app.run('0.0.0.0', 5000)




def foo():
     d = dict()
     d['str'] = "Nhooo"
     d['x']   = 50
     return d
# print(type(test.foo()))