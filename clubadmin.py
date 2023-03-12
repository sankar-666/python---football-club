from flask import *
from database import *
import uuid

# import smtplib
# from email.mime.text import MIMEText
# from flask_mail import Mail

clubadmin=Blueprint('clubadmin',__name__)


@clubadmin.route('/clubhome')
def clubhome():
    
    return render_template('clubhome.html')



@clubadmin.route('/updateprofile',methods=['get','post'])
def updateprofile():
    data={}
    
    q="select * from club where club_id='%s'"%(session['clubid'])
    data['res']=select(q)
    
    if 'update' in request.form:
        club=request.form['club']
        place=request.form['place']
        phone=request.form['phone']
        q="update club set club='%s',place='%s',phone='%s' where club_id='%s'"%(club,place,phone,session['clubid'])
        update(q)
        flash ('profile Updated')
        return redirect(url_for('clubadmin.updateprofile'))
    return render_template('club_add_profile.html',data=data)



@clubadmin.route('/playeradd',methods=['get','post'])
def playeradd():
    data={}
    q="select * from player"
    data['player']=select(q)
    
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
        q="insert into player values(null,'%s','%s','%s','%s','%s','%s','%s','%s','pending','%s','%s','%s')"%(res,session['clubid'],fname,lname,place,phone,email,rno,adhr,path,dob)
        insert(q)
        flash("registration Successfull")
        return redirect(url_for('clubadmin.playeradd'))
    
    if 'action' in request.args:
        id=request.args['id']
        action=request.args['action']
        
    else:
        action=None

    if action=='delete':
        q="delete from player where player_id='%s'" %(id)
        delete(q)
        flash("successfull")
        return redirect(url_for('clubadmin.playeradd'))
        
    if action=='update':
        q="select * from player where player_id='%s'"%(id)
        data['playerupd']=select(q)   
        
    if 'edit' in request.form:
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
        
        q="update player set fname='%s',lname='%s',place='%s',phone='%s',email='%s',dob='%s',photo='%s',aadhar_no='%s' where player_id='%s'"%(fname,lname,place,phone,email,dob,path,adhr,id)
        update(q)
        flash("update Successfull")
        return redirect(url_for('clubadmin.playeradd'))
    return render_template('club_add_players.html',data=data)





@clubadmin.route('/aprovecoach',methods=['get','post'])
def aprovecoach():
    data={}
    
    if 'btn' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
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
            q="insert into coach values (NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,session['clubid'],fname,lname,place,phone,email,path,dob)
            insert(q)
            flash("Registration successfull")
            return redirect(url_for("clubadmin.aprovecoach"))
    
    
    
    
    q="select * from coach  inner join login using(login_id)"
    data['coach']=select(q)
    
    if 'action' in request.args:
        id=request.args['id']
        action=request.args['action']
        
    else:
        action=None

    if action=='approve':
        q="update login set usertype='coach' where login_id=(select login_id from coach where coach_id='%s')"%(id)
        update(q)
        flash("successfull")
        return redirect(url_for('clubadmin.aprovecoach'))
    
    if action=='reject':
        q="update login set usertype='reject' where login_id=(select login_id from coach where coach_id='%s')"%(id)
        update(q)
        flash("successfull")
        return redirect(url_for('clubadmin.aprovecoach'))
    
    
    if action=='update':
        q="select * from coach where coach_id='%s'"%(id)
        res=select(q)
        data['coachup']=res
        
        
    if 'edit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        dob=request.form['dob']
        photo=request.files['photo']
        path="static/uploads/"+str(uuid.uuid4())+photo.filename
        photo.save(path)
        
        q="update coach set fname='%s',lname='%s',place='%s',phone='%s',email='%s',dob='%s',photo='%s' where coach_id='%s'"%(fname,lname,place,phone,email,dob,path,id)
        update(q)
        flash("successFull")
        return redirect(url_for("clubadmin.aprovecoach"))
        
    return render_template('club_approve_coach.html',data=data)






@clubadmin.route('/aprovepsysician',methods=['get','post'])
def aprovepsysician():
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
            return redirect(url_for("clubadmin.aprovepsysician"))
    
    q="select * from psysician  inner join login using(login_id)"
    data['psy']=select(q)
    
    if 'action' in request.args:
        id=request.args['id']
        action=request.args['action']
        
    else:
        action=None

    if action=='approve':
        q="update login set usertype='psysician' where login_id=(select login_id from psysician where psysician_id='%s')"%(id)
        update(q)
        flash("successfull")
        return redirect(url_for('clubadmin.aprovepsysician'))
    
    if action=='reject':
        q="update login set usertype='reject' where login_id=(select login_id from psysician where psysician_id='%s')"%(id)
        update(q)
        flash("successfull")
        return redirect(url_for('clubadmin.aprovepsysician'))
    
    
    
    if action=='update':
        q="select * from coach where coach_id='%s'"%(id)
        res=select(q)
        data['coachup']=res
        
        
    if 'edit' in request.form:
        fname=request.form['fname']
      
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        dob=request.form['dob']
        photo=request.files['photo']
        path="static/uploads/"+str(uuid.uuid4())+photo.filename
        photo.save(path)
        
        q="update psysician set psysician='%s',place='%s',phone='%s',email='%s',dob='%s',photo='%s' where coach_id='%s'"%(fname,place,phone,email,dob,path,id)
        update(q)
        flash("successFull")
        return redirect(url_for("clubadmin.aprovepsysician"))
    
    return render_template('approve_physiotherapist.html',data=data)






