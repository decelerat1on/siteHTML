from flask import Flask, render_template, request
from SQLtest import connection, add_user, check_user

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('input.html')
# @app.route('/Add', methods=['POST'])
# def add_page():
#     data = request.form.to_dict()
#     print(data)
#     return 'Выполнено'

@app.route('/register')
def register():
    return render_template('registerhtml.html')

@app.route('/userprofile', methods=['POST'])
def userprofile():
    data = request.form.to_dict()
    add_user(data)
    return 'Пользователь добавлен в базу данных'
@app.route('/Login', methods=['POST'])
def log_in():
    data = request.form.to_dict()
    print(data)
    return check_user(data)


app.run(debug=True)


