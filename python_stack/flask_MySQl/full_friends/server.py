from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
@app.route('/')
def index():
	# friends = mysql.query_db("SELECT * FROM friends")
	# print friends

	# query = "SELECT * FROM friends"
	# friends = mysql.query_db(query)
	query = "SELECT * FROm friends"
	friends = mysql.query_db(query)
	return render_template('index.html',all_friends=friends)
# @app.route('/friends/<friend_id>')
# def show():
#     # add a friend to the database!
# 	query = "SELECT * FROM friends WHERE id = :specific_id"
# 	data = {'specific_id': friend_id}
# 	friends = mysql.query_db(query, data)
# 	return render_template('index.html', one_friend=friends[0])

@app.route('/create', methods=['POST'])
def create():
	print request.form['name']
	print request.form['age']
	# add a friend to the database!
	query = "INSERT INTO friends (name, age, created_at, updated_at)VALUES (:name, :age, NOW(), NOW())"
	data = {
             'name': request.form['name'],
             'age':  request.form['age'],
           }
    # Run query, with dictionary values injected into the query.
	mysql.query_db(query, data)

	return redirect('/')
app.run(debug=True)