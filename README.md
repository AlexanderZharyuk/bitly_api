# BITLY LINK CREATOR

Want to shorten a link? This script will help you do it right from your terminal!

## Get started

All libraries that used in project are listed in the **requirements.txt** file
To install libraries in your virtual environment, use the command:

```
pip install -r requirements.txt
```

For the script to work, you will need to create an `.env` file, which should contain your API token:

```
BITLY_TOKEN={YOUR_TOKEN}
```

To learn how to get a token, please refer to the official documentation [BITLY](https://dev.bitly.com/).

## How to use

Go to the project folder in your console and write:
```
python3 main.py [url]
```
Where, instead of the URL parameter, pass the full link or bitlink, if you want to check count of clicks of your bitlink.

Example of script execution:
```
python3 main.py https://dvmn.org/

OUTPUT:
Bitlink: https://bit.ly/3MPf9iV
```

## Created with

* [BITLY](https://bitly.com/) - Service for creating short links

## The author

* [Alexander Zharyuk](https://gist.github.com/AlexanderZharyuk)
