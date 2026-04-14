# Spojovej list uplná goata
# | x      | List | Spojový list|
# | Append | O(1) | O(1)        |
# | oppend | O(n) | O(1)        | <- posováme všechno o jednu pozici a vložíme na začátek
# | Insert | O(n) | O(1)        |
# | Delete | O(n) | O(1) první | <- posováme všechno o jednu pozici a smažeme první prvek
from typing import Optional, Any, TypeAlias 
