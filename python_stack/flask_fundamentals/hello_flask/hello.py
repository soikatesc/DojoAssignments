

from flask import Flask, render_template,request,redirect

app = Flask(__name__) #Global varibale __name__ tells Flask whether or not we are running the file

@app.route('/') 
def index():
	return render_template('index.html') #render the html and reutrn it

@app.route('/users/<username>')
def show_user_profile(username):
	print username
	return render_template





# @app.route('/users', methods=['POST'])
# def create_user():
# 	print "got post info"
# 	name = request.form['name']
# 	email = request.form['email']

# 	return redirect('/')

#run our application in debug mode
app.run(debug=True)