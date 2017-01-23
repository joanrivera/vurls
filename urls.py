#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request
from colorama import Fore, Style
import json


urls = {}

data_path = './urls.json'


with open(data_path, 'r') as f:
    read_data = f.read()
    urls = json.loads(read_data)


def validar_url(url):
    """Comprueba si una url está activa

    Args:
        url: La URL que se quiere comprobar

    Returns: true/false según el estado de la URL
    """

    code = -1

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}

    req = urllib.request.Request(url, None, headers)
    try:
        response = urllib.request.urlopen(req) 
        code = response.getcode()
    except urllib.error.HTTPError as e:
        pass

    if code != 200:
        return False

    return True


def obtener_url(url):
    return urllib.urlopen(url).read();


if __name__ == "__main__":
    print('Validando las URL de las depencencias')
    se_encontraron_errores = False
    for key in urls:
        url_cfg = urls[key]
        url = url_cfg['url']
        print(url_cfg['project'], end=' - ')
        if validar_url(url):
            print(Fore.GREEN + 'Ok' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Error: ' + Style.RESET_ALL + url)
    if se_encontraron_errores:
        exit(1)
