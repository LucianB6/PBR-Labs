from re import findall

from bigtree import Node, print_tree

optional1 = Node("optional", nume="Programare bazata pe reguli")
materie1 = Node("materie1", nume="Inteligenta Artificiala", parent=optional1)
materie2 = Node("materie2", nume="Structuri de date", parent=optional1)

optional2 = Node("optional", nume="Aspecte computationale in teoria numerelor")
materie3 = Node("materie1", nume="Inteligenta Artificiala", parent=optional2)
materie4 = Node("materie2", nume="Structuri de date", parent=optional2)

optional3 = Node("optional", nume="Analiza retelelor media sociale")
materie5 = Node("materie1", nume="Inteligenta Artificiala", parent=optional3)
materie6 = Node("materie2", nume="Structuri de date", parent=optional3)

optional4 = Node("optional", nume="Introducere in IoT")
materie7 = Node("materie1", nume="Inteligenta Artificiala", parent=optional4)
materie8 = Node("materie2", nume="Structuri de date", parent=optional4)

optional5 = Node("optional", nume="Tehnici de programare pe platforme mobile")
materie9 = Node("materie1", nume="Inteligenta Artificiala", parent=optional5)
materie10 = Node("materie2", nume="Structuri de date", parent=optional5)

optional6 = Node("optional", nume="Proiectarea jocurilor")
materie11 = Node("materie1", nume="Inteligenta Artificiala", parent=optional6)
materie12 = Node("materie2", nume="Structuri de date", parent=optional6)

optional7 = Node("optional", nume="Programare competitiva")
materie13 = Node("materie1", nume="Inteligenta Artificiala", parent=optional7)
materie14 = Node("materie2", nume="Structuri de date", parent=optional7)

optional8 = Node("optional", nume="Inginerie Software Specifica Automobilelor")
materie15 = Node("materie1", nume="Inteligenta Artificiala", parent=optional8)
materie16 = Node("materie2", nume="Structuri de date", parent=optional8)

optional9 = Node("optional", nume="Cloud Computing")
materie17 = Node("materie1", nume="Inteligenta Artificiala", parent=optional9)
materie18 = Node("materie2", nume="Structuri de date", parent=optional9)

variante = open("optionale", mode='r',encoding="latin").readlines()
variante = ' '.join(variante)
print("Lista de optionale: \n")
print(variante, end="\n\n")

optiune = input("Alege un optional pe care ai dori sa-l urmezi pentru a afla ce cunostiinte ar trebui sa ai: ")

if optiune == "Programare bazata pe reguli":
    print_tree(optional1, attr_list=["nume"])
elif optiune == "Cloud Computing":
    print_tree(optional9, attr_list=["nume"])
elif optiune == "Aspecte computationale in teoria numerelor":
    print_tree(optional2, attr_list=["nume"])
elif optiune == "Analiza retelelor media sociale":
    print_tree(optional3, attr_list=["nume"])
elif optiune == "Introducere in IoT":
    print_tree(optional4, attr_list=["nume"])
elif optiune == "Tehnici de programare pe platforme mobile":
    print_tree(optional5, attr_list=["nume"])
elif optiune == "Proiectarea jocurilor":
    print_tree(optional6, attr_list=["nume"])
elif optiune == "Programare competitiva":
    print_tree(optional7, attr_list=["nume"])
elif optiune == "Inginerie Software Specifica Automobilelor":
    print_tree(optional8, attr_list=["nume"])
# (Node(/a, age=90), Node(/a/b, age=65), Node(/a/c, age=60))
