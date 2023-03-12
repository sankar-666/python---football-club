from flask import *
from database import *

player=Blueprint('player',__name__)

@player.route('/playerhome')
def playerhome():
    return render_template('playerhome.html')


@player.route('/player_view_profile',methods=['get','post'])
def player_view_profile():
    data={}

    data={}
    q="select * from  nutretion where nutretion_id='%s'"%(session['pid'])
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
    else:
        action=None

    
    if action == "update":
        q="select * from  nutretion where nutretion_id='%s'"%(session['pid'])
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            fname=request.form['fname']
            lname=request.form['lname']
            place=request.form['place']
            phone=request.form['phone']
            email=request.form['email']

            q="update nutretion set fname='%s',lname='%s',place='%s', phone='%s', email='%s' where nutretion_id='%s' "%(fname,lname,place,phone,email,session['pid'])
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("player.player_view_profile"))

    return render_template('player_view_profile.html',data=data) 


@player.route('/player_view_news')
def player_view_news():
    data={}
    q="select * from news"
    data['res']=select(q)   
    return render_template('player_view_news.html',data=data)


@player.route('/player_view_videos')
def player_view_videos():
    data={}
    q="select * from video"
    data['res']=select(q)   
    return render_template('player_view_videos.html',data=data)


@player.route('/player_view_yearlyrank')
def player_view_yearlyrank():
    data={}
    q="select * from rank inner join player using (player_id)"
    data['res']=select(q)
    return render_template('player_view_yearlyrank.html',data=data)


@player.route('/player_consultation',methods=['get','post'])
def player_consultation():
    data={}
    q="select * from psysician"
    data['ps']=select(q)
    if 'btn' in request.form:
        reason=request.form['reason']
        pid=request.form['pid']
        q="insert into consultation values (null,'%s','%s','%s','pending')"%(pid,session['loginid'],reason)
        insert(q)
        flash("You will receive your reply soon")
        return redirect(url_for('player.player_consultation'))
    
    q="select * from consultation inner join psysician using (psysician_id) where sender_id='%s'"%(session['loginid'])
    data['res']=select(q)   
    return render_template('player_consultation.html',data=data)


@player.route('/player_complaint',methods=['get','post'])
def player_complaint():
    data={}
    if 'btn' in request.form:
        comp=request.form['comp']
        q="insert into complaint values (null,'%s','pending',curdate(),'%s','player')"%(comp,session['loginid'])
        insert(q)
        flash("Complaint Added!")
        return redirect(url_for('player.player_complaint'))
    
    q="select * from complaint where sender_id='%s'"%(session['loginid'])
    data['res']=select(q)   
    return render_template('player_complaint.html',data=data)