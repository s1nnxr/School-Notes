####################
# Historie :D      #
####################
# 1960 - simula    #
# 1970 - smalltalk #
# 1980 - c++       #
# 1990 - java      #
# 2000 - Python    #
# 2000 - C#        #
####################
# Princip OOP      #
############################
# Objekty: věci            #
# Instance: konkrétní věci #
# Třída: šablona pro věci  #
####################################################################
# Zapouzdření: data a funkce jsou spojeny do objektů               #
# Dědičnost: třídy mohou dědit vlastnosti a metody z jiných tříd   #
# Polymorfismus: objekty mohou být použity jako instance své třídy #
#  aka "mnohotvárnost" - stejné rozhraní, různé implementace       #
# Abstrakce: skrývá složitost a zobrazuje pouze důležité části     #
####################################################################
# Poznámky:                                                        #
# Typ=Trída                                                        #
# Zapouzdření se zapisuje pomocí __init__ a self                   #
####################################################################
## Tvorba třídy
class Dog:
    ## Konstruktor
    def __init__(self, name):
        self.name = name
    def bark(self):
        return "Woof! My name is " + self.name
d=Dog("Rex")
print(d.bark())
# Vypsaní stromu dědičnosti pro třídu
def print_class_tree(cls:tyle, level=0):
    prefix ='| ' * level + '|--' if level > 0 else ''
    print(prefix + cls.__name__)
    for subclass in cls.__subclasses__():
        print_class_tree(subclass, level + 1)
print_class_tree(Exception)
