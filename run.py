import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


if os.path.exists('env.py'):
    import env
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/directions')
def directions():
    return render_template('directions.html')
    

@app.route('/allergies')
def allergies():
    return render_template('allergies.html')

if __name__ == '__main__':
    app.run(
        host = os.environ.get('IP', '0.0.0.0'),
        port = int(os.environ.get('PORT', '5000')),
        debug = True
    )


