from flask import *
from database import *

enquiry=Blueprint('enquiry',__name__)

@enquiry.route('/enquiryhome')
def enquiryhome():
    return render_template('enquiryhome.html')