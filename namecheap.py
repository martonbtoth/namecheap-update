import requests

if __name__ == '__main__':
    print('Namecheap updater v0.1');
    r = requests.get('http://wtfismyip.com/text')
    print(r.text)
