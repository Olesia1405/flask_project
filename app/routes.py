from app import app
from flask import abort, request, render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/hello')
def hello():
    return "Hello, Flask!"

@app.route('/info')
def info():
    return "This is an informational page."

@app.route("/calc/<int:number1>/<int:number2>")
def calc(number1, number2):
    res = number1 + number2
    return f"The sum of {number1} and {number2} is {res}."

@app.before_request
def check_word_not_empty():
    if request.path.startswith("/reverse/"):
        word = request.path.split("/reverse/")[1]
        if not word.strip():
            abort(400, description="Error: The word must contain at least one character!")

@app.route("/reverse/<word>")
def reverse_word(word):
    return word[::-1]

@app.route("/user/<name>/<int:age>")
def user(name, age):
    if age <= 0:
        abort(400, description="Age cannot be negative or zero!")
    return f"Hello, {name}. You are {age} years old."