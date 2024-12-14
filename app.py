from flask import Flask,render_template,request,redirect
from pymongo import MongoClient

app = Flask(__name__)
my_client = MongoClient("localhost",27017)
my_db = my_client["paylaterdb"]
resss = my_db["resss"]
resss1 = my_db["resss1"]


 

@app.route("/home", methods=["GET"])
def frontend():
    return render_template("index.html")

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")


@app.route("/org_reg", methods=["GET","POST"])
def org_reg():
    if request.method == "POST":
        name = request.form["org_name"]
        phone = request.form["contactno"]
        GSTNo = request.form["gstno"]
        ITRNo = request.form["itrno"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        resss.insert_one({"name":name,"phone":phone,
                          "GSTNO":GSTNo,"ITRNO":ITRNo,
                          "Password1":password1,"Password2":password2 
                          })
        return redirect("/org_reg")
    else:
        return render_template("org_reg.html")


    
    

    

@app.route("/usr_reg", methods=["GET","POST"])
def usr_reg():
    if request.method == "POST":
        name= request.form["cus_name"]
        phone= request.form["contactno"]
        AadharNo = request.form["adharno"]
        PANdetails = request.form["panno"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        resss1.insert_one({"name":name,"phone":phone,
                          "AadharNo": AadharNo," PANdetails": PANdetails,
                          "Password1":password1,"Password2":password2 
                          })
        return redirect("/usr_reg")
        

    
    else:
        return render_template("usr_reg.html")

app.run(debug = True)
