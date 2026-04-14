# Spojení Tabulek
## Join
- Spojení tabulek pomocí klíče (sloupce) z obou
## Cross Join
- Spojení všech řádků z obou tabulek (kartézský součin)
- AxB ((a,b), a je v A, B je v B) <- kemo nevím co tam vaflí D:
## Inner Join
- Udělá cross join a pak vybere jen ty řádky, které mají shodné hodnoty v klíčových sloupcích
```sql
-- Vybereme všechny řádky z tabulky A a B, které mají shodné hodnoty v sloupci obec_id a obec
select *
from A.jméno, B.jméno                                                         -- vypiše jména tabulek pro přehlednost
inner join B                                                                  -- spojíme tabulku
A                                                                             -- spojíme tabulku A
on                                                                            -- podmínka spojení, která určuje jak se mají řádky spojit
A.obec = B.obec_id
```
## Outer Join
- Vnější spojení, udělej inner join a pak přidej řádky, které nemají shodné hodnoty v klíčových sloupcích
### Left Join
- Přidá řádky z levé tabulky, které nemají shodné hodnoty v klíčových sloupcích, a doplní je NULL hodnotami pro sloupce z pravé tabulky
### Right Join
- Přidá řádky z pravé tabulky, které nemají shodné hodnoty v klíčových sloupcích, a doplní je NULL hodnotami pro sloupce z levé tabulky
### Full Join
- Přidá řádky z obou tabulek, které nemají shodné hodnoty v klíčových sloupcích, a doplní je NULL hodnotami pro sloupce z druhé tabulky
