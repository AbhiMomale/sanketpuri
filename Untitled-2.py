import requests

def get_weather_forecast():
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data. Please try again later.")
        return None

def print_weather_for_date(weather_data, date):
    for entry in weather_data['list']:
        if entry['dt_txt'].split(' ')[0] == date:
            print(f"Temperature on {entry['dt_txt']}: {entry['main']['temp']}°C")
            break
    else:
        print("No weather data available for the given date.")

def print_wind_speed_for_date(weather_data, date):
    for entry in weather_data['list']:
        if entry['dt_txt'].split(' ')[0] == date:
            print(f"Wind Speed on {entry['dt_txt']}: {entry['wind']['speed']} m/s")
            break
    else:
        print("No weather data available for the given date.")

def print_pressure_for_date(weather_data, date):
    for entry in weather_data['list']:
        if entry['dt_txt'].split(' ')[0] == date:
            print(f"Pressure on {entry['dt_txt']}: {entry['main']['pressure']} hPa")
            break
    else:
        print("No weather data available for the given date.")

if __name__ == "__main__":
    weather_data = get_weather_forecast()
    
    if weather_data is not None:
        while True:
            print("\nMenu:")
            print("1. Get weather")
            print("2. Get Wind Speed")
            print("3. Get Pressure")
            print("0. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                date = input("Enter the date (YYYY-MM-DD): ")
                print_weather_for_date(weather_data, date)
            elif choice == '2':
                date = input("Enter the date (YYYY-MM-DD): ")
                print_wind_speed_for_date(weather_data, date)
            elif choice == '3':
                date = input("Enter the date (YYYY-MM-DD): ")
                print_pressure_for_date(weather_data, date)
            elif choice == '0':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
