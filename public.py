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
            elif utype == "player":
                q="select * from player where login_id='%s'"%(session['loginid'])
                val8=select(q)
                if val8:
                    session['pid']=val8[0]['player_id']
                    flash("Login Success")
                    return redirect(url_for("player.playerhome"))
                
            elif utype == "cadmin":
                q="select * from club where login_id='%s'"%(session['loginid'])
                val1=select(q)
                if val1:
                    session['clubid']=val1[0]['club_id']
                    flash("Login Success")
                    return redirect(url_for("clubadmin.clubhome"))   
                
                
            elif utype == "psysician":
                q="select * from psysician where login_id='%s'"%(session['loginid'])
                val1=select(q)
                if val1:
                    session['psyid']=val1[0]['psysician_id']
                    flash("Login Success")
                    return redirect(url_for("physio.physiohome")) 
                
                    
            elif utype == "user":
                q="select * from user where login_id='%s'"%(session['loginid'])
                val1=select(q)
                if val1:
                    session['uid']=val1[0]['user_id']
                    flash("Login Success")
                    return redirect(url_for("user.userhome"))     
            
            else:
                flash("failed try again")
                return redirect(url_for("public.login"))
        else:
            flash("Invalid Username or Password!")
            return redirect(url_for("public.login"))


    return render_template("login.html")

import uuid
@public.route("/enquiry_reg",methods=['get','post'])
def enquiry_reg():
    if 'btn' in request.form:
        name=request.form['name']
        phone=request.form['phone']
        email=request.form['email']
        dob=request.form['dob']
        photo=request.files['photo']
        path="static/uploads/"+str(uuid.uuid4())+photo.filename
        photo.save(path)
       
        pwd=request.form['pwd']
        uname=request.form['uname']
      

        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("This Username already exist!, try register with new one.")
        else:
            q="insert into login values(null,'%s','%s','pending')"%(uname,pwd)
            lid=insert(q)
            q="insert into enquiry values (NULL,'%s','%s','%s','%s','%s','%s')"%(lid,name,phone,email,path,dob)
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
        dob=request.form['dob']
        photo=request.files['photo']
        path="static/uploads/"+str(uuid.uuid4())+photo.filename
        photo.save(path)
       
        pwd=request.form['pwd']
        uname=request.form['uname']
      

        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("This Username already exist!, try register with new one.")
        else:
            q="insert into login values(null,'%s','%s','pending')"%(uname,pwd)
            lid=insert(q)
            q="insert into nutretion values (NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,place,phone,email,path,dob)
            insert(q)
            flash("Registration successfull")
            return redirect(url_for("public.login"))
    return render_template("nutritionaist_reg.html")





@public.route('/clubreg',methods=['get','post'])
def clubreg():
    if 'register' in request.form:
        club=request.form['club']
        place=request.form['place']
        phone=request.form['phone']
        photo=request.files['photo']
        path="static/uploads/"+str(uuid.uuid4())+photo.filename
        photo.save(path)
        uname=request.form['uname']
        passw=request.form['passw']
        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("This Username already exist!, try register with new one.")
        else:
            q="insert into login values(null,'%s','%s'.'pending')"%(uname,passw)
            res=insert(q)
            q="insert into club values(null,'%s','%s','%s','%s','%s')"%(res,club,place,phone,path)
            insert(q)
            flash('registration Successfull')
            return redirect(url_for("public.login"))
        
    return render_template('club_register.html')




@public.route('/psyreg',methods=['get','post'])
def psyreg():
    id=request.args['id']
    data={}
    if 'btn' in request.form:
        fname=request.form['fname']
   
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        dob=request.form['dob']
        photo=request.files['photo']
        path="static/uploads/"+str(uuid.uuid4())+photo.filename
        photo.save(path)
       
        pwd=request.form['pwd']
        uname=request.form['uname']
      

        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("This Username already exist!, try register with new one.")
        else:
            q="insert into login values(null,'%s','%s','pending')"%(uname,pwd)
            lid=insert(q)
            q="insert into psysician values (NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,session['clubid'],fname,place,phone,email,path,dob)
            insert(q)
            flash("Registration successfull")
            return redirect(url_for("public.login"))
        
    return render_template('phy_reg.html',data=data)




@public.route('/clubs')
def clubs():
    data={}
    q="select * from club"
    res=select(q)
    data['club']=res
    
    return render_template('view_clubs.html',data=data)


@public.route('/viewdetails')
def viewdetails():
    data={}
    id=request.args['id']
    q="select * from club where club_id='%s'"%(id)
    data['club']=select(q)
    return render_template('view_club_details.html',data=data)



@public.route('/userreg',methods=['get','post'])
def userreg():
    id=request.args['id']
    if 'submit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        dob=request.form['dob']
        adhr=request.form['adhar']
        uname=request.form['uname']
        passw=request.form['passw']
        photo=request.files['photo']
        path="static/uploads/"+str(uuid.uuid4())+photo.filename
        photo.save(path)
        pic=request.files['pic']
        path2="static/uploads/"+str(uuid.uuid4())+pic.filename
        pic.save(path)
        
        q="insert into login values(null,'%s','%s','pending')"%(uname,passw)
        res=insert(q)
        q="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(res,id,fname,lname,place,phone,email,adhr,path,dob,path2)
        insert(q)
        return redirect(url_for('public.login'))
        
    return render_template('user_reg.html')


@public.route('/playerreg',methods=['get','post'])
def playerreg():
    id=request.args['id']
    data={}
    
    if 'register' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        dob=request.form['dob']
        adhr=request.form['adhr']
        photo=request.files['photo']
        path="static/uploads/"+str(uuid.uuid4())+photo.filename
        photo.save(path)
        uname=request.form['uname']
        passw=request.form['passw']
        import random

        rno = random.randint(100000, 999999)
        
        q="insert into login values(null,'%s','%s','player')"%(uname,passw)
        res=insert(q)
        q="insert into player values(null,'%s','%s','%s','%s','%s','%s','%s','%s','pending','%s','%s','%s')"%(res,id,fname,lname,place,phone,email,rno,adhr,path,dob)
        insert(q)
        flash("registration Successfull")
        return redirect(url_for('public.login'))
    
    return render_template('player_reg.html',data=data)