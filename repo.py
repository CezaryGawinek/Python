#https://v6.exchangerate-api.com/v6/563075f9e11695fd9ef35c70/latest/USD
#https://app.exchangerate-api.com/dashboard
#https://api.github.com/users/CezaryGawinek/repos
import requests
#waluta_z
#waluta_na
#kwote
def przelicz(kwota:float, waluta_z:str, waluta_na:str) -> float:
    url = f"https://v6.exchangerate-api.com/v6/7f94714774fff4282592c39f/latest/{waluta_z}"
    response = requests.get(url)
    lista_walut = response.json()['conversion_rates']
    wynik=kwota*lista_walut[waluta_na]
    return wynik
print(przelicz(100,'USD','PLN'))
