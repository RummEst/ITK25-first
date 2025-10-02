import math, datetime, random, time

# 1 line comment
""""multi
line
comment"""


### Kasutaja

age = 20
h = 1.8
name =  "Bob Marley"

print(name, age, h) # sep="\n"
print(f"\nUSER: {name.title()}, AGE: {age}, HEIGHT: {h}m")
print(f"Kasutaja {name.title()} vanuses {age} on {h}m pikk")
### Matemaatika


byear = datetime.datetime.now().year - age
print(f"birth year: {byear}")


#vanuse kjontroll Alaealine 1-17, töö 18-63, pens 64-99
if age > 1 or age < 122:
    if age < 18:
        print("Kasutaja on alaealine")
    elif age > 64:
        print("Kasutaja on pensionär")
    else:
        print("kasutaja on tööealine")
else:
    raise ValueError("age must be between 1 and 122")

# küsime elukohta ja vastatvalt elukoha pikkusele väljastame
# väike koht (2-7)
# suur koht (<7)
ekoht = input("Siseta elukoht:").strip()

if 1 < len(ekoht) <= 7 and ekoht.isalpha():
    print("Väike koht")
elif len(ekoht) > 7:
    print("Suur koht")
else:
    print("Elukoht sisaldab numbreid!")

# Substring (alamstring)
# name = "Bob Marley"
print(name[1])      # o
print(name[0:3])    # Bob
print(name[6:])     # rley
print(name[:3])     # Bob
print(name[::-1])   # yelraM boB