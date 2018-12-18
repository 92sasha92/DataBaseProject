from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('first_page.html')


@app.route('/home_page')
def home_page():
    return render_template('pages/main_page.html')


@app.route('/ethnic_cuisines_start')
def ethnic_cuisines_page():
    return render_template('pages/ethnic_cuisines_start.html')


@app.route('/ethnic_cuisines')
def ethnic_cuisines():
    return render_template('pages/ethnic_cuisines.html')


if __name__ == "__main__":
    app.run()
