# Python Weather App

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget , QLabel , QLineEdit, QPushButton , QVBoxLayout) 

from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")


        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.get_weather_button.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                           font-family:calibri;
                           }
                           qLabel#city_label{
                           font-size: 40px;
                           font-style: italic;
                           }
                           QLineEdit#city_input{
                           font-size: 40px;
                           }
                           QPushButton#get_weather_button{
                           font-size: 30px;
                           font-weight:bold;
                           }
                           QLabel#temperature_label{
                            font-size: 75px;
                           }
                           QLabel#emoji_label{
                           font-size:100px;
                           font-family: Segoe UI emoji;
                           }
                           QLabel#description_label{
                           font-size: 50px;}
                """)

    def get_weather(self):

        api_key = "d498fc58320ff0935a20ad97ac54674a" #khudka do yaha pe....copy paste karne se kuch nahi hoga...openweathermap.org
        city = self.city_input.text()
        url = f""

        try: 
            response = requests.get(url)
            reponse.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exception.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Bad Requests:\nPlease check your input")
                case 401:
                    self.display_error("Bad Requests:\nPlease check your input")
                case 402:
                    self.display_error("Bad Requests:\nPlease check your input")
                case 403:
                    self.display_error("Bad Requests:\nPlease check your input")
                case 404:
                    self.display_error("Bad Requests:\nPlease check your input")
                case 500:
                    self.display_error("Bad Requests:\nPlease check your input")
                case 502:
                    self.display_error("Bad Requests:\nPlease check your input")
                case 503:
                    self.display_error("Bad Requests:\nPlease check your input")
                case 504:
                    self.display_error("Bad Requests:\nPlease check your input")
                case _:
                    self.display_error(f"HTTP error occured\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self,message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        
    def display_weather(self,data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_f:.0f}F")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        
        if weather_id >= 200 and weather_id<= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif weather_id == 840:
            return "☁️"
        else:
            return ""

   
if __name__== "__main__":
    app =  QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

