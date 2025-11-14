"""
Luua kasutajataele username ja email
USERNAME
    eesnimi.perenimi
    lowercase
    remove rõhumärgid (öäüõ žš)
    remove spaces and hyphen
EMAIL ADRESS
    eesnimi.perenimi@asutus.com
KELLELE TEHA
    born 1990-1999
UUS FAILI SISU
    sisaldub päist
    Eesnimi;Perenimi;Isikukood;Kasutajanimi;Email
"""

import unicodedata
def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
               if unicodedata.category(c) != "Mn")



src = "Persons.csv"
dst = "Persons_new.csv"

domain = "@gmail.com"
header = ["Username", "Email"]

with open(src, "r", encoding="utf-8") as f:
    with open(dst, "w", encoding="utf-8") as d:
        contents = f.readlines()
        old_header = contents[0].strip().split(";")
        new_header = ";".join(old_header[:2] + old_header[4:] + header)
        print(new_header)
        d.write(new_header + "\n")

        for line in contents[1:]:
            parts = line.strip().split(";")
            year = int(parts[2].split(".")[2])

            if 1990 <= year <= 1999:
                fname, lname = parts[0].replace(" ", "").replace("-", ""), parts[1]
                username = strip_accents(".".join([fname, lname]).lower())
                email = username + domain

                new_line = ";".join(parts[:2] + parts[4:] + [username, email])
                d.write(new_line + "\n")

                if len(username) >= 20:
                    print(new_line)
    print("VALMIS")


