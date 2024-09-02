def convertCentigradeToF(Centigrade):
    F = (Centigrade * 9/5) + 32
    print (F)

def convertFaraniteToC(faranite):
    C = (faranite - 32) * 5/9
    print (C)   

s = input("Please enter the following- 1 for converting Centigrade to Farenheit and 2 for converting Farenheit to Centigrade ")
v=int(s)

s = input("Please enter the temperature ")
value=int(s)

if v==1:
    convertCentigradeToF(value)
elif v==2:
   convertFaraniteToC(value)
    


