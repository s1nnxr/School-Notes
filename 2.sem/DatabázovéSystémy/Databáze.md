# Historie Databází
- vznikaly v padesátých letech a šedmdesátých letech především v IBM
## Relační databázový model
- byl definován v roce 1970 E. F. Coddem
- Vycházi s implementací tabulkového a síťového modela
- je přesně definován pomoví elementárních matematických pojmu:
    - Mnoziny
    - Relace
    - Operace (funkce) nad relacemi
- Klade důraz na datovou integritu (a to jak ve statickém pohledu tak i v dynamickém pohledu)
- V současnosti je to klasický model pro většinu databázových systémů
## Tabulka
- Základní datová struktura
- Tabulka se sestává z posloupnosti uspořádaných n-tic (tuplů) nebo řádku (rows), pro nějš platí:
    - N-tice v tabulce jsou jedinečné
    - Všechny n-tice v tabulce jsou strukturálně shodné, tj. mají stejný počet položek a odpovídající si položky jsou stejného typu (primárně: jsou stejně reprezentovány)
    - Položky jsou atomické, tj. nelze je dělit na podpoložky(=nejsou to pole či podstruktury)
## R-DBMS
- *DBMS* = *Database Management System* = systém pro správu databází
    - úložiště (data a metadata)
    - výknné jádro zajištující přístup k datům
- *Klient Server*= Výkoné jádro DBMS tvoří (alespon) jeden oddělený process (typycky na serveru)

# SQL
- *SQL* = *Structured Query Language* = jazyk pro práci s relačními databázemi
    - QL: *Query Language* = jazyk pro dotazování
    - DDL: Data Definition Language = jazyk pro definici dat (create table, alter table, drop table)
    - DML: Data Manipulation Language = jazyk pro manipulaci s daty (insert, update, delete)
    - DCL: Data Control Language = jazyk pro kontrolu přístupu (grant, revoke)
    - DBMS administrace
- úzce propojen s vývojem relačního modelu a RDBMS (dnešní SQL však obsahuje i nerelační prvky)
- De facto dtandart pro EDBMS (jen v oblasti dotaů esixtují ijrahivé alternativy QBE, LINQ)
## Standardizace SQL
- SQL je průběžně standardizován ISO
- Nejduležitější standardy:
    - SQL-92 (1992) - (společný základ, některé části jsou zastaralé)
    - SQL:2003 (2003) - (v zasadě podporováno, SML, analystické funkce)
    - SQL:2008 (2008), SQL:2011 (2011) - (jen dílčí podpora)
- Podpora standarů není ani u nejduležitějších systémů úplná, ale spíše se jedná o inspiraci pro vývojáře

# Základní pravidla
- Veškeré zpracování by mělo být provedeno pomocí SQL
    - Obecně je to rychlejší než zpracování v aplikačním kódu
    - Konzistence a integrita dat je lépe zajištěna
    - Menší zátěž na přenos dat
# Základní syntaxe
- SQL standardně nerozeznává malá a velká písmena, (v klíčových slovech i identefikátorech)
- Identifikátory jsou běžně tvořeny jen ASCII znaky
- Symbol v uvozovkách (qouted identifier) je však vždy interpretováj jako identidikátor

# Datatypy
- NUMERUC - pro číselné hodnoty u kterých se nám nemění přesnost
- INTEGER - pro celé čísla
- FLOAT - pro čísla s pohyblivou desetinnou čárkou
- CHAR(n) - pro řetězce pevné délky n pro rodné číslo, PSČ, telefonní číslo
- VARCHAR(n) - pro řetězce pevné délky n pro rodné číslo, PSČ, telefonní číslo
- TEXT - pro dlouhé texty pro popisy, komentáře, poznámky
- DATE - pro datum
- TIME - pro čas
- TIMESTAMP - pro datum a čas
- timestamp with time zone - pro datum a čas s časovou zónou
- INTERVAL - pro časový interval
- BOOLEAN - pro logické hodnoty (true/false)
- BLOB - pro binární data pro obrázky, zvuky, videa je to beztvarý datový typ
- CLOB - pro velké textové data pro dlouhé texty, dokumenty, knihy je to beztvarý datový typ

# SQL literály
- Řetězcové literály jsou uzavřeny v jednoduchých uvozovkách (')
- Časové literály:
    - TIMESTAMP '2024-01-01 12:00:00'
    - TIMESTEMP WITH TIME ZONE '2024-01-01 12:00:00+01:00'
- bytea (BLOB), hexadecimální literály:
    - X'1A2B3C4D'
    - E'\\x1A2B3C4D'
# Přetypování dat
- SQL podporuje statické typování (již při překladu)
- ANSI přetipování: cast(value AS type)
# Hodnoty NULL
- NULL představuje neznámou nebo chybějící hodnotu
- NULL není stejné jako prázdný řetězec nebo nula
- Nezaznamenou hodnozu (not avalable, N/A), například nezadané jméno
## Neaplikovatelnou hodnotu 
- (daný atribut není aplokovatelný pro daný oběkt) napč. plat u dobrovolníka
- Mámely hodně null to může znamenat že máme špatně navrženou databázi, protože by měly být použity jiné tabulky pro tyto případy
## Práce s NULL
- NULL se šíří (1+NULL = NULL)
- NULL není rovno NULL (NULL = NULL je false)
- NULL se ignoruje v agregačních funkcích (COUNT(*), SUM(), AVG(), MAX(), MIN())
# Převod NULL na hodnotu a v.v.
- při převodu NULL na běžnou hodnotu se používá funkce COALESCE(expr1, expr2, ...)
- Pro opačný převod (náhradní hodnota na NULL) NULLIF(expr) nebo NULLIF(expr1, expr2) vrací NULL pokud jsou expr1 a expr2 stejné, jinak vrací expr1
- Pro testování zda je hodnota NULL potřeba využít is distinct from null tesp. is not distinct from null
