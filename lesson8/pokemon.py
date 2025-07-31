import pypokedex
# pokemon_all = pypokedex.get(name="pikachu", all=True)
# 查詢皮卡丘
pokemon = pypokedex.get(name="pikachu")
# 顯示皮卡丘的基本資訊
# pypokedex.
print("名稱：", pokemon.name)
print("屬性：", [t for t in pokemon.types])
print("體重：", pokemon.weight)
print("身高：", pokemon.height)


# pokemon_list = [
#     {"編號": 1, "名稱": "妙蛙種子", "屬性": ["草", "毒"]},
#     {"編號": 4, "名稱": "小火龍", "屬性": ["火"]},
#     {"編號": 7, "名稱": "傑尼龜", "屬性": ["水"]},
#     {"編號": 25, "名稱": "皮卡丘", "屬性": ["電"]},
#     {"編號": 39, "名稱": "胖丁", "屬性": ["一般", "妖精"]},
#     # ...可自行增加更多
# ]

# for p in pokemon_list:
#     print(f"{p['編號']:>3} {p['名稱']} 屬性: {', '.join(p['屬性'])}")
