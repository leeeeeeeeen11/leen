from model import Base, Blog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def add_image(title, image, details): #example of a function for the database
	image_object = Image(
	title = title,
	image = image) #creating a new object to store in the database.
	session.add(image_object) #adding the object
	session.commit() #commiting changes.
