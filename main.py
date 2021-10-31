from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, jsonify, request, render_template, url_for,redirect
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

## Your code goes here! ##
  

@app.route('/')
def login():
  return render_template('home.html')





## And doesn't go after this line. ##

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
    debug=True
	)


  Base = declarative_base() #declaration of base.

class Image(Base):
	__tablename__ = 'image' #defining table
id = Column(Integer, primary_key = True) #id is the primary key which is the specific number given to each row in order to recognize it.
	title = Column(String) #added a column.
	image = Column(String) #added a column.
