# Oběktové Programování:
# Objektové programování je základný myšlení v programování
# Jiné základní myšlení programování je imperativný což větvý operace s daty
# Objektové programování je
# - Identifikovatelný (je vymezovaný a může mít identifokátor)
# - Oběkty mají svůj životní cyklus (mohou být vytvořeny, použity a zničeny)
## [Problémová doména](./ProblémováDoména.py)
# - Objekty se nějak chovají (záleží nam na to jakou mají roli a co dělají)
#  - Objekty mají své atributy (vlastnosti, které popisují objekt)
# Třída:
# - Třída je šablona pro objekty se stejnými atributy a nebo chováním
#  - V lidskem světě platí, třída == pojem (rasismus)

# Třída jako syntatický prostředek:
# - Třída má identifikátor
# - Třída má metody (chování)
#  - Funkce, které pracují nad objektem = adresát metody
#   - Mohou menit stav adresáta
#   - Mohou vytvoří nový objekt na základě stavu adresáta
#   - Mohou mít vedlejší efekt (ten se musí týkat prostředku spojených [Vlastněných či Řízených] objektem)
# - Třída popisuje z jakých dat je oběkt složen
# - Musí být schopna tvořit své instance
# (oop preferuje zapouzdření)
# - Vnitřní implementace je skrytá
# - viditelnost jsou metody (rozhraní)
# = snižuje závislost mezi různou urovní kódu a datové representace (nezáleží nám na tom jak to funguje [nepotřebujeme vědět jak to funguje])
### basically jako TCP/IP


# Návrh třídy:
# Jméno: Date
# jak vzniká: Date(20,2,2026) # toto je gregoriánský kalendář
# allokace datumu v paměti
# d=Date(20,2,2026)
## Metody:
# - d.day() -> 20
# - d.month() -> 2
# - d.year() -> 2026

# - d.week_day() -> 5 (ne = 0)
# - d.shift_day(1) -> Date(21,2,2026)

# - d.leap_year() -> False

# Vytvoření třídy v Pythonu:
class Date:
    def __init__(self, day:int, month:int, year:int): # konstruktor/iniciator __init__ je magická metoda
        # Tvorba kontruktoru
        #FIXME: Kontrola validity datumu
        self._day = day
        self._month = month
        assert 1970<year<2099, "Invalid year"
        self._year = year
    def day(self) -> int:
        return self._day
    def month(self) -> int:
        return self.month
    def year(self) -> int:
        return self.year
    def week_day(self) -> int:
        pass
    def shift_day(self, shift:int)-> "Date":
        shift_day=self._day+shift
    def leap_year(self) -> bool:
        return self._year%4==0
d=Date(20,2,2026)
def gregorian_to_jdn(year: int, month: int, day: int) -> int:
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    return day + ((153 * m + 2) // 5) + (365 * y) + (y // 4) - (y // 100) + (y // 400) - 32045

def jdn_to_gregorian(jdn: int) -> (int, int, int):
    a = jdn + 32044
    b = (4 * a + 3) // 146097
    c = a - (146097 * b) // 4
    d = (4 * c + 3) // 1461
    e = c - (1461 * d) // 4
    m = (5 * e + 2) // 153
    day = e - (153 * m + 2) // 5 + 1
    month = m + 3 - 12 * (m // 10)
    year = 100 * b + d - 4800 + (m // 10)
    return year, month, day


# Alternativní reperezentace kalandáře:
# - počet dní od jistého data (např. 1.1.1970)
# - Julianské datum (počet dní od 1.1.4713 př.n.l. v poledne)
class Date2:
    def __init__(self, day: int, month: int = None, year: int = None):
        if day is not None and month is not None and year is not None:
            self.jdn = gregorian_to_jdn(year, month, day)
        elif day is not None and month is None and year is None:
            self.jdn = day
        else:
            raise ValueError("Provide either (day, month, year) or just a single (jdn).")

    def day(self) -> int:
        return jdn_to_gregorian(self.jdn)[2]
        
    def month(self) -> int:
        return jdn_to_gregorian(self.jdn)[1]
        
    def year(self) -> int:
        return jdn_to_gregorian(self.jdn)[0]
        
    def week_day(self) -> int:
        return self.jdn % 7
        
    def leap_year(self) -> bool:
        y = self.year()
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
        
    def shift_day(self, shift: int) -> "Date2":
        return Date2(self.jdn + shift)
        
    def __repr__(self) -> str:
        return f"{self.year():04d}-{self.month():02d}-{self.day():02d}"
        
    def __str__(self) -> str:
        return f"{self.day():02d}.{self.month():02d}.{self.year():04d}"

# Testing with a proper Date2 object
print(Date2(20, 2, 2026))
