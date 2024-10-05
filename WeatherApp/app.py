from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Função para buscar os dados meteorológicos
def get_weather_data(city, api_key):
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'ef6389795e6cda50eda936a05c55bd84'
        weather_data = get_weather_data(city, api_key)

    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
