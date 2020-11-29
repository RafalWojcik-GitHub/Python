# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

import smtplib

nazwa_uzytkownika = 'adres@email_madawcy'
haslo = 'haslo_do_skrzynki'

nadawca = nazwa_uzytkownika
odbiorca = ['adres@_email_odbiorcy']
temat = 'Test'
tresc = 'Wiadomosc testowa \n\n Ta wiadomosc zostala wygenerowana automatycznie. Prosze na nia nie odpowiadac \n\n'

szablon = """\
From: %s
To: %s
Subject: %s

%s
""" % (nadawca, ", ".join(odbiorca), temat, tresc)

try:
    dane_serwera = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    dane_serwera.ehlo()
    dane_serwera.login(nazwa_uzytkownika, haslo)
    dane_serwera.sendmail(nadawca, odbiorca, szablon)
    dane_serwera.close()

    print ('Wiadomosc wyslana poprawnie')
except:
    print ('Cos sie nie udalo')
