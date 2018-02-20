from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
	zipcode = request.form['zip']
	#r = requests.get('http://samples.openweathermap.org/data/2.5/weather?zip='+zipcode+',phl&appid=b6907d289e10d714a6e88b30761fae22')
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',ph&appid=71cc6accb64d04cda13d4cb2906f7233')
	json_object = r.json()
	temp_kelvin = float(json_object['main']['temp'])
	temp_fahrenheit = (temp_kelvin - 273.15) * 1.8 + 32
	return render_template('temperature.html', temp=temp_fahrenheit)

@app.route('/')
def index():
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True)