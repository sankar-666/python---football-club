from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')


@public.route('/login',methods=['post','get'])
def login():

    if 'btn' in request.form:
        uname=request.form['uname']
        pasw =request.form['pasw']

        q="select * from login where username='%s' and password='%s'"%(uname,pasw)
        res=select(q)


        if res:
            session['loginid']=res[0]["login_id"]
            utype=res[0]["usertype"]
            if utype == "admin":
                flash("Login Success")
                return redirect(url_for("admin.adminhome"))
            elif utype == "player":
                q="select * from player where login_id='%s'"%(session['loginid'])
                val=select(q)
                if val:
                    session['pid']=val[0]['player_id']
                    flash("Login Success")
                    return redirect(url_for("player.playerhome"))
            elif utype == "team":
                q="select * from team where login_id='%s'"%(session['loginid'])
                val1=select(q)
                if val1:
                    session['tid']=val1[0]['team_id']
                    flash("Login Success")
                    return redirect(url_for("team.teamhome"))
               
            
            else:
                flash("failed try again")
                return redirect(url_for("public.login"))
        else:
            flash("Invalid Username or Password!")
            return redirect(url_for("public.login"))


    return render_template("login.html")
