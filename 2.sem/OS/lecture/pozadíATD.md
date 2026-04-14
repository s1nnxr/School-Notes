# Spouštení na pozadí
------------------
```bash
# Spouštění na pozadí pomocí &
yes &
```
```bash
# Zobrazí běžící procesy
jobs
```
```bash
# Přesune proces do popředí
fg %1 #<- číslo procesu z jobs
```
```bash
# Poastaví proces
# Ctrl + z
kill -STOP %1
```
```bash
# Znovu spustí proces na pozadí
bg %1
```
