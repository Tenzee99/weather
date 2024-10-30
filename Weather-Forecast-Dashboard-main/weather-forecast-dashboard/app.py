from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'your_api_key'

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt=7&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
    else:
        weather_data = None
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
