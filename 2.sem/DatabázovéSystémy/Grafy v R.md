snadné vykreslení
vizualne poutavé
dvě základní možnosti vykreslování
vestavěná knihovna base graphics
knihovna ggplot2

### Base Graphics
základní vestavěná knihovna pro práci s grafy


### Základní funkce 
- plot() - spojnicový graf
- barplot() - sloupcový graf
- pie() - koláčový graf
- hist() - histogram
- dotchart() - 

### Funkce plot()
- vykreslí proti sobě dva vektory (např. sloupce tabulky)
- typ grafu lze přepínat parametrem type
- popisy os dodáy automaticky dle názvů polí zadaných pro vykreslení

### Parametr type:
l - lines

### Parametry pro dodání popisků:
- main - dodání nadpisu
- xlab - popsání osy x
- ylab - popsání osy y 
- sub - caption grafu

### Barplot
- sloupcový graf
- určný pro vykreslení hodnot daných kategorií
- téměř stejné použití jako u plot
- očekává primárně výšky sloupců
- jména sloupců - jména hodnot ve vektoru


### Histogramy
- absolutní četnost zadaných hodnot v poli
- pro relativní četnost freq = FALSE

### Boxplot
- statistický graf
- každý box ukazuje základní statistiku dané kategorie
- proměnná a kategorie se zadávají jako formula
- informace o mediánu, kvartilech a odlehlých hodnotách

### Knihovna ggplot2
- knihovna určená pro práci s dataframy
- vykreslení objetků = přidání vrstev do obrázku
- komplikovanější zápis
- přiřazení hodnot pomocí funkce aes(x=,y=,color)

### Základní vrstv
- geom_point() - bodový graf
- geom_line() - spojnicový graf
- geom_histogram() - histogram



### Ukázka použití - bodový graf
- library(ggplot2)
- library(dplyr)
- iris %>% ggplot(aes(x=Sepal.Length,y=Sepal.width,color=Species)) + geom_boxplot()

### Ukázka použití - histogram
- library(ggplot2)
- library(dplyr)
- df <- read.csv("test.csv)
- df$Pclass= as.factor