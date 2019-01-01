from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

conn = MySQLdb.connect(host="mysqlsrv1.cs.tau.ac.il",
                       user="DbMysql06",
                       passwd="DbMysql06",
                       db="DbMysql06",
                       use_unicode=True, charset="utf8")

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


@app.route('/picnic_start')
def picnic_page():
    return render_template('pages/picnic_start.html')


@app.route('/picnic')
def picnic_cuisines():
    return render_template('pages/picnic.html')


@app.route('/holiday_start')
def holiday_page():
    return render_template('pages/holiday_start.html')


@app.route('/holiday')
def holiday():
    return render_template('pages/holiday.html')


@app.route('/romantic_start')
def romantic_page():
    return render_template('pages/romantic_start.html')


@app.route('/romantic')
def romantic():
    return render_template('pages/romantic.html')


@app.route('/breakfast_start')
def breakfast_page():
    return render_template('pages/breakfast_start.html')


@app.route('/breakfast')
def breakfast():
    return render_template('pages/breakfast.html')


@app.route('/bbq_start')
def bbq_page():
    return render_template('pages/bbq_start.html')


@app.route('/bbq')
def bbq():
    return render_template('pages/bbq.html')


@app.route('/birthday_start')
def birthday_page():
    return render_template('pages/birthday_start.html')


@app.route('/birthday')
def birthday():
    return render_template('pages/birthday.html')


@app.route('/cocktail', methods=['POST'])
def cocktail_p():
    print(request.get_json())
    return "hi"


if __name__ == "__main__":
    app.run()
