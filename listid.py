# list ehk massiv
# List [nimekiri, loend], tuple (järjend), dictionary {sõnastik}

places = []

places.append("Kehtna") # Lisab 1 elementi lõppu
places.append("Rapla")
places[1:1] = ["Tallinn", "Pärnu"]  # lisab keskele?????????????
places.extend(["Viljandi", "Tartu", "Rapla"])  # LISAB LÕPPU (liidab teise listi lõppu)
places.insert(2, "Are")

nrs = [1, 2, 3]

# kustutama
places.remove("Rapla") # del rapla
places.pop(6) # del BY INDEX
del places[2] # del 2


print(places)
print(nrs)

# ÜLESANNE: lisa rapla, pärnu ja viljandi cahele ni9ng listi l6ppu
# places[3:3] = "Rapla"
places.insert(places.index("Viljandi"), "Rapla")
places.append("Rapla")

print(places)

# leiame elemendi indexi & mitu korda esineb
place = places[-1] # rapla (last)
i = places.index(place) # esimene rapla
count = places.count(place) # mitu rapla
print(i, count)

# kas rapla on nimekirjas
if place in places:
    print(f"{place} on olemas!")

print(f"listi suurus: {len(places)}")
print(f"viimane index: {places[len(places)-1]}")

# Koopia listist
list_copy = places.copy()
list_list = list(places)

# Sorteerimine
list_copy.sort()
# A->Z  .sort()
# Z->A  .sort(reversed=True)
new_list_list = sorted(places, reverse=True)

print(list_copy, new_list_list, places, sep="\n")

print()

new_list_list.clear() # tyhjenda list
print(new_list_list)


# Ülesanne: Kasuta originaal listi ja eemalda listist viimane Rapla. Väljasta 3. el kesmi e täht suurtähena
places.pop(len(places)-1)
print(places)
print(places[2][2].upper()) # 3. elemendi 3. täht