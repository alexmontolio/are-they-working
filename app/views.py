from flask import render_template, request, redirect, url_for
from app import app, db
#from datetime import datetime
from .models import Elevator, Outage, Residents, Management

#Elevator background debug
#class Elevator(object):
#	is_left_working = True
#	is_right_working = False

@app.route('/', methods = ['GET', 'POST'])
def index():
	elevator = Elevator.query.filter_by(building="300 E.138th").first_or_404()
	if request.method == 'POST':
		if request.form['submit'] == 'Report Left Elevator Broken':
			elevator.left = False
			#outage = Outage(number, 1, datetime.now())
			db.session.commit()
			return redirect(url_for('sent'))
		elif request.form['submit'] == 'Report Right Elevator Broken':
			elevator.right = False
			db.session.commit()
			return redirect(url_for('sent'))
		elif request.form['submit'] == 'Report Left Elevator Fixed':
			elevator.left = True
			db.session.commit()
			return redirect(url_for('sent'))
		elif request.form['submit'] == 'Report Right Elevator Fixed':
			elevator.right = True
			db.session.commit()
			return redirect(url_for('sent'))
		else:
			#Raise request error
			pass		
	return render_template('index.html', elevator=elevator)
	
@app.route('/about')
def about():
	elevator = Elevator.query.filter_by(building="300 E.138th").first_or_404()
	return render_template('about.html', elevator=elevator,
							title='Are They Working - About')
							
@app.route('/sent')
def sent():
	#Must actually make redirect page
	#Reroute to about page for now
	elevator = Elevator.query.filter_by(building="300 E.138th").first_or_404()
	return render_template('about.html', elevator=elevator,
							title='Are They Working - About')

@app.route('/outages')
def outages():
	elevator = Elevator.query.filter_by(building="300 E.138th").first_or_404()
	return render_template('outages.html', elevator=elevator)

@app.route('/mailing')
def mailing():
	elevator = Elevator.query.filter_by(building="300 E.138th").first_or_404()
	return render_template('signup.html', elevator=elevator)