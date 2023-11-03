import os
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def sendmail(gmailsmtp: smtplib.SMTP,user: str, password: str):
    reciver = input("podaj odbiorcę\n")
    tytul = input("podaj tytuł maila\n")
    opcja = input("czy chcesz jako wiadomosc zalączyć plik tekstowy z kodem html?y/n\n")
    msg = MIMEMultipart("alternative")
    msg["From"] = user
    msg["To"] = reciver
    msg["Subject"] = tytul
    if opcja == "y":
        wiadomosc = input("podaj lokalizacje pliku w html\n")
        file = open(wiadomosc)
        cz2 = MIMEText(file.read(),"html")
        file.close()
    else:
        wiadomosc = input("podaj wiadomosc\n")
        cz2 = MIMEText(wiadomosc,"plain")
    msg.attach(cz2)
    try:
        gmailsmtp.sendmail(user,reciver,msg.as_string())
        print("wysłano!")
    except:
        print("coś poszło nie tak...")
        os.system('PAUSE')
        exit()
def getmail(gmailimap: imaplib.IMAP4_SSL,  ):
    print(gmailimap.list())
    
option = input("czy chcesz się zalogowac z użyciem pliku?y/n \n")
if option =="n":
    user = input("Podaj email\n")
    password = input("podaj hasło\n")
else:
    localization = input("podaj lokalizacje(lub nazwę jeśli plik jest w tym samym folderze)\n")
    plik = open(localization)
    dane = plik.readlines()
    user = dane[0]
    password = dane[1]
    plik.close()
print("podany użytkownik to " + user + "\n")
try:
    gmailsmtp = smtplib.SMTP_SSL('smtp.gmail.com',465)
    gmailsmtp.ehlo()
    gmailimap = imaplib.IMAP4_SSL('imap.gmail.com',993)
    if gmailsmtp and gmailimap:
        print("połączono!")
except:
    print("coś poszło nie tak ... ")
    os.system('PAUSE')
    exit()
try:
    gmailsmtp.login(user,password)
    gmailimap.login(user,password)
    print("zalogowano")
except:
    print("nie udało się zalogować")
    os.system('PAUSE')
    exit()
while True:
    print("jeśli chcesz wyjść napisz !$exit")
    usin = input("co chcesz zrobić?:\n write or open or download\n")
    if usin.lower() == "write":
        sendmail(gmailsmtp,user,password)
    elif usin.lower() == "!$exit":
        break
    elif usin.lower() == "open":
        getmail(gmailimap)
    os.system('PAUSE')
    os.system('cls')