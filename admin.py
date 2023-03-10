from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@admin.route('/admin_manage_club')
def admin_manage_club():
    data={}
    q="select * from club inner join login using (login_id)"
    data['res']=select(q)

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
    if 'btn' in request.form:
        fixture=request.form['fixture']
       
        q="insert into fixture values (null,'%s')"%(fixture)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_fixture"))

    data={}
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

            q="update fixture set fixture='%s' where fixture_id='%s' "%(fixture,fid)
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
