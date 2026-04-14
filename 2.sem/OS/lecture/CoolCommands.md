# Cool Commands
Realný smazání souboru
```bash
shred -u -n 0 -z -v -- "$file"
```
Metadata o souboru
```bash
stat "$file"
```
Vypsání všch disků a jejich využití
```bash
lsblk -f
```
Práva pro soubory
```bash
# Jestli jsi trouba
chmod 755 "$file"
# jinak
chmod u+x "$file"
```
# chown - změna vlastníka souboru
```bash
# Změna vlastníka na uživatele "john"
sudo chown john "$file"
# Změna vlastníka a skupiny na "john" a "developers"
sudo chown john:developers "$file"
```
chattr - změna atributů souboru
```bash
# Nastavení atributu "immutable" (nepřepisovatelný)
sudo chattr +i "$file"
```
