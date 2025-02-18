import random

list = [{"quote": "Consummatum Es", "author": "Jose rizal"},
        {"quote": "I am you, you are me", "author": "Juan Dela Cruz"},
        {"quote": "No I am me, you are you", "author": "Hwan Dila Cruz"}]

while True:
    quote = input("input quote and author: ")
    split_val = quote.split(" - ")
    print()
    val = {"quote": split_val[0], "author": split_val[1]}
    list.append(val)
    for li in list:
        print(li.get("quote"), " - ", li.get("author"))
    res = random.randint(0, len(list))
    print(list[res-1].get("quote"), " - ", list[res-1].get("author"))

