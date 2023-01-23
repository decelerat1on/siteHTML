from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('any.html')


app.run(debug=True)