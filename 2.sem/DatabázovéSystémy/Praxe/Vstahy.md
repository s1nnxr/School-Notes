# Kardinalita
= Typ vztahu mezi dvěma entitami
## Druhy kardinality

# Zákazníci
| Typ | Jmeno       | Popis       |
| --- | ----------- | ----------- |
| #   | id_costumer | serial (PK) |  |--< id_costumer in Objednávky |--| id_costumer in Přihlašovací údaje
| *   | name        | text        |
| *   | surname     | text        |
| *   | phone       | varchar(20) |
| *   | email       | text        |

# Objednávky
| Typ | Jmeno            | Popis        |
| --- | ---------------- | ------------ |
| #   | id_order         | serial (PK)  | |--< id_order in Obj_vyr |--| id_adress in Fakturační adresa
| *   | order_date       | date         |
| o   | delivery_date    | date         |
| *   | id_costumer      | integer (FK) | >--| id_costumer in Zákazníci
| *   | arrival _address | text         |

# Vyrobky

| Typ | Jmeno          | Popis         |
| --- | -------------- | ------------- |
| #   | id_product     | serial (PK)   | |--< id_product in Obj_vyr  |--| id_product in Slevy
| *   | name           | text          |
| *   | price          | numeric(10,2) |
| o   | description    | text          |
| *   | id_druh_product| integer (FK)  | >--| id_druh_product in Druhy výrobků

# Druhy výrobků

| Typ | Jmeno          | Popis         |
| --- | -------------- | ------------- |
| #   | id_product     | serial (PK)   | |--< id_druh_product in Vyrobky
| *   | name           | text          |

# Obj_vyr

| Typ | Jmeno         | Popis        |
| --- | ------------- | ------------ |
| #   | id_order      | integer (FK) | >--| id_order in Objednávky
| #   | id_product    | integer (FK) | >--| id_product in Vyrobky
| *   | quantity      | integer      |

# Slevy

| Typ | Jmeno          | Popis        |
| --- | -------------- | ------------ |
| #   | id_discount    | serial (PK)  | |--| id_discount in Obj_vyr
| *   | sale           | numeric(5,1) |
| *   | date_from      | date         |
| *   | date_to        | date         |

# Fakturační adresa

| Typ | Jmeno          | Popis        |
| --- | -------------- | ------------ |
| #   | id_address     | serial (PK)  | |--| id_address in Objednávky
| *   | Address        | text         |

# Přihlašovací údaje
| Typ | Jmeno          | Popis        |
| --- | -------------- | ------------ |
| #   | id_costumer    | integer (FK) | |--| id_costumer in Zákazníci
| *   | hash_password  | text         |
| *   | date_created   | date         |

# Vztah mezi Zákazníky a Objednávkami
1. 1:N - Jeden ***zákazník*** může mít více ***objednávek***, ale každá ***objednávka*** patří pouze jednomu ***zákazníkovi***. 1->n a 1<-1
2. M:N - ***Objednavka*** může obsahovat více ***produktů*** a každý ***produkt*** může být součástí více ***objednávek***. 1->n a n<-1
3. N:1 - Každý ***druh_produktu*** může být přiřazen k více ***produktům***, ale každý ***produkt*** patří pouze jednomu ***druhu_produktu***. 1->1 a n<-1
4. 1:1/0 - Vyrobek může mít slevu, ale nemusí mít, a sleva může být přiřazena pouze jednomu výrobku. 1->1 a 1<-1
5. 1:1/0 - Objednávka může mít fakturační adresu, ale nemusí mít, a fakturační adresa může být přiřazena pouze jedné objednávce. 1-|1 a 1|-1

# Značky/Optionalita
- # - primární klíč
- * - povinné pole
- o - nepovinné pole

- | - nutký záznam
- > - odkaz na jinou tabulku
- < - odkaz z jiné tabulky
- o - volitelný záznam

# Transferabilita
## Značky
- čára - transferabilní
- <> - netransferabilní