@clubadmin.route('/aprovenutretion',methods=['get','post'])
def aprovenutretion():
    data={}
    
    
    if 'btn' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
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
            q="insert into nutretion values (NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,session['clubid'],fname,lname,place,phone,email,path,dob)
            insert(q)
            flash("Registration successfull")
            return redirect(url_for("clubadmin.aprovenutretion"))
    
    
    
    q="select * from nutretion  inner join login using(login_id)"
    data['nutri']=select(q)
    
    if 'action' in request.args:
        id=request.args['id']
        action=request.args['action']
        
    else:
        action=None

    if action=='approve':
        q="update login set usertype='nutretion' where login_id=(select login_id from nutretion where nutretion_id='%s')"%(id)
        update(q)
        flash("successfull")
        return redirect(url_for('clubadmin.aprovenutretion'))
    
    if action=='reject':
        q="update login set usertype='reject' where login_id=(select login_id from nutretion where nutretion_id='%s')"%(id)
        update(q)
        flash("successfull")
        return redirect(url_for('clubadmin.aprovenutretion'))
    
    
    if action=='update':
        q="select * from coach where coach_id='%s'"%(id)
        res=select(q)
        data['coachup']=res
        
        
    if 'edit' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        dob=request.form['dob']
        photo=request.files['photo']
        path="static/uploads/"+str(uuid.uuid4())+photo.filename
        photo.save(path)
        
        q="update coach set fname='%s',lname='%s',place='%s',phone='%s',email='%s',dob='%s',photo='%s' where coach_id='%s'"%(fname,lname,place,phone,email,dob,path,id)
        update(q)
        flash("successFull")
        return redirect(url_for("clubadmin.aprovenutretion"))
    
    return render_template('club_approve_nutri.html',data=data)






@clubadmin.route('/aproveuser')
def aproveuser():
    data={}
    q="select * from user  inner join login using(login_id)"
    data['nutri']=select(q)
    
    if 'action' in request.args:
        id=request.args['id']
        action=request.args['action']
        
    else:
        action=None

    if action=='approve':
        q="update login set usertype='user' where login_id=(select login_id from user where user_id='%s')"%(id)
        update(q)
        flash("successfull")
        return redirect(url_for('clubadmin.aproveuser'))
    if action=='promote':
        q="update login set usertype='player' where login_id=(select login_id from user where user_id='%s')"%(id)
        update(q)
        q="select * from user where user_id='%s'"%(id)
        res=select(q)
        if res:
            fname=res[0]['fname']
            lname=res[0]['lname']
            place=res[0]['place']
            phone=res[0]['phone']
            email=res[0]['email']
            lid=res[0]['login_id']
            q="insert into player values(null,'%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,place,phone,email)
            insert(q)
            flash("successfull")
        return redirect(url_for('clubadmin.aproveuser'))
    
    if action=='reject':
        q="update login set usertype='reject' where login_id=(select login_id from user where user_id='%s')"%(id)
        update(q)
        flash("successfull")
        return redirect(url_for('clubadmin.aproveuser'))
    
    return render_template('club_approve_user.html',data=data)





@clubadmin.route('/newsadd',methods=['get','post'])
def newsadd():
    data={}
    q="select * from news"
    data['news']=select(q)
    
    if 'register' in request.form:
        news=request.form['news']
       
        
        q="insert into news values(null,'%s')"%(news)
        res=insert(q)
       
        flash("News Added Successfull")
        return redirect(url_for('clubadmin.newsadd'))
    
    if 'action' in request.args:
        id=request.args['id']
        action=request.args['action']
        
    else:
        action=None

    if action=='delete':
        q="delete from news where news_id='%s'" %(id)
        delete(q)
        flash("successfull")
        return redirect(url_for('clubadmin.newsadd'))
        
    if action=='update':
        q="select * from news where news_id='%s'"%(id)
        data['newsup']=select(q)   
        
    if 'edit' in request.form:
        news=request.form['news']
        
        
        q="update news set news='%s' where news_id='%s'"%(news,id)
        update(q)
        flash("update Successfull")
        return redirect(url_for('clubadmin.newsadd'))
    return render_template('club_add_news.html',data=data)


@clubadmin.route('/viewbannedplayers')
def viewbannedplayers():
    data={}
    q="select * from banned inner join player using(player_id)"
    data['bplayer']=select(q)
    return render_template('club_view_bannedplayers.html',data=data)


@clubadmin.route('/viewrank')
def viewrank():
    data={}
    q="select * from rank inner join player using(player_id)"
    data['rank']=select(q)
    return render_template('club_view_rank.html',data=data)

@clubadmin.route('/viewselection')
def viewselection():
    data={}
    q="select * from selection_list inner join player using(player_id)"
    data['slection_list']=select(q)
    return render_template('club_view_selection_list.html',data=data)

# try:
#             gmail = smtplib.SMTP('smtp.gmail.com', 587)
#             gmail.ehlo()
#             gmail.starttls()
#             gmail.login('sngistoutpass@gmail.com','izgqjuqneorhokje')
#         except Exception as e:
#             print("Couldn't setup email!!"+str(e))

#         pwd = MIMEText(pwd)

#         pwd['Subject'] = 'Your Letter Transaction Number'

#         pwd['To'] = email

#         pwd['From'] = 'sngistoutpass@gmail.com'

#         try:
#             gmail.send_message(pwd)
   
#             flash("EMAIL SENED SUCCESFULLY")
            


#         except Exception as e:
#             print("COULDN'T SEND EMAIL", str(e))
#         else:
#             flash("INVALID DETAILS")
#         flash('ADDED...')