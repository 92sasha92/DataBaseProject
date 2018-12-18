from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('first_page.html')


@app.route('/home_page')
def home_page():
    return render_template('pages/main_page.html')


if __name__ == "__main__":
    app.run()
