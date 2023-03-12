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
    q="select * from player"
    data['player']=select(q)
    
    return render_template('psysician_view_players.html',data=data)

@physio.route('/viewcoach')
def viewcoach():
    data={}
        
    q="select * from coach  inner join login using(login_id)"
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