# Program wydobywa z kodu źródłowego HTML kurs euro - tzw. WEB Scraping

# Polskie znaki
# -*- coding: utf-8 -*-

# Import potrzebnych bibliotek
from bs4 import BeautifulSoup
import requests
import time

# Deklaracja funkcji
def kurs(nazwa_kurs_euro):
    # Do zmiennej link przypisz potrzebny adres URL z zapytaniem Google o kurs euro
    link = 'https://www.google.com/search?q='+nazwa_kurs_euro+'+euro' 
    # Do zmiennej pobierz_HTML przypisz funkcję zapytania do wyszukiwarki Google
    pobierz_HTML = requests.get(link)    
    # Parser zczytuje kod źródłowy HTML z wynikiem zmiennej pobierz_HTML i przypisuje do zmiennej dane
    dane = BeautifulSoup(pobierz_HTML.text, 'html.parser')
    # Opcjonalnie szybki podgląd kodu źródłowego HTML do przeszukania intersujących nasz informacjiz obkiektem <div class="BNeawe iBp4i AP7Wnd"> w którym znajduje się informacja o aktualnym kursie euro
    # print (dane.prettify())
    # Znajdź w żródle strony element DIV z informacją o kursie
    text = dane.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    # zwróć wynik
    return text

# Do zmiennej cena przypisz wynik funkcji kurs()
cena = kurs('euro')
# Wyświetl zawartość zmiennej cena z dodatkowym tekstem
print("Kurs waluty Euro wynosi: ",cena)
