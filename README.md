# BITLY LINK CREATOR 

Хотите сократить ссылку? Данный скрипт поможет вам сделать это прямо из вашего терминала!

## Предустановка

Все используемые библиотеки указаны в файле **requirements.txt**
Для установки библиотек в виртуальное окружение используйте команды:

```
pip install -r requirements.txt
```

Для работы скрипта вам потребуется создать .env файл, в котором должен находится ваш API-токен:

```
BITLY_TOKEN={YOUR_TOKEN}
```

Для того, чтобы узнать, как получить токен - обратитесь к официальной документации [BITLY](https://dev.bitly.com/).

### Начало работы

Для старта скрипта напишите в консоле, находясь в директории с файлом:
```
python3 main.py [URL]
```
Где вместо URL параметром передайте полную ссылку или битлинк.

Пример выполнения скрипта:
```
python3 main.py https://dvmn.org/

OUTPUT:
Битлинк: https://bit.ly/3MPf9iV
```

## Создано при помощи

* [DEVMAN](https://dvmn.org/) - Обучающая платформа
* [BITLY](https://bitly.com/) - Сервис по созданию коротких ссылок

## Авторы

* [Alexander Zharyuk](https://gist.github.com/AlexanderZharyuk)

