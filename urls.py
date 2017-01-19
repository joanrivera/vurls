#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request
from colorama import Fore, Style


urls = [
    {
        'project': 'CommaCD',
        'url': 'https://github.com/shyiko/commacd.git',
    },
    {
        'project': 'Composer',
        'url': 'https://raw.githubusercontent.com/composer/getcomposer.org/master/web/installer',
    },
    {
        'project': 'DBeaver',
        'url': 'http://dbeaver.jkiss.org/files/dbeaver-ce_latest_amd64.deb',
    },
    {
        'project': 'Firefox Developer',
        'url': 'https://download-installer.cdn.mozilla.net/pub/firefox/nightly/latest-mozilla-aurora/firefox-52.0a2.en-US.linux-x86_64.tar.bz2',
    },
    {
        'project': 'HHighlighter',
        'url': 'https://github.com/paoloantinori/hhighlighter.git',
    },
    {
        'project': 'Insomnia',
        'url': 'https://builds.insomnia.rest/downloads/ubuntu/latest',
    },
    {
        'project': 'Liquid Prompt',
        'url': 'https://github.com/nojhan/liquidprompt.git',
    },
    {
        'project': 'NodeJS',
        'url': 'https://nodejs.org/dist/v6.9.4/node-v6.9.4-linux-x64.tar.xz',
    },
    {
        'project': 'ShellCheck',
        'url': 'http://launchpadlibrarian.net/183003718/shellcheck_0.3.3-1~ubuntu14.04.1_amd64.deb',
    },
    {
        'project': 'Visual Studio Code',
        'url': 'https://go.microsoft.com/fwlink/?LinkID=760868',
    },
]


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
    for url_cfg in urls:
        url = url_cfg['url']
        print(url_cfg['project'], end=' - ')
        if validar_url(url):
            print(Fore.GREEN + 'Ok' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Error: ' + Style.RESET_ALL + url)
    if se_encontraron_errores:
        exit(1)
