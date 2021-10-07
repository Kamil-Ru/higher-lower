from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(1, 9)
print(random_number)


def make_h1(function):
    def wrapped():
        return f"<h1> {function()} </h1>"

    return wrapped


def too_low():
    return f'<h1 style="color:Red;">To low, try again</h1>\n' \
           f'<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>'


def too_high():
    return f'<h1 style="color:Purple;">To high, try again</h1>\n' \
           f'<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>'


def equal():
    return '<h1 style="color:Green;">You find me!</h1>\n' \
           f'<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>'


@app.route('/')
def main():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<input type="number">' \
           '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'


@app.route('/<int:number>')
def check_number(number):
    if number == random_number:
        return equal()
    elif number < random_number:
        return too_low()
    elif number > random_number:
        return too_high()


if __name__ == "__main__":
    app.run(debug=True)
