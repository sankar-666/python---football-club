from flask import *
from database import *

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
        uname=request.form['uname']
        passw=request.form['passw']
        
        q="insert into login values(null,'%s','%s','player')"%(uname,passw)
        res=insert(q)
        q="insert into player values(null,'%s','%s','%s','%s','%s','%s')"%(res,fname,lname,place,phone,email)
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
        
        q="update player set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where player_id='%s'"%(fname,lname,place,phone,email,id)
        update(q)
        flash("update Successfull")
        return redirect(url_for('clubadmin.playeradd'))
    return render_template('club_add_players.html',data=data)


@clubadmin.route('/aprovecoach')
def aprovecoach():
    data={}
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
    
    return render_template('club_approve_coach.html',data=data)

@clubadmin.route('/aprovepsysician')
def aprovepsysician():
    data={}
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
    
    return render_template('approve_physiotherapist.html',data=data)

@clubadmin.route('/aprovenutretion')
def aprovenutretion():
    data={}
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
    return render_template('club_view_rank.html',data=data)