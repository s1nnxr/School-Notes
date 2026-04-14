# # Dědičnost (inheritance)
# 
# - dědičnost je typickým mechanismem OOP (Simula 68 podporoval dědičnost)
# - existuje přístupů k immplementaci dědičnosti a také použití
# 
# Dědičnost je:
#   1. mechanismus podporovaný OOP
#   2. návrhový princip jak uspořádat třídy
# 
# ## Mechanismus dědičnosti
# 
# dědičnost se týká tříd nikoliv jednotlivých objektů
# 
# 1. dědění a predefinování metod tříd
# 2. skládání pro objekty tříd
# 3. polymorfismus na urovni tříd
# 
# ### dědění a předefinování metod
# 
# existuje bázová třída a z ní lze dědičnost odvodit odvozenou třídou
# 
# - odvozená třída dědí všechny metody bázové třídy
# - odvozená třída může přidávat vlastní
# - odvozená třída může předefinovat zděděné metody
class Base:
    def __init__(self, value):
        self._value = value
    def base_method(self):
        print("Base method")
    def method(self):
        print(self._value)

class Derived(Base):
    # Je nutné se postarat, aby v instancích odvozené třídy byly k dispozici i "atributy objektu bázové třídy":
    ## v Pythonu se to provádí pomocí delegování konstruktorů:
    ### - Konstruktor odvozené třídy musí volat konstruktor bázové třídy (automaticky jen u implicitních bezparametrických konstruktorů)
    def __init__(self):
        super().__init__(21) # <- objekt bázové třídy (values)
        # Base.__init__(self,21) # <- Alternativa


    def new_method(self):
        print("Derived method")

    # Předefinování metody je nutno odlišit od zastínění (shadowing)
    ## Overraiding = předefinování + zachování původní metody (super)
    ### Měla by mít stejné parametry jako původní metoda
    ### Měla by vracet obdobný výsledek jako původní metoda
    ### Musí splňovat kontrakt původní metody: Precondition (předpoklad), Postcondition (následek), Invariant (neporušitelnost)
    ### Pokud jsou v bázove třídě nějaké vyjímky, tak odvozená nesmí vyhazovat jiné vyjímky
    def base_method(self):
        print("Overridden base method")

    ## Shadowing = předefinování + nahrazení původní metody
    def shadowed_method(self):
        print("Shadowed base method")

instance = Derived()
instance.base_method()
x=Derived()
x.method()

# Podpora Polymorfismu
# Definice:
# - Je možné napsat kód, který je různě implementován v závislosti na třídách objektů a zároveň by měl splňovat kontrakt
## Ducky Typing
## Definice:
## - Univerzální polymorfismus
## Příklad:
## `a+b` <- Je to sčítání (pro veškeré číselné typy včetně bool)
## ^ je to spojování řetězců
## Obecně funguje pro jakékoliv `a` pokud implementuje metodu `__add__`
## Nebo/Zároveň `b` implementuje metodu `__radd__`
### Duck typing vede k divokému polymorfismu (vše co má kompatibilní metodu
### lze polymorfně volat) ALE kontrakt může být zcela jiný
## Dědičnost vede k bezpežnému polymorfismu (není v pythonu jediný)
class ConstantValue:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value

class LimitedConstantValue(ConstantValue):
    def __init__(self, value, minval, maxval):
        if not (minval <= value <= maxval):
            raise ValueError("Out of limit")
        super().__init__(value)
# SUbtituční princip:
## - Objekty odvozené třídy mohou v jakémkoliv kódu nahradit objekty bázové třídy
## - tj. polymorfismus je bezpečný (! předefinování musí splňovat kontrakt)
### Komunativnost = Nezáleží na pořadí
## Bázová třída = Nadřazená (jen při splnění principu substituce)
## Odvozená třída = Podřízena
class PrintedLimitedConstantValue(LimitedConstantValue):
    def __init__(self, value, minval, maxval):
        super().__init__(value, minval, maxval)
    @property
    def value(self):
        print(f"value is {self._value}")
        return super().value
x =PrintedLimitedConstantValue(10,0,100)
x.value
## Jak se projeví polymorfismus v pythonu?
### - Není poviný: funguje bezpečný duck typing polymorfismus
### - má však 2 výhody: Při dinamickém a statickém testování typů je odvozená třída podtřídou
x=PrintedLimitedConstantValue(10,0,100)
isinstance(x,PrintedLimitedConstantValue)
isinstance(x,ConstantValue)
isinstance(x,object)
woman = "lol"

print("Je žená objekt?")
print(isinstance(woman,object))

def print_value(o: ConstantValue):
    print(o.value)
print_value(x)
# print_value(1) <- není atribut konstantní value

# Využití dědičnosti:
## 1. Použití pro Abstract base class (list, iterátor)
### - Nemají žádné atributy
### - Metody jsou pouze abstraktní (tj, jen hlavička)
### > Je to pouze příslib splnění kontraktu (je nutné předdefinovat metody a splnit kontrakt)
## 2. Mixiny (přidání funkčnosti do existující třídy) -> příště
## 3. Reprezentace specializace a generalizace (TCP/IP více méně, bez tříd jsme v ISO/OSI)
## 4. Reprezentace hierarchie tříd (Skládání pomoci vícenásobné dědičnosti)
