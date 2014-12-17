from django.db import models
from google.appengine.ext import db
from google.appengine.api import users
import webapp2
import datetime



class Pictures(db.Model):
	perlink=db.StringProperty()
	author = db.StringProperty()
	createdate= db.DateTimeProperty()
	title = db.StringProperty()
# Create your models here.
class Questions(db.Model):
	# location 			= db.StringProperty(required=False)
	description= db.StringProperty(multiline=True)
	title = db.StringProperty(required=False)
	votes = db.IntegerProperty(default=0)
	createdate= db.DateTimeProperty()
	modifydate= db.DateTimeProperty()
	identifier = db.StringProperty()
	author= db.UserProperty()

	meta = {
		'indexes': [
			#'location',
			'author',
			'title',
			'votes',
			'id'
		]
	}

class Tags(db.Model):
	tag_name= db.StringProperty(required=False)
	question_id= db.StringProperty()


class Answers(db.Model):
	title = db.StringProperty(required=False)
	description = db.StringProperty(multiline=True)
	author = db.UserProperty()
	identifier = db.StringProperty()
	createdate= db.DateTimeProperty()
	modifydate= db.DateTimeProperty()
	votes = db.IntegerProperty(default=0)


class Votes(db.Model):
	author = db.UserProperty(required=False)
	val = db.IntegerProperty(default=0)
