import requests
from pyfiglet import Figlet
import platform
from socket import socket, AF_INET, SOCK_DGRAM
from subprocess import check_output
import scapy.all as sc
from scapy.all import ARP, Ether, srp
import socket
import os
import time

#pip install requests
#pip install --pre scapy[basic]
kast =' >>'
version = '1.2.0'

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
    
def ban_ip():
    pass
    print("ops разрабочик ленивый :(")
        
def ulr_to_ip(ulrtoip):   
    try:
        # Using gethostbyname() function of socket module for IP address
        ip_address = socket.gethostbyname(ulrtoip)
        # Returning IP address from the function
        return ip_address
        # if error occurs, returns the error
    except:
        print("Error")
def mu_ip():
    r = requests.get('https://api.ipify.org/?format=json')
    mu_ip = r.json()['ip']
    print(f"ваш ip{kast} {mu_ip}")
    return mu_ip

def ping(ping_url)->int:
    start_time = time.time()
    try:
        k=requests.get(ping_url)
        s=k.status_code
        if s== 200:
            pass
        else:
            return "not"
    except requests.exceptions.InvalidURL:
        return f"Invalid url {kast}{ping_url}"
    response=time.time() - start_time
#    print('ping',response)
    return response


    
    
def menu():
    preview_text = Figlet(font='standard')
    print("\033[32m{}".format(preview_text.renderText('py.net')))
    print(f"[01]pyip\n[02]scan_local_net\n[03]ban_ip\n[04]ulr_to_ip\n[05] ping \n")
    while True: 
        menu = input(f'pyNet{kast}')
        if menu =="1" or menu =="01":
            ippy()
        elif menu=="2" or menu=="02":
            scan_local_net()
        elif menu == "3" or menu == "03":
            ban_ip()
        elif menu =="4" or menu =="04":
            ulrtoip = input(f"ulr{kast}")
            ip = ulr_to_ip(ulrtoip)
            print(f"The IP address of {ulrtoip} is {ip}")
        elif menu =="5"or menu =="05":
            print(ping(input(f'ping in domen {kast}')))
#        elif menu =="6"or menu=="06":


        else:
            print('error')
menu()


