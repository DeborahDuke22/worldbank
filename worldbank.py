import sqlite3
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# database details - to remove some duplication
db_name = 'world_bank_data.db'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name=request.form['count']
        if name == "Nigeria":
            return redirect(url_for("country", country=country))
        if name == "Ghana":
            return redirect(url_for("country_2", country_2=country_2))
        else:
            return('Please enter either Nigeria or Ghana')

        

    return render_template('index.html')

@app.route("/")

@app.route('/country')
def country():
    # open the connection to the database
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from country")
    rows = cur.fetchall()
    conn.close()
    return render_template('country.html', rows=rows)

@app.route('/dev/<count_id>')
def dev(count_id):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from statuses
    cur.execute("select * from deployments WHERE country_name_id =?", (count_id,))
    rows = cur.fetchall()
    #get results from deployments
    cur.execute("select * from country WHERE count_id =?", (count_id,))
    country = cur.fetchall()
    conn.close()
    return render_template('dev.html', rows=rows, country=country)


@app.route('/country_2')
def country_2():
    # open the connection to the database
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from indicators")
    rows = cur.fetchall()
    conn.close()
    return render_template('country_2.html', rows=rows)
    
@app.route('/dev_2/<count_ID>')
def dev_2(count_ID):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from statuses
    cur.execute("select * from years WHERE count_name_id =?", (count_ID,))
    rows = cur.fetchall()
    #get results from deployments
    cur.execute("select * from indicators WHERE count_ID =?", (count_ID,))
    country_2 = cur.fetchall()
    conn.close()
    return render_template('dev_2.html', rows=rows, country_2=country_2)