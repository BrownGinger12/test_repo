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

        count = 1
        for li in list:
            print(count, ". ", li.get("quote"), " - ", li.get("author"))
            count += 1

        select = input("input the quote you want to display: ")
        split = select.split(" ")

        for sp in split:
            print(list[int(sp)-1].get("quote"), " - ", list[int(sp)-1].get("author"))

    except:
        if quote == "q":
            print("Program terminated")
        else:
            print("invalid input")


