from flask import Flask, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True


form = '''
    <style>
        .error {{ color: red; }}
    </style>
    <h1>User Signup</h1>
    <form method='POST'>

        <label>Username
            <input name="username" type="text" value='{username}' />
        </label>
        <span class="error">{user_error}</span>
        <br>

        <label>Password
            <input name="password" type="password" value='{password}' />
        </label>
        <span class="error">{pass_error}</span>
        <br>
        <label>Verify Password
            <input name="passwordVerify" type="password" value='{passwordVerify}' />
        </label>
        <span class="error">{passVerify_error}</span>
        <br>

        <label>Email(optional)
            <input name="email" type="text" value='{email}' />
        </label>
        <span class="error">{email_error}</span>
        <br>
        <input type="submit" value="submit" />

        
    </form>

'''


@app.route("/homepage")
def index():
    return form.format(username='',user_error='',
    password='',pass_error ='',
    passwordVerify = '', passVerify_error = '',
    email = '',email_error = '')

@app.route('/homepage',methods=['POST'])
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
    
    if len(email) > 0 and len(email) < 3:
        email_error = "enter valid email"


    if not user_error and not pass_error and not passVerify_error and not email_error:
        return redirect('/welcomePage')
    else:
        return form.format(username=username,user_error=user_error,
        password = password,pass_error=pass_error,
        passVerify_error=passVerify_error,passwordVerify=passwordVerify,
        email=email, email_error=email_error)

@app.route("/welcomePage/",methods = ['POST'] )
def welcomePage():
    username = request.form['username']
    return (username)

app.run()