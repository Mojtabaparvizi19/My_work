from flask import Flask
from random import *

number = randint(1, 9)
print(number)

game = Flask(__name__)




@game.route("/")
def guess_number():
    return ("<h1>Guess a number between 1-9</h1>"
            "<style>"
            "h1{background-color:antiquewhite;"
            "text-align:center;}"
            "img {display:block; margin-left:auto; margin-right:auto}"
            "</style>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")



@game.route("/<int:guess_number>")
def user_choice(guess_number):
    if guess_number == number:
        return ("<h1> correct </h1>"
                "<style>"
                "h1{background-color:antiquewhite;text-align:center;}"
                "</style>")


if __name__ == "__main__":
    game.run(debug=True, use_reloader=False)
