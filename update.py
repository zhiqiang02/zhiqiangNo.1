import requests, os, threading


PROVIDER_DIR = 'C:/Users/Administrator/.config/clash/ruleset'

RULE_PROVIDERS = ('apple', 'applications', 'cncidr', 'direct', 'gfw', 'google', 'greatfire',
                  'icloud', 'lancidr', 'private', 'proxy', 'reject', 'telegramcidr', 'tld-not-cn')
RELEASE_URL = 'https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/'

PROXY = {'https': 'http://zhiqiang:0000@127.0.0.1:7890'}

def curl(file: str, url: str):
    while True:
        try:
            response = requests.get(url, proxies=PROXY)
            response.raise_for_status()
        except:
            continue
        else:
            break
    open(file, 'w').write(response.text)


if __name__ == '__main__':
    os.chdir(PROVIDER_DIR)
    
    for i in RULE_PROVIDERS:
        file = f'{i}.yaml'
        url = f'{RELEASE_URL}{i}.txt'

        new_thread = threading.Thread(target=curl, args=(file, url))
        new_thread.start()
