"""A madlib game that compliments its users."""

from random import sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html", person=player, compliments=compliments)

@app.route("/game")
def show_madlib_form():
    """Play madlib game."""
    game_choice = request.args.get("game_choice")

    if game_choice == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route("/madlib")
def show_madlib():
    person = request.args.get("person")
    color = request.args.get("color")
    noun_choice = request.args.get("noun_choice")
    adj_choice = request.args.get("adj_choice")

    print(type(adj_choice))
    print(adj_choice)
    return render_template("madlib.html", person=person, color = color, noun = noun_choice, adj = adj_choice )



if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
