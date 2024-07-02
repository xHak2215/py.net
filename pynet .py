import requests
from pyfiglet import Figlet
import folium
import platform
from platform import system
from socket import socket, AF_INET, SOCK_DGRAM
from subprocess import check_output
import os
import scapy.all as sc
from scapy.all import ARP, Ether, srp
import subprocess
import psutil

#pip install requests
#pip install --pre scapy[basic]
#pip install folium
kast =' >>'
version =' 1.0 '
def ippy():
    base_url = "https://demo.ip-api.com/json/"
    ip = input(f"ip {kast}")
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://ip-api.com',
    'Referer': 'https://ip-api.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }
    session = requests.Session()
    response = session.get(f"{base_url}{ip}", headers=headers, params={'fields': 66842623, 'lang': 'en'}) 
    if response.status_code == 200:
        data = response.json()
        print({
            '[IP]': data.get('query'),  # IP адрес
            '[Int prov]': data.get('isp'),  # Интернет провайдер
            '[Org]': data.get('org'),  # Организация
            '[Country]': data.get('country'),  # Страна
            '[Region Name]': data.get('regionName'),  # Регион
            '[City]': data.get('city'),  # Город
            '[ZIP]': data.get('zip'),  # Почтовый код
            '[Lat]': data.get('lat'),  # Широта
            '[Lon]': data.get('lon'),  # Долгота
            })
    else:
        print(f"Ошибка запроса: {response.status_code}")
        
def get_local_ipv4():
    if platform.system() == "Windows":
        local_ip = os.popen("ipconfig | findstr IPv4").read().split(":")[-1].strip()
    else:
        local_ip = os.popen("hostname -I").read().split()[0]
    return local_ip
def get_local_gateway():
    if platform.system() == "Windows":
        gateway = os.popen("ipconfig | findstr Default").read().split(":")[-1].strip()
    else:
        gateway = os.popen("ip route | grep default").read().split()[2]
    return gateway
def scan_local_net():
    local_ip = get_local_ipv4()
    gateway = get_local_gateway()
    print(f'n[+] Local IP: {local_ip}n[+] Local Gateway: {gateway}')
    local_network = local_ip + "/24"
    arp = ARP(pdst=local_network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    print("n[+] Devices on the local network:")
    print("IP" + " "*18+"MAC")
    for device in devices:
        print("{:16}    {}".format(device['ip'], device['mac']))
    input()
    
def ban_ip():
    ip = input(f'ip baning{kast}')
    subprocess.call(['iptables','-A','INPUT','-s',f'"{ip}"','-j','DROP'])
#    import requestsres = requests.get('http://httpbin.org/ip',proxies={ 'http': 'http://user-key:[email protected]:8080','https': 'http://user-key:[email protected]:8080' },headers={'X-BOTPROXY-COUNTRY': 'US'})print(res.text)
def mu_ip():
    r = requests.get('https://api.ipify.org/?format=json')
    mu_ip = r.json()['ip']
    print(f"ваш ip{kast} {mu_ip}")

def inter_info():
    # Получение информации о сетевых интерфейсах
    network_interfaces = psutil.net_if_addrs()
    print("Информация о сетевых интерфейсах:")
    print(network_interfaces)
    # Получение информации о сетевом трафике
    network_traffic = psutil.net_io_counters()
    print("Информация о сетевом трафике:")
    print(network_traffic)

    

preview_text = Figlet(font='standard')
print("\033[32m{}".format(preview_text.renderText('py.net')))
print(version)
print(f"[01]pyip \n[02]scan_local_net\n[03]ban_ip\n[04]mu_ip\n[05]exit")
menu = input(f'pyNet{kast}')
if menu =="1":
    ippy()
elif menu=="2":
    scan_local_net()
elif menu == "3":
    ban_ip()
elif menu =="4":
    mu_ip()
elif menu =="5":
    exit()
elif menu =="6":
    inter_info()

else:
    print('error')



