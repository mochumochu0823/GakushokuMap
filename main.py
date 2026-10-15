from maps.GakushokuSample import GakushokuSample

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample(), ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(f"オススメポイント: {d.get_summary()}")
    print(f"書いた人: {d.get_author()}")
    print()