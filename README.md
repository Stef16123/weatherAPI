# weatherAPI
API для статистики по погоде с использованием внешнего api. 

При запуске сервера, так же запускается шедулер, который раз в час получает данные о текущей погоде в Москве со стороннего сервера ([AccuWeather](https://www.accuweather.com/)) и сохраняет в БД. 


## Стэк:
- FastApi
- mongodb (motor)
- docker


## Api:


`/weather/current` - Текущая температура (Запрос к AccuWeather)

`/weather/historical` - Почасовая температура за последние 24 часа 

`/weather/historical/max` - Максимальная температура за 24 часа

`/weather/historical/min` - Минимальная температура за 24 часа
