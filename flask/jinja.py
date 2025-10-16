#biulding dynamic url
#variable rule
#Jinja 2 template engine


##jinja 2 template engine
'''
{{  }}expressions to print output in html
{# #} comments
{% %} statements to control the flow of the template conditions,loop'''






from flask import Flask,render_template,request,redirect,url_for
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

@app.route("/submit_name",methods=['GET','POST'])
def submit_name():
    if request.method == 'POST':
        name=request.form['name']
        return f"hello {name}, your form has been submitted successfully"
    return render_template("form.html")

##variable rule
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"
    return render_template("result.html",results=res)
      

@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score >= 50:
        res="PASS"
    else:
        res="FAIL"

    exp={'score':score,'results':res}
    return render_template("result1.html",results=exp)



#if condition
@app.route("/successif/<int:score>")
def successif(score):
    return render_template("result.html",results=score)


@app.route("/fail/<int:score>")
def fail(score):
    return render_template("result1.html",results=score)


@app.route("/getresults", methods=['GET'])
def getresults():
    return render_template("getresults.html")

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method =='POST':
        science=float(request.form['science'])
        math=float(request.form['math'])        
        english=float(request.form['english'])
        history=float(request.form['history'])
        total_score = (science + math + english + history) / 4
        
    return redirect(url_for('successres', score=total_score)) #for creating duynamic url and to redirect
    

if __name__=="__main__":
    #local host #debug=True will reload the server automatically when you make changes to the code
    app.run(debug=True) #local host #debug=True will reload the server automatically when you make changes to the code
