from flask import Flask

app = Flask(__name__)

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

@app.route("/reverse/<word>")
def reverse_word(word):
    return word[::-1]

@app.route("/user/<name>/<int:age>")
def user(name, age):
    return f"Hello, {name}. You are {age} years old."



if __name__ == "__main__":
    app.run(debug=True)