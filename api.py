from flask import * 
from database import *
import uuid


api=Blueprint('api',__name__)




@api.route('/uploadfile',methods=['get','post'])
def uploadfile():
    data={}
    image=request.files['image'];
    lid=request.form['lid'];
    path="static/uploads/"+str(uuid.uuid4())+image.filename
    image.save(path)

  
    fname=request.form['fname']
    lname=request.form['lname']
    place=request.form['place']
    phone=request.form['phone']
    email=request.form['email']
    dob=request.form['dob']
    clubid=request.form['clubid']
    uname=request.form['username']
    passw=request.form['password']
    
    q="select * from login where username='%s'"%(uname)
    print(q)
    res=select(q)
    if res:
        data['status']='duplicate'
        data['method']='reg'
    else:
        q="insert into login values(null,'%s','%s','user')"%(uname,passw)
        print(q)
        id=insert(q)
        q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
        print(q)
        insert(q)
        data['method']='reg'
        data['status']='success'
        

    return str(data)



@api.route('/viewclub')
def viewclub():
    data={}
    q="select * from club"
    res=select(q)
    data['method']='viewclub'
    
    if res:
        data['status']='success'
        data['data']=res
        
    else:
        data['status']='failed'
       
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