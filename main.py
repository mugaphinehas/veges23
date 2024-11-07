from flask import Flask,render_template,flash,url_for,request
import pymysql


app=Flask(__name__)



@app.route("/")
def navbar():
    return render_template("home.html")




@app.route("/")
def Home():
    return render_template("home.html")


@app.route("/portifolio")
def portifolio():
    return render_template("portifolio.html")

@app.route("/aboutus")
def aboutus():
    return render_template("about.html")


@app.route("/login")
def login():
    return render_template("login.html")
    
@app.route("/contactus")  
def contactus():
    return render_template("contactus.html")




if __name__ == "__main__":
  app.run(debug=True)



