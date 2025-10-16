from flask import Flask
'''
it creates an instance of the Flask class, which will be your MSGI (web server gateway interface
application.'''
##WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return " Hey girl, this is best course .Welcome to flask course.This is a amazing course to learn flask"
@app.route("/index")
def index():
    return "Welcome to index page"
if __name__=="__main__":
    app.run(debug=True) #local host #debug=True will reload the server automatically when you make changes to the code
             