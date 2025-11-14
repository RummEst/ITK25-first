
def tere():
    print("Tere, kuidas laheb?")

def tere_name(name):
    return f"tere {name}"

def div(a, b):
    return a / b

def introduce(name, age=25):
    """

    :param name: str isiku nimi
    :param age: int isiku vanus
    :return: Tekstiline tutvustus
    """
    return f"Tema on {name} ja ta on {age}a vana"

for x in range(5):
    tere()

names = ["Marko", "Bob", "Ross"]

for name in names:
    print(tere_name(name))

print(introduce("Rosss"))

def nimed(nimedl):
    for n in nimedl:
        if len(n) == 4:
            print(n)

nimed(names)