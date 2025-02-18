import random

list = ["Consummatum Es - Jose rizal",
        "I am you, you are me - Juan Dela Cruz",
        "No I am me, you are you - Hwan Dila Cruz"]
quote = ""

while quote != "q":
    quote = input("input quote and author: ")
    list.append(quote)
    for li in list:
        print(li)
    res = random.randint(0, len(list ) -1)
    print(list[res])