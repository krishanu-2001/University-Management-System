from flask import *
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
import hashlib
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_mail import Mail
from flask_mail import Message


app = Flask(__name__)
CORS(app)

app.config.from_object('config.DevConfig')

mysql = MySQL(app)
mail = Mail(app)


#UTIL functions
def get_reset_token(id, expires_sec=600):
    s = Serializer(app.config['SECRET_KEY'], expires_sec)
    return s.dumps({'user_id': id}).decode('utf-8')
def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return user_id
def send_reset_mail(user,email,id):
    token = get_reset_token(id)
    msg = Message('Password Reset Request',
                  sender='noreply@universitymanagementsystem.com',
                  recipients=[email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, user=user , _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

# endUtils


def login(user):
    flash = ""
    flag = 1
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        user_id = userDetails['user_id']
        password = userDetails['password']
        hashedpassword = hashlib.md5(password.encode()).hexdigest()
        cur = mysql.connection.cursor()
        if(user=="student"):
            cur.execute("SELECT COUNT(*), password, first_name FROM student WHERE student_id = '%s' "% (user_id))
            rv = cur.fetchall()
            flag = (rv[0][0])
            dbpassword = (rv[0][1])
            name = (rv[0][2])
            mysql.connection.commit()
            cur.close()
            #give access here!!
            if(flag >= 1 and hashedpassword == dbpassword):
                session['id'] = user_id
                session['role'] = 'student'
                return redirect(url_for('student_dashboard'))
            else:
                flash = "Wrong Id or Password!"
                flag = 0
        elif(user=="faculty"):
            cur.execute("SELECT COUNT(*), password, first_name FROM faculty WHERE faculty_id = '%s' "% (user_id))
            rv = cur.fetchall()
            flag = (rv[0][0])
            dbpassword = (rv[0][1])
            name = (rv[0][2])
            mysql.connection.commit()
            cur.close()
            #give access here!!
            if(flag >= 1 and hashedpassword == dbpassword):
                session['id'] = user_id
                session['role'] = 'faculty'
                return redirect(url_for('faculty_dashboard'))
            else:
                flash = "Wrong Id or Password!"
                flag = 0
        elif(user=="admin"):
            cur.execute("SELECT COUNT(*), password, name FROM admin WHERE admin_id = '%s' "% (user_id))
            rv = cur.fetchall()
            flag = (rv[0][0])
            dbpassword = (rv[0][1])
            name = (rv[0][2])
            mysql.connection.commit()
            cur.close()
            #give access here!!
            if(flag >= 1 and hashedpassword == dbpassword):
                session['id'] = user_id
                session['role'] = 'admin'
                return redirect(url_for('admin_dashboard'))
            else:
                flash = "Wrong Id or Password!"
                flag = 0
        else:
            flash = "Some Error Occured!"
            flag = 0
            return flash,400
    if flag != 0:
        flash = ""
    if(user=="student"):
        return render_template('student/login.html', flash = flash)
    elif(user=="faculty"):
        return render_template('faculty/login.html', flash = flash)
    elif(user=="admin"):
        return render_template('admin/login.html', flash = flash)

def logout():
    flash = "Logged out successfully!"
    if(session.get('id')):
        session.pop('id')
        session.pop('role')
    return render_template('index.html', flash = flash)


def resetpassword(user):
    flash="Reset link has been sent to your registered Email."
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        id = userDetails['user_id']
        if(user=="student"):
            cur = mysql.connection.cursor()
            cur.execute("SELECT emailid FROM student WHERE student_id = '%s' "% (id))
            rv = cur.fetchall()
            if (rv==() ):
                flash="Invalid Username"
                return render_template('resetrequest.html', flash = flash, user=user)       
            else:
                email=rv[0][0]
                send_reset_mail(user,email,id) 
            cur.close()
            return render_template('student/login.html', flash = flash)
        elif(user=="faculty"):
            cur = mysql.connection.cursor()
            cur.execute("SELECT emailid FROM faculty WHERE faculty_id = '%s' "% (id))
            rv = cur.fetchall()
            if (rv==() ):
                flash="Invalid Username"
                return render_template('resetrequest.html', flash = flash, user=user)       
            else:
                email=rv[0][0]
                send_reset_mail(user,email,id) 
            cur.close()
            return render_template('faculty/login.html', flash = flash)
        elif(user=="admin"):
            cur = mysql.connection.cursor()
            cur.execute("SELECT emailid FROM admin WHERE admin_id = '%s' "% (id))
            rv = cur.fetchall()
            if (rv==() ):
                flash="Invalid Username"
                return render_template('resetrequest.html', flash = flash, user=user)       
            else:
                email=rv[0][0]
                send_reset_mail(user,email,id) 
            cur.close()
            return render_template('admin/login.html', flash = flash)
    flash=""
    return render_template('resetrequest.html', flash = flash, user=user)               

def reset_token(user,token):
    user_id=verify_reset_token(token)
    flash=""
    if user_id is None:
        flash="Your token is Invalid or Expired."
        return render_template('resetrequest.html', flash = flash, user=user)
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        password = userDetails['password'] 
        cpassword = userDetails['confirmpassword']
        hashedpassword = hashlib.md5(password.encode()).hexdigest()
        if(password!=cpassword):
            flash="Passwords do not match. Check Password."
            render_template('resetpassword.html', flash = flash, user=user ,token=token)
        else:
            if(user=="student"):
                cur = mysql.connection.cursor()
                cur.execute("UPDATE student SET password = %s WHERE student_id = %s",(hashedpassword, user_id))
                mysql.connection.commit()
                cur.close()
                flash="Your password has been updated!"
                return render_template('student/login.html', flash = flash)
            elif(user=="faculty"):
                cur = mysql.connection.cursor()
                cur.execute("UPDATE faculty SET password = %s WHERE faculty_id = %s",(hashedpassword, user_id))
                mysql.connection.commit()
                cur.close()
                flash="Your password has been updated!"
                return render_template('faculty/login.html', flash = flash)
            elif(user=="admin"):
                cur = mysql.connection.cursor()
                cur.execute("UPDATE admin SET password = %s WHERE admin_id = %s",(hashedpassword, user_id))
                mysql.connection.commit()
                cur.close()
                flash="Your password has been updated!"
                return render_template('admin/login.html', flash = flash)

    return render_template('resetpassword.html', flash = flash, user=user ,token=token)   