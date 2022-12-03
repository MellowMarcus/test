from flask import Flask, render_template, flash, request, redirect, url_for

# Create a Flask Instance
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
