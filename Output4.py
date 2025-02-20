import re
import random

list = [{"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
        {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
        {"quote": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein"},
        {"quote": "Do what you can, with what you have, where you are.", "author": "Theodore Roosevelt"},
        {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
        {"quote": "The best way to predict the future is to create it.", "author": "Peter Drucker"},
        {"quote": "Happiness depends upon ourselves.", "author": "Aristotle"},
        {"quote": "Do not go where the path may lead, go instead where there is no path and leave a trail.", "author": "Ralph Waldo Emerson"},
        {"quote": "Everything you’ve ever wanted is on the other side of fear.", "author": "George Addair"},
        {"quote": "Opportunities don't happen. You create them.", "author": "Chris Grosser"}]

while True:
    inp = input("\nWhat do you want to do? \n[1] Add new quote and author \n[2] Show the quote that you like \n[3] Search for a quote or author \n[4] Random quote \ninput: ")

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
    elif inp == "4":
        res = random.randint(0, len(list) - 1)
        print("random quote: ", list[res].get("quote"), " - ", list[res].get("author"))

    elif inp == "q":
        print("Program terminated")
        break

    else:
        print("invalid input")


