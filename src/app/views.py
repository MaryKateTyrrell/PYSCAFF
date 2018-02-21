import sysInfo
from app import app
from sysInfo import main
 
@app.route('/')

def display_info():
	return "The platform  is " + main.main()
