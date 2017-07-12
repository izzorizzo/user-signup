from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup", methods= ["POST", "GET"])
def signup():

    if request.method == "POST":

        #requests info from form
        username = request.form["username"]
        password = request.form["password"]
        verify = request.form["verify"]
        email = request.form["email"]

        #empty strings for errors 
        username_error = ""
        password_error = ""
        verify_error = "" 
        email_error = ""

        # checks length of username
        if len(username) >=3 and len(username) <20:
            return True
        else:
            username_error = "Please input a username between 3 and 20 characters." 
            # wipe out username if wrong
            username = ""
            
        # checks length of password
        if len(password) >=3 and len(password) <20:
            return True
        else:
            password_error = "Please input a password between 3 and 20 characters." 
            # wipe out password fields if error
            password = ""
            verify = ""


        # checks passwords match
        if password == verify:
            return True
        else:
            verify_error = "Passwords do not match."
            # wipe out if passwords don't match
            password = ""
            verify = ""


        # validates email
        if (len(email) >=3 and len(email) <20) and "@" in email and "." in email and " " not in email: 
            return True
        else: 
            email_error = "Please input valid email address that is between 3 and 20 characters long."
            # wipes out email field
            email = ""

        #redirects if no errors show up
        if (username_error == "") and (password_error == "") and (verify_error == "") and (email_error == ""):
            return redirect("/welcome.html?username={0}".format(username))
        else: 
            return render_template("signup.html", title="Signup", username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, password=password, verify=verify, email=email) 

    return render_template("signup.html", title="Signup")


@app.route("/welcome", methods = ["POST", "GET"])
def welcome():
    username = request.args.get('username')
    return render_template("welcome.html", title="WELCOME", username=username)

app.run()