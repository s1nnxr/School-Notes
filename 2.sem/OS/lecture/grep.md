# Přesměrování dat

## Přesměrování dat do souborů
- Přesměrování standardního výstupu do souboru

```bash
echo "Hello, World!" > output.txt
```
## Zahazování dat
- Zahození chyby to /dev/null a vypsaní něčeho jiného
```
```bash
rm -rf /tmp/dir 2>/dev/null || echo "Nešlo smazat adresář"
```
## Přesměrování dat do příkazu
- Přesměrování standardního výstupu do příkazu

```bash
bash << "konec" ls echo "$DATE" "konec"
```

## Přesměrování dat do tvou outputu s tee
- Přesměrování standardního výstupu do souboru a zároveň na obrazovku

```bash
echo "Hello, World!" | tee output.txt
```
# Neanonimní pipa
- Umožní nám přesměrovat data z jednoho příkazu
```bash
mkfifo mypipe
# V jednom terminálu
echo "Hello, World!" > mypipe
# V jiném terminálu
cat mypipe
```
# Transformace dat s TR
- Umožní nám transformovat data, například převést malá písmena na velká

```bash
echo "hello, world!" | tr '[:lower:]' '[:upper:]'
```
# Grep
- Umožní nám zahazovat data
