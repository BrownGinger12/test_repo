import re
from re import search

list = [{"quote": "Consummatum Es", "author": "Jose rizal"},
        {"quote": "I am you, you are me", "author": "Juan Dela Cruz"},
        {"quote": "No I am me, you are you", "author": "Hwan Dila Cruz"}]

while True:
    inp = input("\nWhat do you want to do? \n[1] Add new quote and author \n[2] Show the quote that you like \n[3] Search for a quote or author \ninput: ")

    if inp == "1":
        quote = input("input quote and author: ")
        split_val = quote.split(" - ")
        try:
            val = {"quote": split_val[0], "author": split_val[1]}
            list.append(val)

            count = 1
            for li in list:
                print(count, ". ", li.get("quote"), " - ", li.get("author"))
                count += 1
            print("Quote and Author added.")
        except:
            print("invalid input")

    elif inp == "2":
        count = 1
        print("\nQuotes and Authors")
        for li in list:
            print(count, ". ", li.get("quote"), " - ", li.get("author"))
            count += 1

        select = input("\ninput the quote you want to display: ")
        try:
            split = select.split(" ")

            for sp in split:
                print(list[int(sp) - 1].get("quote"), " - ", list[int(sp) - 1].get("author"))
        except:
            print("invalid input")

    elif inp == "3":
        found = False
        search = input("Search for quote or author: ").lower()
        for li in list:
            match_auth = re.search(search, li.get("author").lower())
            match_quote = re.search(search, li.get("quote").lower())

            if match_auth or match_quote:
                print(li.get("quote"), " - ", li.get("author"))
                found = True

        if not found:
            print("No quotes or authors found")
    elif inp == "q":
        print("Program terminated")
        break

    else:
        print("invalid input")


