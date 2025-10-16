

from flask import Flask,render_template,request
'''
it creates an instance of the Flask class, which will be your MSGI (web server gateway interface
application.'''
##WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return " <html><H1>Hey girl, this is best course .Welcome to flask course.This is a amazing course to learn flask</H1></html>"
@app.route("/index",methods=['GET'])
def index():

    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f"hello {name}, your form has been submitted successfully"
    return render_template("form.html")
@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f"hello {name}, your form has been submitted successfully"
    return render_template("form.html")
if __name__=="__main__":
    app.run(debug=True) #local host #debug=True will reload the server automatically when you make changes to the code
        