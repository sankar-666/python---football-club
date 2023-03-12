from flask import Flask,render_template
from public import public
from admin import admin
from clubadmin import clubadmin
from player import player
from physio import physio
from enquiry import enquiry
from api import api

from nutritionaist import nutritionaist

app=Flask(__name__)

app.secret_key="prayulla"

app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(clubadmin,url_prefix="/clubadmin")
app.register_blueprint(player,url_prefix="/player")
app.register_blueprint(physio,url_prefix="/physio")
app.register_blueprint(enquiry,url_prefix="/enquiry")
app.register_blueprint(api,url_prefix="/api")
app.register_blueprint(nutritionaist,url_prefix="/nutritionaist")
app.register_blueprint(public)

@app.errorhandler(404) 
def not_found(e):
  return render_template("404.html")

app.run(debug=True,port=5008,host="0.0.0.0")