"""A madlib game that compliments its users."""

from random import choice, sample, randint

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

    return "Hi! This is the home page. <br><a href='/hello'>Go to Hello page</a>"


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    random_num = randint(1, len(AWESOMENESS))
    compliment = sample(AWESOMENESS, random_num)

    return render_template("compliment.html", person=player, compliments=compliment)

@app.route('/game')
def show_madlib_form():

    play_game = request.args.get("wants_to_play")

    if play_game:
        return render_template('game.html')
    else:
        return render_template('goodbye.html')
    # if play_game == 'yes':
    #     return render_template('game.html')
    # if play_game == 'no':
    #     return render_template('goodbye.html')
    


# try to add methods
# @app.route('/database', methods=['GET', 'POST'])

@app.route('/madlib', methods=['post'])
def show_madlib():
    #  get person, color, noun, and adjective 
    person = request.form.get("person")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")

    return render_template(
        'madlib.html', 
        person=person, 
        color=color, 
        noun=noun, 
        adjective=adjective,
    )

@app.route('/madlib2')
def show_madlib2():
    name1 = request.args.get("name1")
    name2 = request.args.get("name2")
    movie = request.args.get("movie")
    adjective1 = request.args.get("adjective1")
    verb1 = request.args.get("verb1")
    noun = request.args.get("noun")
    candy = request.args.get("candy")
    food = request.args.get("food")
    verb2 = request.args.get("verb2")
    verb3 = request.args.get("verb3")
    verb4 = request.args.get("verb4")
    adjective2 = request.args.get("adjective2")
    adjective3 = request.args.get("adjective3")
    adjective4 = request.args.get("adjective4")
    adjective5 = request.args.get("adjective5")

    return render_template(
        'madlib2.html', 
        name1=name1,
        name2=name2,
        movie=movie,
        adjective1=adjective1,
        verb1=verb1,
        noun=noun,
        candy=candy,
        food=food,
        verb2=verb2,
        verb3=verb3,
        verb4=verb4,
        adjective2=adjective2,
        adjective3=adjective3,
        adjective4=adjective4,
        adjective5=adjective5,
    )


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
