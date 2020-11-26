# Program wydobywa z kodu źródłowego HTML kurs euro, tzw. WEB Scraping - autor Rafał W

# Poprawne wyświetlanie polskich znaków dla napisu ,,Złoty"
# -*- coding: utf-8 -*-

# Import potrzebnych bibliotek dla użytych funkcji w programie
from bs4 import BeautifulSoup # dla funkcji BeautifulSoup()
import requests # dla funkcji requests.get()    
import time # dla funkcji time.sleep()

# Deklaracja głownej funkcji kurs() parsującej i przetwarzającej kod źródłowy HTML w poszukiwaniu kursu euro
def kurs(nazwa_kurs_euro):
    # Przypisz URL z zapytanie Google o kurs euro do zmiennej
    link = 'https://www.google.com/search?q='+nazwa_kurs_euro+'+euro' 
    # Utwórz zapytanie to strony
    pobierz_HTML = requests.get(link)    
    # Parser przetwarzający kod HTML
    dane = BeautifulSoup(pobierz_HTML.text, 'html.parser')
    # Podgląd kodu źródłowego HTML do przeszukania <div class="BNeawe iBp4i AP7Wnd">
    # print (dane.prettify())
    # Znajdź w żródle strony element DIV z informacją o kursie
    text = dane.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    # zwróć wynik
    return text


cena = kurs('euro')
print("Kurs waluty Euro wynosi: ",cena)

# Opcjonalna deklaracja funkcji z zapętloną instrukcją while sprawdzającą kurs euro w czasie rzeczywistym 
def sprawdzaj():
    #zmienna potrzebna do instrukcji warunkowej if
    ostatnia_cena = -1
    # Zapętlenie działania programu
    while True:
        zmienna1 = 'euro'
        cena = kurs(zmienna1)
        # Warunek logiczny w instrukcji warunkowej if, jeśli cena euro nie jest równa -1 wtedy wyświetl komunikat ( warunek nigdy nie będzie spełniony)
        if cena != ostatnia_cena:
            print (zmienna1+' cena: ', cena )
            ostatnia_cena = cena
        # Funkcja wstrzymania działania programu na 3 sekundy
        time.sleep(3)

# Wywołanie wcześniej zadeklarowanej funkcji  
sprawdzaj()
