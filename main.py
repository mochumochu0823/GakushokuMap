from maps.GakushokuSample import GakushokuSample
from maps.AmayasuOsusume import AmayasuOsusume

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample(), 
        AmayasuOsusume(), 
        ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(f"オススメポイント: {d.get_summary()}")
    print(f"書いた人: {d.get_author()}")
    print() 