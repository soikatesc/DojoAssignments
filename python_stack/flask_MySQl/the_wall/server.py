from flask import Flask, request, redirect, render_template, session, flash
import os, binascii
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = os.urandom(24)

mysql = MySQLConnector(app,'the_wall')
@app.route('/')
def index():
	return render_template('index.html')


# rendering wall.html page
@app.route('/wall')
def wall():
	# print session['user_id']
	if 'user_id' not in session:
		return redirect('/')
	else:
		# user_query = "SELECT * FROM messages"
		user_id = session['user_id']
		# print user_id
		# user_query = "SELECT * FROM messages WHERE user_id= :user_id"
		# query_data = {'user_id':user_id}
		# message_from_db = mysql.query_db(user_query)
		# # query_data
		# show_message = message_from_db
		# # [0]['message']


		# query_messages = "SELECT users.id as user_id, comments.comment, users.first_name,users.last_name, messages.id as message_id, messages.created_at,messages.message FROM users LEFT JOIN messages ON users.id = messages.user_id LEFT JOIN comments ON users.id = comments.user_id LEFT JOIN comments as comments2 on messages.id = comments2.message_id"
		query_messages = "SELECT users.first_name as message_user_first_name,users.last_name as message_user_last_name, users2.first_name as comment_user_first_name, users2.last_name as comment_user_last_name, messages.created_at as message_created_date, messages.message, messages.id as message_id,users2.id as comment_user_id, comments.comment, comments.created_at as comment_date from messages left join users on messages.user_id = users.id left join comments on comments.message_id = messages.id left join users as users2 on comments.user_id = users2.id;"
		message_from_db = mysql.query_db(query_messages)
		print message_from_db

		#list of all the dictionary : message_form_db
		# print message_from_db
		message_ids = []
		messages = []
		for dicts in message_from_db:
			print '/////////////////////////////////'
			if dicts['message_id'] not in message_ids:
				message_ids.append(dicts['message_id'])
				new_message = {}
				new_message['message_id'] = dicts['message_id']
				new_message['message'] = dicts['message']
				new_message['message_user_first_name'] = dicts['message_user_first_name']
				new_message['message_user_last_name'] = dicts['message_user_last_name']
				new_message['message_user_created_at'] = dicts['message_created_date']
				new_message['comments'] = []
				if dicts['comment'] != None:
					new_comment = {}
					new_comment['comment'] = dicts['comment']
					new_comment["comment_user_first_name"] = dicts['comment_user_first_name']
					new_comment["comment_user_last_name"] = dicts['comment_user_last_name']
					new_comment['comment_date'] = dicts['comment_date']
					new_message['comments'].append(new_comment)
				
				messages.append(new_message)
			else:
				if dicts['comment'] != None:
					new_comment = {}
					new_comment['comment'] = dicts['comment']
					new_comment["comment_user_first_name"] = dicts['comment_user_first_name']
					new_comment["comment_user_last_name"] = dicts['comment_user_last_name']
					new_comment['comment_date'] = dicts['comment_date']
					messages[-1]['comments'].append(new_comment)

		# for message in messages:
		# 	# print message
		# 	print message['message']
		# 	# print message['comments']
		# 	for comment in message['comments']:
		# 		print comment['comment']

		print message_ids
		print messages

		return render_template('wall.html', show_messages = messages)


#logout by clearing session
@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')


@app.route('/messages', methods=['POST'])
def messages():
	# print request.form['messege']
	# user_id = session['user_id']
	insert_query = "INSERT INTO messages (message,user_id,created_at,updated_at) VALUES (:message,:user_id, NOW(), NOW())"
	query_data = {
	  'message':request.form['messege'],
	  'user_id': session['user_id']
	}
	mysql.query_db(insert_query, query_data)
	
	return redirect('/wall')


#inserting comment into database
@app.route('/comments', methods=['POST'])
def comments():
	comment = request.form['comment']
	message_id = request.form['message_id']
	# print comment
	insert_query = "INSERT INTO comments (comment,user_id,message_id,created_at,updated_at) VALUES (:comment,:user_id,:message_id, NOW(), NOW())"
	query_data = {
	  'comment':request.form['comment'],
	  'user_id': session['user_id'],
	  'message_id': request.form['message_id'],
	}
	mysql.query_db(insert_query, query_data)
	
	return redirect('/wall')


@app.route('/login', methods=['POST'])
def login():

	email = request.form['email']
	password = request.form['password']
	# email_query = "SELECT email FROM users"
	# emails = mysql.query_db(email_query)
	# print emails

	
	# for i in emails:
	# 	# flash(i['email'])
	# 	if i['email'] == request.form['email']:
	# 		break

	

	user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
	query_data = {'email':email}
	user = mysql.query_db(user_query, query_data)

	# print user

	if user[0]:
		encrypted_password = md5.new(password + user[0]['salt']).hexdigest();
		print 'new encrypted password', encrypted_password
		if user[0]['password'] == encrypted_password:
			print 'successful'
			session['user_id'] =user[0]['id']
			session['user'] = {'first_name': user[0]['first_name'],
						'last_name': user[0]['last_name']
						}
			return redirect('/wall')
		else:
			flash('invalid password')
	else:
		flash('invalid email')
	return redirect('/')

@app.route('/regestration', methods=['POST'])
def regestration():
	email = request.form['email']
	first_name = request.form['first-name']
	last_name = request.form['last-name']
	password = request.form['password']
	confirm_password = request.form['passwordconfirm']


	error = True
	#len(first_name) & len(last_name) & len(password) & len(confirm_password)<1
	if len(first_name)<2 or len(last_name)<2:
		flash('letters only, at least 2 characters and that it was submitted')
		error = False
	elif not str.isalpha(str(first_name)) or not str.isalpha(str(last_name)):
		flash('letters only, at least 2 characters and that it was submitted')
		error = False
	elif not EMAIL_REGEX.match(email):
		flash('email shoud be vaild email')
		error = False
	elif len(password)<9:
		flash('password should be more than 8 characters')
		error = False
	elif password != confirm_password:
		flash('password not match')
		error = False

				##############################
				# inserting to database		#
				##############################
	if error == True:
		salt = binascii.b2a_hex(os.urandom(15))
		encrypted_pw = md5.new(password + salt).hexdigest()
		# print encrypted_pw
		# print salt
		insert_query = "INSERT INTO users (first_name,last_name,email,password,salt,created_at,updated_at) VALUES (:first_name, :last_name,:email, :encrypted_pw, :salt, NOW(), NOW())"
		query_data = {
					  'first_name':first_name,
		              'last_name':last_name,
					  'email': email, 
					  'encrypted_pw': encrypted_pw, 
					  'salt': salt, 
					  }

		session['user_id'] = mysql.query_db(insert_query, query_data)

		return redirect('/wall')
	return redirect('/')

	
app.run(debug=True)