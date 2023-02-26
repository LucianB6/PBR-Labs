print("O sa va ajut sa alegeti un optional pentru fiecare pachet\n")
print("O sa alegem mai intai un optional din primul pachet\n")

pachet1 = open("pachet1.txt", "r")

print("Materiile din pachetul 1 sunt: \n\n", pachet1.read(), end="\n")
pachet1.close()

pachet1 = []

raspuns1 = input("Va place sa analizati o problema sau s-o scrieti? (analiza/scriere) ")

raspuns2 = input("Va place sa rezolvati probleme matematice? (da/nu) ")

raspuns3 = input("Va place sa dezvoltati aplicatia pe mobil sau pe web? (mobile/web) ")

pachet1.append(raspuns1)
pachet1.append(raspuns2)
pachet1.append(raspuns3)

rule_baze = [["analiza", "nu", "web"], ["scriere", "nu", "web"]]
mobile_dev = [["scriere", "nu", "mobil"], ["analiza", "nu", "mobil"]]
game_dev = [["scriere", "da", "web"], ["scriere", "da", "mobil"]]
number_theory = [["analiza", "da", "web"],["analiza", "da", "mobile"]]

if pachet1 in rule_baze:
    print("Ati ales optionalul de Rule based programming \n\n")
elif pachet1 in mobile_dev:
    print("Ati ales optionalul de Mobile development \n\n")
elif pachet1 in game_dev:
    print("Ati ales optionalul de Game development \n\n")
elif pachet1 in number_theory:
    print("Ati ales optionalul de Computational Aspects on the Number Theory \n\n")

pachet2 = open("pachet2.txt", "r")
print("Materiile din pachetul 2 sunt: \n\n", pachet2.read(), end="\n")
pachet2.close()

pachet2 = []

raspuns1 = input("Va place sa lucrati in echipa? (da/nu) ")

raspuns2 = input("Doresti sa aprofundezi materii deja studiata sau vrei ceva nou? (studiat/nou) ")

raspuns3 = input("Va place sa dezvoltati aplicatia pe un sistem fizic sau pe web? (sistem/web) ")

pachet2.append(raspuns1)
pachet2.append(raspuns2)
pachet2.append(raspuns3)

Psihologie = [["da", "nou", "sistem"], ["da", "studiat", "sistem"]]
Cloud = [["nu", "studiat", "web"], ["da", "studiat", "web"]]
Iot = ["nu", "nou", "sistem"], ["nu", "studiat", "sistem"]
Analiza = [["da", "nou", "web"],["nu", "nou", "web"]]

if pachet2 in Psihologie:
    print("Ati ales optionalul Psihologia comunicarii profesionale in domeniul IT-lui \n\n")
elif pachet2 in Cloud:
    print("Ati ales optionalul de Cloud Computing \n\n")
elif pachet2 in Iot:
    print("Ati ales optionalul Interactune om-calculator \n\n")
elif pachet2 in Analiza:
    print("Ati ales optionalul de Analiza a retelelor media sociale \n\n")

pachet3 = open("pachet3.txt", "r")
print("Materiile din pachetul 3 sunt: \n\n", pachet3.read(), end="\n")
pachet3.close()

pachet3 = []

raspuns1 = input("Iti place sa lucrezi cu microprocesoare? (da/nu) ")

raspuns2 = input("Preferi sa construiesti un sistem sau sa il analizezi? (construieste/analizeaza) ")

raspuns3 = input("Preferi o gandesti o solutie sau sa o implementezi? (gandeste/implementeaza) ")

pachet3.append(raspuns1)
pachet3.append(raspuns2)
pachet3.append(raspuns3)

petri = [["da", "construieste", "gandeste"], ["da", "construieste", "implementeaza"]]
smart = [["da", "analizeaza", "gandeste"], ["da", "analizeaza", "implementeaza"]]
automobile = [["nu", "construieste", "gandeste"], ["nu", "construieste", "implementeaza"]]
internet = [["nu", "analizeaza", "gandeste"], ["nu", "analizeaza", "implementeaza"]]

if pachet3 in petri:
    print("Ati ales optionalul de Retele Petri si aplicatii \n\n")
elif pachet3 in smart:
    print("Ati ales optionalul de Smart Card-uri si Aplicatii \n\n")
elif pachet3 in automobile:
    print("Ati ales optionalul de Inginerie software specifica automobilelor \n\n")
elif pachet3 in Analiza:
    print("Ati ales optionalul de Introducere in Internetul lucrurilor \n\n")

