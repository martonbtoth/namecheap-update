import requests
import configparser 

if __name__ == '__main__':
    print('-----Namecheap updater v0.1----');
    config = configparser.ConfigParser()
    config.read('namecheap.conf')
    host = config['namecheap']['host']
    domain = config['namecheap']['domain']
    passwd = config['namecheap']['password']
    print('Host: ' + host)
    print('Domain: ' + domain)
    r = requests.get('http://wtfismyip.com/text')
    ip = r.text
    print('IP: ' + ip)
    url = 'https://dynamicdns.park-your-domain.com/update?host=%s&domain=%s&password=%s&ip=%s' % (host, domain, passwd, ip)
    print('\nUpdating host record...')
    r = requests.get(url)
    print(r.text)
