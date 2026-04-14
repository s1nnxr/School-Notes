# Místo toho pojmenujeme všechny věci tím, že jméno nadefinujeme v základní třídě. Dále přidáme metody sound() a hello(). Metodu sound() přepíšeme v některých podtřídách.

class Thing:
  def __init__(self, name: str):
    self.name = name

  def sound(self):
    return ''

  def hello(self):
    print(f'Hi, I am {self.name} - {self.sound()}!')

class Machine(Thing):
  def __str__(self) -> str:
    return self.__class__.__name__ + ': ' + self.name
  def __repr__(self) -> str:
    return str(self) + ' / ' + self.sound()
  def sound(self) -> str:
    return 'wrrr'

class LivingThing(Thing):
  pass

class Robot(Machine):
  pass

class Animal(LivingThing):
  pass

class Cyborg(Animal, Robot):
  pass

class Mammal(LivingThing):
  pass

class Dog(Mammal):
  def __str__(self) -> str:
    return self.__class__.__name__ + ': ' + self.name
  def __repr__(self) -> str:
    return str(self) + ' / ' + self.sound()
  def sound(self) -> str:
    return 'woof'

class Cat(Mammal):
  def sound(self):
    return 'miaow'

class Cat(Mammal):
  def __str__(self) -> str:
    return self.__class__.__name__ + ': ' + self.name
  def __repr__(self) -> str:
    return str(self) + ' / ' + self.sound()
  def sound(self) -> str:
    return 'miaow'

things: list[Thing] = [Machine('M'), Robot('R'), Cat('Miezekatze'), Dog('Athos')]

for thing in things:
    print(thing)

#❖ Úloha: lepší výpis
#Upravte třídu Thing tak, aby vypisovala jméno objektu a jeho zvuk, podobně, jako je to již u kočky.

