from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')


@public.route('/login',methods=['post','get'])
def login():

    if 'btn' in request.form:
        uname=request.form['uname']
        pasw =request.form['pasw']

        q="select * from login where username='%s' and password='%s'"%(uname,pasw)
        res=select(q)


        if res:
            session['loginid']=res[0]["login_id"]
            utype=res[0]["usertype"]
            if utype == "admin":
                flash("Login Success")
                return redirect(url_for("admin.adminhome"))
            elif utype == "enquiryteam":
                q="select * from enquiry where login_id='%s'"%(session['loginid'])
                val1=select(q)
                if val1:
                    session['eid']=val1[0]['enquiry_id']
                    flash("Login Success")
                    return redirect(url_for("enquiry.enquiryhome"))
            elif utype == "nutritionaist":
                q="select * from nutretion where login_id='%s'"%(session['loginid'])
                val7=select(q)
                if val7:
                    session['nid']=val7[0]['nutretion_id']
                    flash("Login Success")
                    return redirect(url_for("nutritionaist.nutritionaisthome"))
               
            
            else:
                flash("failed try again")
                return redirect(url_for("public.login"))
        else:
            flash("Invalid Username or Password!")
            return redirect(url_for("public.login"))


    return render_template("login.html")


@public.route("/enquiry_reg",methods=['get','post'])
def enquiry_reg():
    if 'btn' in request.form:
        name=request.form['name']
        phone=request.form['phone']
        email=request.form['email']
       
        pwd=request.form['pwd']
        uname=request.form['uname']
      

        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("This Username already exist!, try register with new one.")
        else:
            q="insert into login values(null,'%s','%s','pending')"%(uname,pwd)
            lid=insert(q)
            q="insert into enquiry values (NULL,'%s','%s','%s','%s')"%(lid,name,phone,email)
            insert(q)
            flash("Registration successfull")
            return redirect(url_for("public.login"))
    return render_template("enquiry_reg.html")


@public.route("/nutritionaist_reg",methods=['get','post'])
def nutritionaist_reg():
    if 'btn' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        phone=request.form['phone']
        email=request.form['email']
        place=request.form['place']
       
        pwd=request.form['pwd']
        uname=request.form['uname']
      

        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("This Username already exist!, try register with new one.")
        else:
            q="insert into login values(null,'%s','%s','pending')"%(uname,pwd)
            lid=insert(q)
            q="insert into nutretion values (NULL,'%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,place,phone,email)
            insert(q)
            flash("Registration successfull")
            return redirect(url_for("public.login"))
    return render_template("nutritionaist_reg.html")
