import webapp2 # NOTE: pull in a library for using appengine
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import urlfetch
import json

the_jinja_env=jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True)
# NOTE: For c++ clas
# C++:do the mod operation with double : fmod(3.5,1)
# X%10 to print out the last digits of a number: 3456 %10
# x%100 to print the last two digits
# To print the number without the last digit, 124412/10
# Second to last (52342%100)/10, (234234234/10)%10
class Mainhandler(ndb.model):
    def get(self):
        Mian_template=the_jinja_env.get_template('templates/index.html')
        self.response.write(Main_template.render())
    def post(self):
        Mian_template=the_jinja_env.get_template('templates/index.html')
        self.response.write(Main_template.render())

app=webapp2.WSGIApplication([
('/',Mainhandler)
],debug=True)
