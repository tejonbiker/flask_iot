from flask import Flask, render_template
from flask import request

import datetime
import RPi.GPIO as GPIO
import unicornhat as UH

app = Flask(__name__)

#GPIO.setmode(GPIO.BCM)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('main.html', **templateData)

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route("/writepixel/<pixel>")
def writePixel(pixel):
   #try:
      #GPIO.setup(int(pin), GPIO.IN)
      #if GPIO.input(int(pin)) == True:
      #   response = "Pin number " + pin + " is high!"
      #else:
      #   response = "Pin number " + pin + " is low!"
   #except:
      #response = "There was an error reading pin " + pin + "."

   color = int(pixel)

   for i in range(0,8):
   	UH.set_pixel(0,i,color,color,color)

   UH.show()

   response="All correct"   

   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")

   templateData = {
      'title' : 'Status of Pixel' + str(pixel),
      'time': timeString,
      'response' : response
      }

   return render_template('main.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
