import requests
from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
import config

TOKEN = config.TOKEN
OPENWEATHERTOKEN = config.OPENWEATHERTOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_function(message: types.Message):
      await message.reply("Add city name: ")



@dp.message_handler()
async def echo(message: types.Message):
    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OPENWEATHERTOKEN}&units=metric&lang=ru')
        data = response.json()

        with open('weather.txt', 'w') as f:
            f.write(str(data))

            city = data["name"]
            des = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            country = data["sys"]["country"]
            sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M')
            sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M')

            await message.reply(
                f"City: {city}\n"
                f"Country: {country}\n"
                f"Current temp: {temp}°C\n"
                f"Weather: {des}\n"
                f"Humidity: {humidity}\n"
                f"Wind speed: {wind} m\s\n"
                f"Sunrise: {sunrise}\n"
                f"Sunset: {sunset}\n"
                )
    except Exception as ex:
        await message.reply("Add Correct City name")
        

if __name__ == '__main__':
       executor.start_polling(dp)