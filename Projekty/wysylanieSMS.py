# Program umożliwia wysyłanie wiadomości SMS za pomocą platformy Twilio z użyciem kodu Python
# https://www.twilio.com/console
# python -m pip install twilio

from twilio.rest import Client

account_sid = "twój sid twilio"
auth_token = "twój token twilio"
client = Client(account_sid, auth_token)
client.messages.create(from_="twój numer zarejestrowany w twilio", body="Wiadomosc testowa od Python", to="+48numer telefonu odbiorcy")


