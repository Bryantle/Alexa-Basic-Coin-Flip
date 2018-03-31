from flask import Flask, render_template
from flask_ask import Ask, question, session, statement, convert_errors
from random import randint

app = Flask(__name__)
ask = Ask(app, "/")

def coinflipper():
    return randint(0,2)

def messager(side, flip):
    if side == flip:
        return render_template("win")
    else:
        return render_template("lost")

@ask.launched
def launched():
    message = render_template("bet")
    return question(message)

@ask.intent("HeadsIntent")
def heads():
    flip = coinflipper()
    message = messager(0, flip)
    return statement(message)

@ask.intent("TailsIntent")
def tails():
    flip = coinflipper()
    message = messenger(1, flip)
    return statement(message)
