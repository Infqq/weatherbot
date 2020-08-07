from vkbottle import *
import pyowm


bot=Bot('токен группы вк')
owm=pyowm.OWM('токен pyowm', language = 'ru')


@bot.on.message(text='<name>')
async def wrapper(ans: Message, name):
  try:
    observation = owm.weather_at_place(name)
    w = observation.get_weather()
    temp=w.get_temperature('celsius')['temp']

    await ans("В городе " + name + " сейчас " + w.get_detailed_status() + "\n")
    await ans("Температура в районе " + str(round(temp)) + " градусов")
    
    if temp<10:
      await ans("Холодно, лучше надеть куртку.")
    elif temp<17:
      await ans("Прохладно, надень толстовку.")
    else:
      await ans("На улице тепло, можешь надеть майку и шорты")

  except pyowm.exceptions.api_response_error.NotFoundError:
      await ans("Город не найден")

bot.run_polling(skip_updates=False)
