from flask import Flask, request, redirect
import cgi
#JINGA SETUP
import os
import jinja2

#where templates
template_dir = os.path.join(os.path.dirname(__file__),'templates')
#initialize jinja engine
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)


app = Flask(__name__)
app.config['DEBUG'] = True





@app.route("/homepage")
def index():
    template = jinja_env.get_template("Input_forms.html")

    return template.render(username='',user_error='',
    password='',pass_error ='',
    passwordVerify = '', passVerify_error = '',
    email = '',email_error = '')

@app.route('/homepage',methods=['POST'])
def homepage():
    template = jinja_env.get_template("Input_forms.html")
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
    
    if len(email) > 0 and len(email) < 3:
        email_error = "enter valid email"


    if not user_error and not pass_error and not passVerify_error and not email_error:
        return redirect('/welcomePage')
    else:
        return template.render(username=username,user_error=user_error,
        password = password,pass_error=pass_error,
        passVerify_error=passVerify_error,passwordVerify=passwordVerify,
        email=email, email_error=email_error)

@app.route("/welcomePage/",methods = ['POST'] )
def welcomePage():
    username = request.form['username']
    return (username)

app.run()