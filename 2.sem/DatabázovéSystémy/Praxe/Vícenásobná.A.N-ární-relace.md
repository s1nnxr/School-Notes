# Výcenásobné relace

### tymmy

| # | id_tym         | (pk) | int  | ||-o< zápasy.id_tymu_domaci ||-o< zápasy.id_tymu_hoste
|---|----------------|------|------|
| * | nazev          |      | text |
| * | rok_vzniku     |      | int  |
| * | id_mesta       | (fk) | int  | >o-|| mesta.id_mesta (muže byt tranferativní)
| * | datum_zalozeni |      | date |

### mesta

| # | id_mesta        | (pk) | int  | |-o< místa_zápasů.id_mesta  ||-o< tymmy.id_mesta
|---|-----------------|------|------|
| * | nazev           |      | text |

### zápasy

| # | id_zapasu        | (pk) | int  |
|---|------------------|------|------|
| * | datum_zapasu     |      | date |
| * | cas_zapasu       | (fk) | int  |
| o | cas_zapasu_konec |      | int  |
| * | id_mista_zapasu  | (fk) | int  | >o-|| místa_zápasů.id_mista_zapasu (muže byt tranferativní)
| * | id_tymu_domaci   |      | int  | >o-| tymmy.id_tym
| * | id_tymu_hoste    |      | int  | >o-| tymmy.id_tym
| o | vysledek_domaci  |      | int |
| o | vysledek_hoste   |      | int |

### místa_zápasů

| # | id_mista_zapasu  | (pk) | int  | ||-o< zápasy.id_mista_zapasu
|---|------------------|------|------|
| * | nazev            |      | text |
| * | id_mesta         | (fk) | int  | >o-| mesta.id_mesta 

# N-ární relace

Docela hovno, děláme 3 prdele sraček kolem.
vvvv
### Filmy

| # | id_filmu         | (pk) | int  | |-|< filmy_herci.id_filmu  
|---|------------------|------|------|
| * | nazev            |      | text |
| * | rok_vydani       |      | int  |
| * | délka            |      | int  |


### herci

| # | id_herce         | (pk) | int  | |-o< filmy_herci.id_herce
|---|------------------|------|------|
| * | jmeno            |      | text |
| * | prijmeni         |      | text |

#### filmy_herci

| # | id_filmu         | (pk) | int  | >|-| filmy.id_filmu 
|---|------------------|------|------|
| * | id_herce         | (pk) | int  | >o-| herci.id_herce
| o | postava          |      | text |

#### fil_reziseri

| # | id_filmu         | (pk) | int  | >|-| filmy.id_filmu
|---|------------------|------|------|
| * | id_rezisera      | (pk) | int  | >|-| reziseri.id_rezisera

#### fil_skladatel
| # | id_filmu         | (pk) | int  | >|-| filmy.id_filmu
|---|------------------|------|------|
| o | id_skladatele    | (pk) | int  | >|-| skladatelé.id_skladatele

#### fil_scenariste
| # | id_filmu         | (pk) | int  | >|-| filmy.id_filmu
|---|------------------|------|------|
| o | id_scenariste    | (pk) | int  | >|-


### reziseri

| # | id_rezisera      | (pk) | int  | |-|< fil_reziseri.id_rezisera
|---|------------------|------|------|
| * | jmeno            |      | text |
| * | prijmeni         |      | text |

### skladatelé

| # | id_skladatele    | (pk) | int  | |-|< fil_skladatel.id_skladatele
|---|------------------|------|------|
| * | jmeno            |      | text |
| * | prijmeni         |      | text |

### scenariste

| # | id_scenariste    | (pk) | int  | |-|< fil_scenariste.id_scenariste
|---|------------------|------|------|
| * | jmeno            |      | text |
^^^^
Docela hovno, děláme 3 prdele sraček kolem.
Lepší řešení
vvvv

### Filmy

| # | id_filmu         | (pk) | int  | |-|< filmy_herci.id_filmu  
|---|------------------|------|------|
| * | nazev            |      | text |
| * | rok_vydani       |      | int  |
| * | délka            |      | int  |


### osoby

| # | id_herce         | (pk) | int  | |-o< filmy_herci.id_herce
|---|------------------|------|------|
| * | jmeno            |      | text |
| * | prijmeni         |      | text |

### filmove_pozice

| # | id_pozice        | (pk) | int  | |-o< filmy_herci.id_pozice
|---|------------------|------|------|
| * | nazev            |      | text |

### fil_pozice_osoby

| # | id_filmu         | (pk) | int  | >|-| filmy.id_filmu
|---|------------------|------|------|
| * | id_herce         | (pk) | int  | >o-|| osoby.id_herce
| * | id_pozice        | (pk) | int  | >o-|| filmove_pozice.id_pozice

