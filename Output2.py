import random

list = [{"quote": "Consummatum Es", "author": "Jose rizal"},
        {"quote": "I am you, you are me", "author": "Juan Dela Cruz"},
        {"quote": "No I am me, you are you", "author": "Hwan Dila Cruz"}]

quote = ""

while quote != "q":
    quote = input("input quote and author: ")
    split_val = quote.split(" - ")
    try:
        val = {"quote": split_val[0], "author": split_val[1]}
        list.append(val)
    except:
        print("invalid input")
    for li in list:
        print(li.get("quote"), " - ", li.get("author"))
    res = random.randint(0, len(list)-1)
    print("random quote: ", list[res].get("quote"), " - ", list[res].get("author"))

