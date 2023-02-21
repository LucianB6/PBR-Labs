from bigtree import Node, print_tree

optional = Node("optional", nume="Programare bazata pe reguli")
materie1 = Node("materie1", nume="Inteligenta Artificiala", parent=optional)
materie2 = Node("materie2", nume="Structuri de date", parent=optional)

optiune = input("Alege un optional pe care ai dori sa-l urmezi pentru a afla ce cunostiinte ar trebui sa ai: ")


print_tree(optional, attr_list=["nume"])

