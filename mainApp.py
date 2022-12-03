from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import date

# Create a Flask Instance
app = Flask(__name__)

app.config['SECRET_KEY'] = "secret hehehe"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Views
@app.route('/name', methods=['GET', 'POST'])
def name():
	name = None
	form = NamerForm()
	# Validate Form
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		flash("Form Submitted Successfully!")
		
	return render_template("name.html", 
		name = name,
		form = form)



@property
def password(self):
	raise AttributeError('password is not a readable attribute!')

@password.setter
def password(self, password):
	self.password_hash = generate_password_hash(password)

def verify_password(self, password):
	return check_password_hash(self.password_hash, password)





#Models
class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False, unique=True)
	name = db.Column(db.String(200), nullable=False)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)
	profile_pic = db.Column(db.String(), nullable=True)

	# Do some password stuff!
	password_hash = db.Column(db.String(128))

