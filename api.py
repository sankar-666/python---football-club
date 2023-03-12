from flask import * 
from database import *


api=Blueprint('api',__name__)




@api.route('/userregister')
def userregister():
    
    data={}
 
  
    fname=request.args['fname']
    lname=request.args['lname']
    place=request.args['place']
    phone=request.args['phone']
    email=request.args['email']
    uname=request.args['username']
    passw=request.args['password']
    q="select * from login where username='%s'"%(uname)
    print(q)
    res=select(q)
    if res:
        data['status']='duplicate'
    else:
        q="insert into login values(null,'%s','%s','user')"%(uname,passw)
        print(q)
        id=insert(q)
        q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
        print(q)
        insert(q)
        data['status']='success'
    return str(data)


@api.route('/login')
def login():
    data={}
    username=request.args['username']
    password=request.args['password']

    q="select * from login where username='%s' and password='%s'"%(username,password)
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
        
    return str(data)


@api.route('/player_my_profile')
def player_my_profile():
    data={}
    lid=request.args['lid']
  

    q="select *,concat(fname,'',lname) as name from player where login_id='%s'"%(lid)
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="player_my_profile"

    return str(data)

@api.route('/player_view_news')
def player_view_news():
    data={}

    q="select * from news"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="player_view_news"

    return str(data)


@api.route('/viewvideos')
def viewvideos():
    data={}

    q="select * from video"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="viewvideos"

    return str(data)


@api.route('/player_view_Physicians')
def player_view_Physicians():
    data={} 
    lid=request.args['lid']
    q="select * from psysician where club_id=(select club_id from player where login_id='%s')"%(lid)
    print(q)
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="player_view_Physicians"

    return str(data)

@api.route('/player_view_nutri')
def player_view_nutri():
    data={} 
    lid=request.args['lid']
    q="select *,concat(fname,'',lname) as psysician from nutretion where club_id=(select club_id from player where login_id='%s')"%(lid)
    print(q)
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="player_view_nutri"

    return str(data)


@api.route('/player_view_coach')
def player_view_coach():
    data={} 
    lid=request.args['lid']
    q="select *,concat(fname,'',lname) as psysician from coach where club_id=(select club_id from player where login_id='%s')"%(lid)
    print(q)
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="player_view_coach"

    return str(data)


@api.route('/player_view_practise')
def player_view_practise():
    data={}
    lid=request.args['lid']
  

    q="select *,concat(fname,'',lname) as coach from coach inner join practice using (coach_id)"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="player_view_practise"

    return str(data)



@api.route("/chatdetail")
def chatdetail():
	sid=request.args['sender_id']
	rid=request.args['receiver_id']
	
	data={}
	q="select * from message where (sender_id='%s' and receiver_id='%s') or (sender_id='%s' and receiver_id='%s') group by message_id "%(sid,rid,rid,sid)
	
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		
		data['status']="failed"
	data['method']='chatdetail'
	
	return str(data)

@api.route("/chat")
def chat():
	data={}
	sid=request.args['sender_id']
	rid=request.args['receiver_id']
	det=request.args['details']
	
	
	q="insert into message values(null,'%s','%s','%s',curdate())"%(sid,rid,det)
	insert(q)
	data['status']='success'
	data['method']='chat'
	return str(data)



@api.route('/player_view_fixture')
def player_view_fixture():
    data={}

    q="select * from `fixture` INNER JOIN `match_category` USING (catg_id)"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="player_view_fixture"

    return str(data)


@api.route('/player_view_rank')
def player_view_rank():
    data={}

    q="select *,concat(fname,'',lname) as name from `rank` INNER JOIN `player` USING (player_id)"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="player_view_rank"

    return str(data)


@api.route('/player_apply_noc')
def player_apply_noc():
    data={}
    lid=request.args['lid']
    q="select * from `noc_request` where sender_id='%s' and club_id=(select club_id from player where login_id='%s') "%(lid,lid)
    res=select(q)
    if res:
        data['status']="failed"
    else:
        q="insert into noc_request values (null,'%s',(select club_id from player where login_id='%s'),curdate())"%(lid,lid)
        insert(q)
        print(q)
        data['status']="success"
    data['method']="player_apply_noc"

    return str(data)




@api.route("/player_addcomplaint")
def player_addcomplaint():
    complaint=request.args['complaint']
    lid=request.args['lid']
   
    data={}

    q="insert into complaint values (null,'%s','pending',curdate(),'%s','player')"%(complaint,lid)
    insert(q)
    data['status']="success"
    data['method']="player_addcomplaint"
    return str(data)
  
    
@api.route('/player_viewcomplaint')
def player_viewcomplaint():
    data={}
    lid=request.args['lid']
    z="select * from complaint where sender_id='%s'"%(lid)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="player_viewcomplaint"
    return str(data)

@api.route('/player_view_consulted')
def player_view_consulted():
    data={}
    lid=request.args['lid']
    pid=request.args['pid']
    z="select * from consultation where sender_id='%s' and psysician_id='%s'"%(lid,pid)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']="player_view_consulted"
    return str(data)

@api.route("/player_add_consulted")
def player_add_consulted():
    complaint=request.args['complaint']
    lid=request.args['lid']
    pid=request.args['pid']
   
    data={}

    q="insert into consultation values (null,'%s','%s','%s','pending')"%(pid,lid,complaint)
    insert(q)
    data['status']="success"
    data['method']="player_add_consulted"
    return str(data)