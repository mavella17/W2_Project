import requests
import pprint
import pandas as pd
import sqlalchemy as db
from sqlalchemy import delete
from sqlalchemy.sql import text as sa_text



engine = db.create_engine('sqlite:///currency.db')


def updateDB():
    listofCurr = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json'
    currList = requests.get(listofCurr)
    currList = currList.json().keys()
    url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/"
    first = True
    for currency in currList:
        r = requests.get(url + currency + ".json")
        rates = r.json()[currency]
        firstColumn = {'Currency':currency, 'Date Updated':r.json()['date']}
        firstColumn.update(rates)
        d = pd.DataFrame(firstColumn, index=[0])
        if first:
            d.to_sql('exchange', con=engine, if_exists='replace', index=False)
            first = False
        else:
            d.to_sql('exchange', con=engine, if_exists='append', index=False)


def printDB():
    with engine.connect() as connection:
        query_result = connection.execute(db.text("""SELECT * FROM
        exchange;""")).fetchall()
        print(pd.DataFrame(query_result))

def getList():
    listofCurr = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json'
    currList = requests.get(listofCurr)
    pprint.pprint(currList.json())

def base():




def main():
    while True:
        print("---------")
        print("Commands:")
        print("---------")
        print("Input B to input a base currency")
        print("Input U to update the exchange rate database")
        print("Inpuy V to view the exchange rate database")
        print("Input Q to quit")
        print("Input L to list all currencies and their acronyms")

        base = input("Type command here: ")
        base = base.upper()
        if base == "L":
            getList()
        elif base == "Q":
            print("Quitting!")
            break
        elif base == "U":
            updateDB()
            printDB()
        elif base == "V":
            printDB()
        elif base =="B":
            print("TEsting")
        else:
            print("Invalid Command, Try Again!")
        
        

if __name__ == "__main__":
    main()