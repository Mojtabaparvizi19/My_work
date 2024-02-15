from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"

    return wrapper_function


def make_u(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route("/")
def say_hello():
    return ("<h1 style='text-align: center'> Hello Bitches</h1>"
            "<p style=' text-align: center'>This is a paragraph</p>"
            "<h2 style='text-align: center'> I am learning HTML and CSS </h2>"
            "<div style='margin: 0 auto; text-align: center'>"
            "<a href='https://google.com', >  Click Here</a>"
            " </div>"
            "<img src='https://i0.wp.com/picjumbo.com/wp-content/uploads/pink-clouds-wallpaper-free-photo.jpg?w=2210"
            "&quality=70'>"
            "<style>"
            "img {"
            "width: 20%;"
            "margin-left:auto;"
            "margin-right:auto;     "
            "display: block"
            "}"
            "</style>"

            )


@app.route("/bye")
@make_bold
@make_u
def say_bye():
    return "bye!"


@app.route("/username/<path:name>/<int:number>")
def greet(name, number):
    return f"hello {name}, you are {number} y/o"


app.run(debug=True ,use_reloader=False)
