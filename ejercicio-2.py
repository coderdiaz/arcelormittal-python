"""
El programa solicitará al usuario el monto a convertir y la divisa:
Hint: input()

Crea una función `exchange_money()` que reciba dos parámetros:
  1. `budget`: El monto de dinero que se planea cambiar.
  2. `exchange_rate`: La cantidad de moneda igual a una
      unidad de moneda extranjera.

Hint: exchange_money(4000, 20.37) -> 196.3672066765 USD
  
Nota: Tomando como ejemplo que tu moneda sea el peso Mexicano
y buscas convertilo a otra divisa

20.37 MXN = 1 USD
21.45 MXN = 1 EUR
25.81 MXN = 1 GBP

El programa deberá poder convertise a las diferentes divisas, y en caso, de que la divisa
no este disponible deberá mostrar un mensaje indicando que no existe.
"""

EXCHANGE_RATE_USD = 20.37
EXCHANGE_RATE_EUR = 21.45
EXCHANGE_RATE_GBP = 25.81

def exchange_rate(budget, exchange_rate):
  return budget / exchange_rate

budget = float(input("¿Cuánto deseas convertir (MXN)?: "))
currency = input("Selecciona la divisa (USD, EUR, GBP): ")

match currency:
  case "USD":
    amount = exchange_rate(budget, EXCHANGE_RATE_USD)
    print(amount)
  case "EUR":
    amount = exchange_rate(budget, EXCHANGE_RATE_EUR)
    print(amount)
  case "GBP":
    amount = exchange_rate(budget, EXCHANGE_RATE_GBP)
    print(amount)
  case _:
    print("No existe esta divisa")