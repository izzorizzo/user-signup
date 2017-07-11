from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods= ["POST", "GET"])
def signup():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        verify = request.form["verify"]
        email = request.form["email"]

        username_error = ''
        password_error = ''
        verify_error = '' 
        email_error = ''

        def validate_username(username):
            #checks length of username
            if len(username) >=3 and len(username) <20:
                return True
            else:
                username_error = "Please input a username between 3 and 20 characters." 
                #wipe out username if wrong
                username = ""
            
        
        def validate_password(password):
            # checks length of password
            if len(password) >=3 and len(password) <20:
                return True
            else:
                password_error = "Please input a password between 3 and 20 characters." 
                #wipe out password fields if error
                password = ""
                verify = ""

        
        def validate_verify(verify):
            # checks passwords match
            if password == verify:
                return True
            else:
                verify_error = "Passwords do not match."
                #wipe out if passwords don't match
                password = ""
                verify = ""


        def validate_email(email):
            if (len(email) >=3 and len(email) <20) and "@" in email and "." in email and " " in email: 
                return True
            else: 
                email_error = "Please input valid email address that is between 3 and 20 characters long."
                email = ""


        if not username_error and not password_error and not verify_error and not email_error:
            return redirect("/welcome")


    return render_template("signup.html", title="Signup")

@app.route("/welcome", methods = ["POST", "GET"])
def welcome():
    return render_template("welcome.html", title="WELCOME")

app.run()