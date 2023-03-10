from flask import *
from database import *

nutritionaist=Blueprint('nutritionaist',__name__)

@nutritionaist.route('/nutritionaisthome')
def nutritionaisthome():
    return render_template('nutritionaisthome.html')