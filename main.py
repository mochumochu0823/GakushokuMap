from maps.GakushokuSample import GakushokuSample

from maps.k25072Osusume import k25072Osusume

from maps.Gakushoku_hana import Gakushoku_hana
from maps.Gakushoku25112 import Gakushoku25112
from maps.AmayasuOsusume import AmayasuOsusume


# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [Gakushoku_hana(), 
        AmayasuOsusume(),
        Gakushoku25112(),
        k25072Osusume(),
        GakushokuSample()]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(f"オススメポイント: {d.get_summary()}")
    print(f"書いた人: {d.get_author()}")
    print() 