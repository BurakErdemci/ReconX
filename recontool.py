import socket
import requests
import subprocess
import os

# Subdomain brute force için kullanılacak liste
subdomains = ['www', 'mail', 'ftp', 'test', 'dev']

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP Adresi: {ip}")
        return ip
    except:
        print("[-] IP alınamadı.")
        return None

def whois_lookup(domain):
    print("\n[+] WHOIS bilgileri:")
    os.system(f"whois {domain}")

def subdomain_bruteforce(domain):
    print("\n[+] Subdomain brute force:")
    for sub in subdomains:
        full = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full)
            print(f" - {full} --> {ip}")
        except:
            continue

def dns_lookup(domain):
    print("\n[+] DNS Kayıtları:")
    os.system(f"dig {domain} any +short")

def nmap_scan(ip):
    print("\n[+] Port Tarama (nmap):")
    os.system(f"nmap -F {ip}")

def geoip_lookup(ip):
    print("\n[+] IP Konum Bilgisi:")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        print(f" - Ülke: {data['country']}, Şehir: {data['city']}, ISP: {data['isp']}")
    except:
        print("[-] IP konumu alınamadı.")

if __name__ == "__main__":
    domain = input("Hedef domain: ").strip()
    ip = get_ip(domain)
    whois_lookup(domain)
    subdomain_bruteforce(domain)
    dns_lookup(domain)
    if ip:
        geoip_lookup(ip)
        nmap_scan(ip)