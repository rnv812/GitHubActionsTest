from flask import Flask, render_template

from utils import roll_the_dice


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('roll-the-dice.html', number=roll_the_dice())


app.run(host='localhost', port=8080, debug=True)
