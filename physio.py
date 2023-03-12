from flask import *
from database import *

physio=Blueprint('physio',__name__)


@physio.route('/physiohome')
def physiohome():
    
    return render_template('physiohome.html')


@physio.route('/updateprofilepsy',methods=['get','post'])
def updateprofilepsy():
    data={}
    q="select * from psysician where psysician_id='%s'"%(session['clubid'])
    data['res']=select(q)
    
    if 'update' in request.form:
        name=request.form['name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        q="update psysician set psysician='%s',place='%s',phone='%s',email='%s' where psysician_id='%s'"%(name,place,phone,email,session['psyid'])
        print(q)
        update(q)
        flash ('profile Updated')
        return redirect(url_for('physio.updateprofilepsy'))
    return render_template('physio_update_profile.html',data=data)


@physio.route('/viewplayers')
def viewplayers():
    data={}
    q="select * from player where club_id=(select club_id from psysician where psysician_id='%s')"%(session['psyid'])
    data['player']=select(q)
    
    return render_template('psysician_view_players.html',data=data)

@physio.route('/viewcoach')
def viewcoach():
    data={}
        
    q="select * from coach  inner join login using(login_id) where club_id=(select club_id from psysician where psysician_id='%s')"%(session['psyid'])
    data['coach']=select(q)
    
    return render_template('physio_view_coach.html',data=data)



@physio.route('/viewconsluted',methods=['get','post'])
def  viewconsluted():
    data={}    
    q="SELECT `consultation_id`,psysician_id,`consulted`,details,sender_id,CONCAT(player.fname,player.lname) AS nameval FROM `consultation` INNER JOIN psysician USING(psysician_id) INNER JOIN player ON(player.login_id=`consultation`.sender_id) UNION SELECT `consultation_id`,psysician_id,`consulted`,details,sender_id,CONCAT(`nutretion`.fname,`nutretion`.lname) AS NAME FROM `consultation` INNER JOIN psysician USING(psysician_id) INNER JOIN `nutretion` ON(`nutretion`.login_id=`consultation`.sender_id) where psysician_id='%s'"%(session['psyid'])
    res=select(q)
    data['res']=res
    
    
    if 'reply' in request.args:
        reply=request.args['reply']
        data['reply']=4
        
    if 'send' in request.form:
        msg=request.form['msg']
        q="update `consultation` set details='%s' where consultation_id='%s'"%(msg,reply)
        update(q)
        return redirect(url_for('physio.viewconsluted'))
    
    return render_template('physio_view_consulted.html',data=data)


@physio.route('/viewpracticesection')
def viewpracticesection():
    data={}
        
    q="select *,concat(coach.fname,coach.lname) as coach,practice.place as place from practice  inner join coach using(coach_id) inner join club using(club_id) where club_id=(select club_id from psysician where psysician_id='%s')"%(session['psyid'])
    data['practice']=select(q)
    
    return render_template('physio_view_practicesec.html',data=data)



@physio.route('/physiochat',methods=['post','get'])
def physiochat():
    data={}
    uid=session['loginid']
    did=request.args['lid']
    if 'btn' in request.form:
        name=request.form['txt']
    
        q="insert into message values(NULL,'%s','%s','%s',now())"%(uid,did,name)
        insert(q)
        return redirect(url_for("physio.physiochat",lid=did))
    q="SELECT * FROM message WHERE (sender_id='%s' AND receiver_id='%s') OR (sender_id='%s' AND receiver_id=('%s')) order by message_id"%(uid,did,did,uid)
    # q="select * from chats where senderid='%s' and receiverid=( select login_id from doctors where doctor_id='%s' )"%(uid,did)
    print(q)
    res=select(q)
    data['ress']=res
    
    return render_template("physio_chat.html",data=data,uid=uid)


@physio.route('/physio_complaints',methods=['get','post'])
def physio_complaints():
    data={}
    if 'btn' in request.form:
        comp=request.form['comp']
        q="insert into complaint values (null,'%s','pending',curdate(),'%s','physio')"%(comp,session['loginid'])
        insert(q)
        flash("Complaint Added!")
        return redirect(url_for('physio.physio_complaints'))
    
    q="select * from complaint where sender_id='%s'"%(session['loginid'])
    data['res']=select(q)   
    return render_template('physio_complaints.html',data=data)



@physio.route('/physio_view_news')
def physio_view_news():
    data={}
    q="select * from news"
    data['res']=select(q)   
    return render_template('physio_view_news.html',data=data)



@physio.route('/physio_view_rank')
def physio_view_rank():
    data={}
    q="select * from rank inner join player using (player_id)"
    data['res']=select(q)   
    return render_template('physio_view_rank.html',data=data)