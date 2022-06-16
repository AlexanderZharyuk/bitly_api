import argparse
import os
from os.path import exists
from urllib.parse import urlparse

import dotenv
import requests

from exceptions import IncorrectURL


def get_user_info(token: str):
    """Return info in json-format."""
    get_info_url = 'https://api-ssl.bitly.com/v4/user'
    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url=get_info_url, headers=headers)
    response.raise_for_status()
    user_info = response.json()

    return user_info


def create_shorten_link(long_url: str, token: str) -> str:
    """Return short link"""
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    request_data = {
        'long_url': f'{long_url}'
    }

    response = requests.post(url=url, headers=headers, json=request_data)
    response.raise_for_status()
    response_info = response.json()
    shorten_link = response_info['link']

    return shorten_link


def count_clicks(bitlink_id: str, token: str) -> int:
    """Return counts of click by URL"""
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_id}/clicks'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = {
        'unit': 'month',
        'units': '-1'
    }

    response = requests.get(url=url, headers=headers, params=params)
    response.raise_for_status()
    response_info = response.json()
    clicks_counts = response_info['link_clicks'][0]['clicks']

    return clicks_counts


def is_bitlink(link: str, token: str) -> bool:
    """Check URL and return True if it's a bitlink"""
    parse_url = urlparse(link)
    try:
        transformed_link = parse_url.hostname + parse_url.path
    except TypeError:
        raise IncorrectURL(link)

    headers = {
        'Authorization': f'Bearer {token}'
    }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{transformed_link}'
    response = requests.get(url=url, headers=headers)

    return response.ok


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скрипт возвращает сокращенную ссылку на ваш URL, либо если была '
                                                 'указана сокращенная ссылка показывает количество кликов по ней.')
    parser.add_argument('url', help='Ссылка или битлинк')
    args = parser.parse_args()
    url = args.url

    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if not exists(dotenv_path):
        raise FileNotFoundError('Not found .env file')
    bitly_api_token = dotenv.get_key(dotenv_path=dotenv_path, key_to_get='BITLY_TOKEN')

    if is_bitlink(url, token=bitly_api_token):
        bitlink_url = urlparse(url)
        bitlink_id = bitlink_url.hostname + bitlink_url.path
        clicks_count = count_clicks(bitlink_id=bitlink_id, token=bitly_api_token)
        print(f'Количество кликов по ссылке: {clicks_count}')
    else:
        shorten_link = create_shorten_link(long_url=url, token=bitly_api_token)
        print(f'Битлинк: {shorten_link}')
