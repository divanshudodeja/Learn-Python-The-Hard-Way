from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/hello', methods = ['POST', 'GET'])
def index():
    greeting = "Hello World"
    
    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting = greeting)
    else:
        return render_template("hello_form.html")

@app.route('/divanshu')
def hello_divanshu():
    greeting = "Divanshu"
    return f'Hello, {greeting}'

if __name__ == "__main__":
    app.run()