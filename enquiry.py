from flask import *
from database import *

enquiry=Blueprint('enquiry',__name__)

@enquiry.route('/enquiryhome')
def enquiryhome():
    return render_template('enquiryhome.html')


@enquiry.route('/enquiry_view_profile',methods=['get','post'])
def enquiry_view_profile():
    data={}

    data={}
    q="select * from  enquiry where enquiry_id='%s'"%(session['eid'])
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
    else:
        action=None

    
    if action == "update":
        q="select * from  enquiry where enquiry_id='%s'"%(session['eid'])
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            enquiry=request.form['enquiry']
            phone=request.form['phone']
            email=request.form['email']

            q="update enquiry set enquiry='%s', phone='%s', email='%s' where enquiry_id='%s' "%(enquiry,phone,email,session['eid'])
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("enquiry.enquiry_view_profile"))

    return render_template('enquiry_view_profile.html',data=data) 



@enquiry.route('/enquiry_yearwise_rank',methods=['get','post'])
def enquiry_yearwise_rank():
    data={}
    q="select * from player"
    data['val']=select(q)
    if 'btn' in request.form:
        pid=request.form['pid']
        rank=request.form['rank']
       
        q="insert into rank values (null,'%s','%s')"%(pid,rank)
      
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("enquiry.enquiry_yearwise_rank"))


    q="select * from rank inner join player using (player_id)"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        rid=request.args['rid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from rank where rank_id='%s'"%(rid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            rank=request.form['rank']

            q="update rank set rank='%s' where rank_id='%s' "%(rank,rid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("enquiry.enquiry_yearwise_rank"))
    if action == "delete":
        q="delete from rank where rank_id='%s' "%(rid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("enquiry.enquiry_yearwise_rank"))
    return render_template('enquiry_yearwise_rank.html',data=data) 



@enquiry.route('/enquiry_ban_player',methods=['get','post'])
def enquiry_ban_player():
    data={}
    q="select * from player"
    data['val']=select(q)
    if 'btn' in request.form:
        pid=request.form['pid']
        reason=request.form['reason']
       
        q="insert into banned values (null,'%s','%s')"%(pid,reason)
      
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("enquiry.enquiry_ban_player"))


    q="select * from banned inner join player using (player_id)"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        rid=request.args['rid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from banned where ban_id='%s'"%(rid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            reason=request.form['reason']

            q="update banned set reason='%s' where ban_id='%s' "%(reason,rid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("enquiry.enquiry_ban_player"))
    if action == "delete":
        q="delete from banned where ban_id='%s' "%(rid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("enquiry.enquiry_ban_player"))
    return render_template('enquiry_ban_player.html',data=data) 


@enquiry.route('/enquiry_view_complaints')
def enquiry_view_complaints():
    data={}
    q="""
    SELECT `psysician` AS NAME,sended_by AS fromname,complaint,DATE,reply FROM `complaint` INNER JOIN `psysician` ON `complaint`.`sender_id`=`psysician`.login_id
    UNION
    SELECT CONCAT(fname,'',lname) AS NAME,sended_by AS fromname,complaint,DATE,reply FROM `complaint` INNER JOIN `nutretion` ON `complaint`.`sender_id`=`nutretion`.login_id
    UNION
    SELECT CONCAT(fname,'',lname) AS NAME,sended_by AS fromname,complaint,DATE,reply FROM `complaint` INNER JOIN `user` ON `complaint`.`sender_id`=`user`.login_id
    UNION
    SELECT CONCAT(fname,'',lname) AS NAME,sended_by AS fromname,complaint,DATE,reply FROM `complaint` INNER JOIN `player` ON `complaint`.`sender_id`=`player`.login_id
    UNION
    SELECT CONCAT(fname,'',lname) AS NAME,sended_by AS fromname,complaint,DATE,reply FROM `complaint` INNER JOIN `coach` ON `complaint`.`sender_id`=`coach`.login_id
    """
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
    else:
        action=None
    
    if action == "reply":
        data['showrep']=True
    
    if 'btn' in request.form:
        reply=request.form['reply']
        q="update complaint set reply='%s' where complaint_id='%s'"%(reply,cid)
        update(q)
        flash("reply Updated")
        return redirect(url_for('enwuiry.enquiry_view_complaints'))
    return render_template('enquiry_view_complaints.html',data=data)

@enquiry.route('/enquiry_view_playerhistory')
def enquiry_view_playerhistory():
    data={}
    q="select * from player"
    data['res']=select(q)   
    return render_template('enquiry_view_playerhistory.html',data=data)

@enquiry.route('/enquiry_view_club')
def enquiry_view_club():
    data={}
    q="select * from club"
    data['res']=select(q)   
    return render_template('enquiry_view_club.html',data=data)

@enquiry.route('/enquiry_view_users')
def enquiry_view_users():
    data={}
    q="select * from user"
    data['res']=select(q)   
    return render_template('enquiry_view_users.html',data=data)

@enquiry.route('/enquiry_view_physiotherapist')
def enquiry_view_physiotherapist():
    data={}
    q="select * from psysician"
    data['res']=select(q)   
    return render_template('enquiry_view_physiotherapist.html',data=data)

@enquiry.route('/enquiry_view_nutritionalist')
def enquiry_view_nutritionalist():
    data={}
    q="select * from nutretion"
    data['res']=select(q)   
    return render_template('enquiry_view_nutritionalist.html',data=data)


@enquiry.route('/enquiry_view_coach')
def enquiry_view_coach():
    data={}
    q="select * from coach"
    data['res']=select(q)   
    return render_template('enquiry_view_coach.html',data=data)


@enquiry.route('/enquiry_view_news')
def enquiry_view_news():
    data={}
    q="select * from news"
    data['res']=select(q)   
    return render_template('enquiry_view_news.html',data=data)

