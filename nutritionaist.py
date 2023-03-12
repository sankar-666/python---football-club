from flask import *
from database import *

nutritionaist=Blueprint('nutritionaist',__name__)

@nutritionaist.route('/nutritionaisthome')
def nutritionaisthome():
    return render_template('nutritionaisthome.html')


@nutritionaist.route('/nutritionaist_view_profile',methods=['get','post'])
def nutritionaist_view_profile():
    data={}

    data={}
    q="select * from  nutretion where nutretion_id='%s'"%(session['nid'])
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
    else:
        action=None

    
    if action == "update":
        q="select * from  nutretion where nutretion_id='%s'"%(session['nid'])
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            fname=request.form['fname']
            lname=request.form['lname']
            place=request.form['place']
            phone=request.form['phone']
            email=request.form['email']

            q="update nutretion set fname='%s',lname='%s',place='%s', phone='%s', email='%s' where nutretion_id='%s' "%(fname,lname,place,phone,email,session['nid'])
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("nutritionaist.nutritionaist_view_profile"))

    return render_template('nutritionaist_view_profile.html',data=data) 

@nutritionaist.route('/nutritionaist_view_players')
def nutritionaist_view_players():
    data={}
    q="select * from player"
    data['res']=select(q)   
    return render_template('nutritionaist_view_players.html',data=data)

@nutritionaist.route('/nutritionaist_view_users')
def nutritionaist_view_users():
    data={}
    q="select * from user"
    data['res']=select(q)   
    return render_template('nutritionaist_view_users.html',data=data)


@nutritionaist.route('/nutritionaist_view_coach')
def nutritionaist_view_coach():
    data={}
    q="select * from coach"
    data['res']=select(q)   
    return render_template('nutritionaist_view_coach.html',data=data)

@nutritionaist.route('/nutritionaist_view_news')
def nutritionaist_view_news():
    data={}
    q="select * from news"
    data['res']=select(q)   
    return render_template('nutritionaist_view_news.html',data=data)


@nutritionaist.route('/nutritionaist_view_rank')
def nutritionaist_view_rank():
    data={}
    q="select * from rank inner join player using (player_id)"
    data['res']=select(q)   
    return render_template('nutritionaist_view_rank.html',data=data)


@nutritionaist.route('/nutritionaist_complaints',methods=['get','post'])
def nutritionaist_complaints():
    data={}
    if 'btn' in request.form:
        comp=request.form['comp']
        q="insert into complaint values (null,'%s','pending',curdate(),'%s','nutritionaist')"%(comp,session['loginid'])
        insert(q)
        flash("Complaint Added!")
        return redirect(url_for('nutritionaist.nutritionaist_complaints'))
    
    q="select * from complaint where sender_id='%s'"%(session['loginid'])
    data['res']=select(q)   
    return render_template('nutritionaist_complaints.html',data=data)


@nutritionaist.route('/nutritionaist_consultation',methods=['get','post'])
def nutritionaist_consultation():
    data={}
    q="select * from psysician"
    data['ps']=select(q)
    if 'btn' in request.form:
        reason=request.form['reason']
        pid=request.form['pid']
        q="insert into consultation values (null,'%s','%s','%s','pending')"%(pid,session['loginid'],reason)
        insert(q)
        flash("You will receive your reply soon")
        return redirect(url_for('nutritionaist.nutritionaist_consultation'))
    
    q="select * from consultation inner join psysician using (psysician_id) where sender_id='%s'"%(session['loginid'])
    data['res']=select(q)   
    return render_template('nutritionaist_consultation.html',data=data)


@nutritionaist.route('/nutritionaist_chat',methods=['post','get'])
def nutritionaist_chat():
    data={}
    uid=session['loginid']
    did=request.args['did']
    if 'btn' in request.form:
        name=request.form['txt']
    
        q="insert into message values(NULL,'%s','%s','%s',now())"%(uid,did,name)
        insert(q)
        return redirect(url_for("nutritionaist.nutritionaist_chat",did=did))
    q="SELECT * FROM message WHERE (sender_id='%s' AND receiver_id='%s') OR (sender_id='%s' AND receiver_id=('%s')) order by message_id"%(uid,did,did,uid)
    # q="select * from chats where senderid='%s' and receiverid=( select login_id from doctors where doctor_id='%s' )"%(uid,did)
    print(q)
    res=select(q)
    data['ress']=res
    
    return render_template("nutritionaist_chat.html",data=data,uid=uid)
