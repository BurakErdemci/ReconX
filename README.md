# ReconX 🔍

**ReconX**, Kali Linux üzerinde Python ile geliştirilmiş, hedef bir domain hakkında bilgi toplayan basit ve etkili bir bilgi toplama (reconnaissance) aracıdır.

## Özellikler

- 🌐 Domain IP adresini öğrenme  
- 🧾 WHOIS kayıtlarını çekme  
- 🔎 Subdomain brute force ile alt alan adlarını bulma  
- 📛 DNS kayıtlarını listeleme (TXT, A, NS vb.)  
- 🌍 IP lokasyon bilgisi (ülke, şehir, ISP)  
- 🚪 Basit port tarama (nmap ile)

## Kurulum

Gerekli paketleri yüklemek için:

linux terminalde:

sudo apt update

sudo apt install python3 whois nmap -y

pip3 install -r requirements.txt

Alternatif olarak sanal ortam:

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt(Önerilen Kurulum)


Kullanım:

Linux Terminale

python3 recontool.py yazınız

Komut çalıştırıldığında sizden hedef domain istenecektir. Örnek çıktı: Hedef domain: example.com

Kodu çalıştırdıktan sonra örnek çıktı: [+] IP Adresi: 93.184.216.34

[+] WHOIS bilgileri: ...
[+] Subdomain brute force: ...
[+] DNS Kayıtları: ...
[+] IP Konum Bilgisi: ...
[+] Port Tarama: ...

!!! Bu araç sadece eğitim ve etik siber güvenlik çalışmaları için tasarlanmıştır.
    Yalnızca izinli testlerde kullanınız. İzinsiz testler yasal değildir ve etik dışıdır.

    Geliştirici:Burak Erdemci
