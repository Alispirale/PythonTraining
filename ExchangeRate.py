import pandas as pd
df = pd.read_excel(r'Foreign_Exchange_Rates.xlsx')

dict_rate = pd.Series(df.Rate.values,index=df.Country).to_dict()

def convert(amount,currency):
    return float(amount)/float(dict_rate[currency])

x = input("Amount to convert ")
y = input("Currency to convert from ")

while y not in dict_rate :
    y=input("Choose a valid currency ")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while not is_number(x):
    x = input("Please enter a valid number ")

result=round(convert(float(x),y),2)
print(f"{x} {y} is {result} USD")