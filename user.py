from flask import *
from database import *
import uuid

user=Blueprint('user',__name__)


@user.route('/userhome')
def userhome():
    
    return render_template('user_home.html')




@user.route('/user_view_profile',methods=['get','post'])
def user_view_profile():
    data={}


    q="select * from  user where user_id='%s'"%(session['uid'])
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
    else:
        action=None

    
    if action == "update":
        q="select * from  user where user_id='%s'"%(session['uid'])
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            fname=request.form['fname']
            lname=request.form['lname']
            place=request.form['place']
            phone=request.form['phone']
            email=request.form['email']
            dob=request.form['dob']
            adhr=request.form['adhar']
            photo=request.files['photo']
            path="static/uploads/"+str(uuid.uuid4())+photo.filename
            photo.save(path)

            q="update user set fname='%s',lname='%s',place='%s', phone='%s', email='%s',aadhar_no='%s',photo='%s',dob='%s' where user_id='%s' "%(fname,lname,place,phone,email,adhr,path,dob,session['uid'])
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("user.user_view_profile"))

    return render_template('user_view_profile.html',data=data) 



@user.route('/user_view_news')
def user_view_news():
    data={}
    q="select * from news"
    data['res']=select(q)   
    return render_template('user_view_news.html',data=data)



@user.route('/user_view_videos')
def user_view_videos():
    data={}
    q="select * from video"
    data['res']=select(q)   
    return render_template('user_view_video.html',data=data)

@user.route('/user_view_fixtures')
def user_view_fixtures():
    data={}
    q="select * from fixture"
    data['res']=select(q)
    data['count']=len(select(q)) 
    return render_template('user_view_fixtures.html',data=data)



@user.route('/user_complaints',methods=['get','post'])
def user_complaints():
    data={}
    if 'btn' in request.form:
        comp=request.form['comp']
        q="insert into complaint values (null,'%s','pending',curdate(),'%s','user')"%(comp,session['loginid'])
        insert(q)
        flash("Complaint Added!")
        return redirect(url_for('user.user_complaints'))
    
    q="select * from complaint where sender_id='%s'"%(session['loginid'])
    data['res']=select(q)   
    return render_template('user_complaints.html',data=data)