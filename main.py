from flask import Flask, request, redirect,render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template("Input_forms.html")

@app.route("/",methods=['POST'])
def homepage():
    username = request.form['username']
    password =request.form['password']
    passwordVerify=request.form['passwordVerify']
    email = request.form['email']

    user_error = ''
    pass_error = ''
    passVerify_error = ''
    email_error = ''


    #USER ERROR
     #if " " in username = username-1 OK!
    username = username.strip()
    if (len(username)==0)or (len(username) > 20):
       user_error = "Please enter a username"
    if (len(username)>0 and len(username) < 3):
        user_error = "Username too short"
    if (" " in username):
        user_error = "No spaces allowed in username"

   
    #PASSWORD ERROR
    if len(password) == 0:
        pass_error = "Enter Password"
    if len(passwordVerify)== 0:
        passVerify_error = "Verify Password"
    if len(password) < 3 and len(password) > 20:
        pass_error = "Password length"
    if password != passwordVerify:
        pass_error = "passwords do not match"
        passVerify_error = "passwords do not match"
    if pass_error or passVerify_error:
        password = ""
        passwordVerify = ""



    #EMAIL ERROR    
    if (len(email) > 0 and len(email) < 3) and ( "@" not in email):
        email_error = "enter valid email"
    if " " in email:
        email_error = "Spaces invalid"


    if not user_error and not pass_error and not passVerify_error and not email_error:
        return redirect('/welcomePage?username='+ username)
    else:
        return render_template("Input_forms.html",username=username,user_error=user_error,
        password = password,pass_error=pass_error,
        passVerify_error=passVerify_error,passwordVerify=passwordVerify,
        email=email, email_error=email_error)

@app.route("/welcomePage/")
def welcomePage():
    
    username = request.args.get('username')
    return render_template("welcome.html",username=username)


app.run()