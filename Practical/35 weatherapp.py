import tkinter as tk 
import random

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Weather App')

        self.city_label = tk.Label(root, text="enter city:")
        self.city_label.grid(row=0, column=0, padx=10, pady=10)

        self.entry_city = tk.Entry(root)
        self.entry_city.grid(row=0, column=1, padx=10, pady=10)

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.grid(row=1, column=1, padx=10, pady=10)

        self.weather_info_label = tk.Label(root, text="")
        self.weather_info_label.grid(row=2, column=1, padx=10, pady=10)

    def get_weather(self):
        city = self.entry_city.get()
        weather_info = self.simulate_weather()

        self.weather_info_label.config(text=f"weather in {city}, {weather_info}")

    def simulate_weather(self):
        tempreture = random.randint(-5, 40)
        condition = random.choice(['sunny', 'cloudy', 'rainy', 'windy'])
        return f'{tempreture}, {condition}'


root = tk.Tk()
app = WeatherApp(root)
root.mainloop()