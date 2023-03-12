from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@admin.route('/admin_manage_club',methods=['get','post'])
def admin_manage_club():
    data={}
    q="select * from club inner join login using (login_id)"
    data['res']=select(q)

    if 'register' in request.form:
        club=request.form['club']
        place=request.form['place']
        phone=request.form['phone']
        uname=request.form['uname']
        passw=request.form['passw']
        image=request.files['image']
        path="static/uploads/"+str(uuid.uuid4())+image.filename
        image.save(path)
        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("This Username already exist!, try register with new one.")
        else:
            q="insert into login values(null,'%s','%s','clubadmin')"%(uname,passw)
            res=insert(q)
            q="insert into club values(null,'%s','%s','%s','%s','%s')"%(res,club,place,phone,path)
            insert(q)
            flash('Club added Successfull')
            return redirect(url_for('admin.admin_manage_club'))

    if 'action' in request.args:
        action=request.args['action']
        lid=request.args['lid']

      
    else:
        action=None

    if action == "active":
        q="update login set usertype='clubadmin' where login_id='%s' "%(lid)
        update(q) 
        return redirect(url_for("admin.admin_manage_club"))
    if action == "inactive":
        q="update login set usertype='rejected' where login_id='%s' "%(lid)
        update(q)
        return redirect(url_for("admin.admin_manage_club"))
    
    return render_template('admin_manage_club.html',data=data)


@admin.route('/admin_manage_enquiry')
def admin_manage_enquiry():
    data={}
    q="select * from enquiry inner join login using (login_id)"
    data['res']=select(q)

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
            return redirect(url_for("admin.admin_manage_enquiry"))

    if 'action' in request.args:
        action=request.args['action']
        lid=request.args['lid']

      
    else:
        action=None

    if action == "active":
        q="update login set usertype='enquiryteam' where login_id='%s' "%(lid)
        update(q) 
        return redirect(url_for("admin.admin_manage_enquiry"))
    if action == "inactive":
        q="update login set usertype='rejected' where login_id='%s' "%(lid)
        update(q)
        return redirect(url_for("admin.admin_manage_enquiry"))
    
    return render_template('admin_manage_enquiry.html',data=data)



@admin.route('/admin_manage_news',methods=['get','post'])
def admin_manage_news():
    data={}
    if 'btn' in request.form:
        news=request.form['news']
       
        q="insert into news values (null,'%s')"%(news)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_news"))

    data={}
    q="select * from news"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        nid=request.args['nid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from news where news_id='%s'"%(nid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            news=request.form['news']

            q="update news set news='%s' where news_id='%s' "%(news,nid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_news"))
    if action == "delete":
        q="delete from news where news_id='%s' "%(nid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_news"))
    return render_template('admin_manage_news.html',data=data) 



@admin.route('/admin_manage_fixture',methods=['get','post'])
def admin_manage_fixture():
    data={}
    q="select * from match_category"
    data['val']=select(q)
    if 'btn' in request.form:
        fixture=request.form['fixture']
        date=request.form['date']
        time=request.form['time']
        team1=request.form['team1']
        team2=request.form['team2']
        pid=request.form['pid']
       
        q="insert into fixture values (null,'%s','%s','%s','%s','%s','%s')"%(pid,fixture,date,time,team1,team2)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_fixture"))


    q="select * from fixture"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        fid=request.args['fid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from fixture where fixture_id='%s'"%(fid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            fixture=request.form['fixture']
            date=request.form['date']
            time=request.form['time']
            team1=request.form['team1']
            team2=request.form['team2']

            q="update fixture set fixture='%s',date='%s', time='%s', team1='%s', team2='%s' where fixture_id='%s' "%(fixture,date,time,team1,team2,fid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_fixture"))
    if action == "delete":
        q="delete from fixture where fixture_id='%s' "%(fid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_fixture"))
    return render_template('admin_manage_fixture.html',data=data) 



@admin.route('/admin_manage_video',methods=['get','post'])
def admin_manage_video():
    data={}
    if 'btn' in request.form:
        video=request.files['video']
        path="static/uploads/"+str(uuid.uuid4())+video.filename
        video.save(path)
       
        q="insert into video values (null,'%s')"%(path)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_video"))

    data={}
    q="select * from video"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        vid=request.args['vid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from video where video_id='%s'"%(vid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            if request.files['video']:
                video=request.files['video']
                path="static/uploads/"+str(uuid.uuid4())+video.filename
                video.save(path)

                q="update video set video='%s' where video_id='%s'"%(path,vid)
                update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_video"))
    if action == "delete":
        q="delete from video where video_id='%s' "%(vid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_video"))
    return render_template('admin_manage_video.html',data=data) 



@admin.route('/admin_view_playerhistory')
def admin_view_playerhistory():
    data={}
    q="select * from player"
    data['res']=select(q)   
    return render_template('admin_view_playerhistory.html',data=data)


@admin.route('/admin_view_bannedplayers')
def admin_view_bannedplayers():
    data={}
    q="select * from player inner join banned using (player_id)"
    data['res']=select(q)   
    return render_template('admin_view_bannedplayers.html',data=data)


@admin.route('/admin_view_users')
def admin_view_users():
    data={}
    q="select * from user"
    data['res']=select(q)   
    return render_template('admin_view_users.html',data=data)


@admin.route('/admin_view_coach')
def admin_view_coach():
    data={}
    q="select * from coach"
    data['res']=select(q)   
    return render_template('admin_view_coach.html',data=data)



@admin.route('/admin_manage_matchcategory',methods=['get','post'])
def admin_manage_matchcategory():
    data={}
    if 'btn' in request.form:
        catg=request.form['catg']
       
        q="insert into match_category values (null,'%s')"%(catg)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_matchcategory"))

    data={}
    q="select * from match_category"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid'] 
    else:
        action=None

    
    # if action == "update":
    #     q="select * from video where video_id='%s'"%(vid)
    #     val=select(q)
    #     data['raw']=val

    #     if 'update' in request.form:
    #         if request.files['video']:
    #             video=request.files['video']
    #             path="static/uploads/"+str(uuid.uuid4())+video.filename
    #             video.save(path)

    #             q="update video set video='%s' where video_id='%s'"%(path,vid)
    #             update(q)
    #         flash("Updated Successfully")
    #         return redirect(url_for("admin.admin_manage_matchcategory"))
    if action == "delete":
        q="delete from match_category where catg_id='%s' "%(cid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_matchcategory"))
    return render_template('admin_manage_matchcategory.html',data=data) 

