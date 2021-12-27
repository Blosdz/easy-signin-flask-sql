from flask import Flask
from flask import render_template,request,redirect,url_for,request
import sqlite3

from flask.helpers import url_for

app=Flask(__name__)


@app.route("/",methods=["POST","GET"])
def usuario():
    if request.method=="POST":
        nombreuser=request.form["username"]
        password=request.form["password"]
        conn=sqlite3.connect('userData.db')    
        c=conn.cursor()
        statement=f"SELECT * from userDatas WHERE name='{nombreuser}' AND passWord='{password}'"
        c.execute(statement)
        if not c.fetchone():
            return render_template("log.html")
        else:
            return render_template("succesLogin.html")
    else:
        request.method=="GET"
        return render_template('log.html')

@app.route("/register",methods=["POST","GET"])
def registerFunct():
    conn=sqlite3.connect('userData.db')
    c=conn.cursor()
    if request.method=="POST":    
        if (request.form["registerUsername"]!="" and request.form["registerEmail"]!="" and request.form["registerPassword"]!=""):
            userRegister=request.form["registerUsername"]
            emailRegister=request.form["registerEmail"]
            passwordRegister=request.form["registerPassword"]
            
            statement=f"SELECT * from userDatas WHERE name='{userRegister}' AND email='{emailRegister}' AND passWord='{passwordRegister}'"
            c.execute(statement)
            data=c.fetchone()
            if data:
                return render_template("error.html")
            else:
                if not data:
                    c.execute("INSERT INTO userDatas (name,email,passWord) VALUES(?,?,?)",(userRegister,emailRegister,passwordRegister))
                    conn.commit()
                    conn.close()
                return render_template("succesLogin.html") 
    return render_template("register.html")
    



if __name__=="__main__":
    app.run(debug=True)

#thing() create table 


