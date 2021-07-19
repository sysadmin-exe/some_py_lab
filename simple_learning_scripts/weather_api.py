import requests

def get_weather_desc_temp():
  api_key = "ba50656b1ef17af13081c5ccbda501c3"
  city = input('which city do you need weather report for?: ')
  url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

  request = requests.get(url)
  json = request.json()

  description = json.get('weather')[0].get('description')
  temp_min = json.get('main').get('temp_min')
  temp_max = json.get('main').get('temp_max')

  return{'description': description,
         'temp_min': temp_min,
         'temp_max': temp_max
        }
def main():
  weather_dict = get_weather_desc_temp()
  print("the weather for the day is:", weather_dict.get('description'))
  print('the minimum temp for the day is:',  weather_dict.get('temp_min'))
  print('the maximum temp for the day is:',  weather_dict.get('temp_min'))

main()