# Program wydobywa z kodu źródłowego HTML kurs euro - tzw. WEB Scraping

# Polskie znaki
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time

def kurs(nazwa_kurs_euro):
    # Pobierz URL
    link = 'https://www.google.com/search?q='+nazwa_kurs_euro+'+euro' 
    # Utwórz zapytanie to strony
    pobierz_HTML = requests.get(link)    
    # Parser HTML
    dane = BeautifulSoup(pobierz_HTML.text, 'html.parser')
    # Podgląd kodu źródłowego HTML do przeszukania <div class="BNeawe iBp4i AP7Wnd">
    # print (dane.prettify())
    # Znajdź w żródle strony element DIV z informacją o kursie
    text = dane.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    # zwróć wynik
    return text


cena = kurs('euro')
print("Kurs waluty Euro wynosi: ",cena)
