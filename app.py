from flask import Flask, render_template, redirect
import RPi.GPIO as GPIO
import time

def trigger_relay():
	relay_pin = 4
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(relay_pin, GPIO.OUT)
	time.sleep(.5)
	GPIO.cleanup()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trigger_relay/', methods=['POST'])
def trigger_relay_flask():
    trigger_relay()
    return redirect("/", code=302)
    
if __name__ == "__main__":
        app.run(host='0.0.0.0',port=5050,debug=True)