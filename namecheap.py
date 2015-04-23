import requests
import configparser 
from subprocess import Popen, PIPE

def checkip (ip):
    try:
        f = open('/tmp/previp.txt', 'r')
        previp = f.readline()
        f.close()
        if previp == ip:
            return True
        return False
    except FileNotFoundError:
        return False

def writeip (ip):
    f = open ('/tmp/previp.txt', 'w')
    f.write(ip)
    f.close

if __name__ == '__main__':
    print('-----Namecheap updater v0.1----');
    config = configparser.ConfigParser()
    config.read('namecheap.conf')
    host = config['namecheap']['host']
    domain = config['namecheap']['domain']
    passwd = config['namecheap']['password']
    print('Host: ' + host)
    print('Domain: ' + domain)
    p = Popen([config['namecheap']['getip_command']], shell=True, stdout=PIPE, stderr=PIPE)
    ip, err = p.communicate()
    ip = ip.decode("utf-8")
    err = err.decode("utf-8")
    print('IP: ' + ip)
    print('Err: ' + err)
    if checkip(ip) == False:
        writeip(ip)
        url = 'https://dynamicdns.park-your-domain.com/update?host=%s&domain=%s&password=%s&ip=%s' % (host, domain, passwd, ip)
        print('\nUpdating host record...')
        r = requests.get(url)
        print(r.text)
    else:
        print('IP matches previous address, skipping update.')
