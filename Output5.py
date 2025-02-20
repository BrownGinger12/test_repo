import re
import random

dict_list = [{"author": "Steve Jobs", "quotes": ["test1 quote", "test2 quote"]},
             {"author": "Steve Bobs", "quotes": ["test1 quote1", "test2 quote2"]}]

while True:
    inp = input(
        "\nWhat do you want to do? \n[1] Add new quote and author \n[2] Show the quote that you like \n[3] Search for a quote or author\n[4] Delete quote or author \ninput: ")

    if inp == "1":
        quote = input("input quote and author: ")
        split_val = quote.split(" - ")
        try:
            found_author = False
            for li in dict_list:
                match_auth = re.search(split_val[1].lower(), li.get("author").lower())
                if match_auth:
                    li["quotes"].append(split_val[0])
                    found_author = True

            if not found_author:
                new_auth = {"author": split_val[1], "quotes": [split_val[0]]}
                dict_list.append(new_auth)

            for li in dict_list:
                print("Author: ", li["author"], "\nQuotes: ")
                for qu in li["quotes"]:
                    print(qu)
                print("\n")

            print("Quote and Author added.")
        except:
            print("invalid input")

    elif inp == "2":
        count = 1
        print("\nQuotes and Authors")
        for li in dict_list:
            print("Author: ", li["author"], "\nQuotes: ")
            for qu in li["quotes"]:
                print(qu)
            print("\n")
            count += 1

        select = input("input author: ")

        found_author = False
        author_index = 0

        for li in dict_list:
            match_auth = re.search(select, li.get("author").lower())
            if match_auth:
                found_author = True
                counter = 1
                for qu in li["quotes"]:
                    print(counter, ". ", qu)
                    counter += 1
                break
            author_index += 1

        if not found_author:
            print("Author does not exist")

        select_quote = input("Select quote: ")

        try:
            split = select_quote.split(" ")

            for sp in split:
                print(dict_list[author_index].get("quotes")[int(sp) - 1])
        except:
            print("invalid input")

    elif inp == "3":
        found = False
        search = input("Search for quote or author: ").lower()
        for li in dict_list:
            match_auth = re.search(search, li.get("author").lower())

            if match_auth:
                print("author: ", li.get("author"), "\nquotes: ")
                for qu in li["quotes"]:
                    print(qu)
                found = True

            for qu in li["quotes"]:
                match_quote = re.search(search, qu.lower())
                if match_quote:
                    print("\nauthor: ", li.get("author"), "\nquote: ", qu)
                    found = True

        if not found:
            print("No quotes or authors found")
    elif inp == "4":
        count = 1
        print("\nQuotes and Authors")
        for li in dict_list:
            print("Author: ", li["author"], "\nQuotes: ")
            for qu in li["quotes"]:
                print(qu)
            print("\n")
            count += 1

        select_opt = input("What do you want to delete? [1] Author [2]Quote: ")

        if select_opt == "1":
            auth_del = input("Enter author's full name: ")
            found = False

            counter = 0
            for li in dict_list:
                if li.get("author").lower() == auth_del.lower():
                    dict_list.remove(li)
                    print("Author deleted")
                    found = True
                    break
                counter += 1

            if not found:
                print("Author does not exist")

        elif select_opt == "2":
            found = False
            quote_count = 1
            print("\nQuotes and Authors")
            for li in dict_list:
                print("Author: ", li["author"], "\nQuotes: ")
                for qu in li["quotes"]:
                    print(quote_count, ". ", qu)
                    quote_count += 1
                print("\n")

            quote_del = int(input("Enter quote number to delete: ")) - 1

            del_count = 0

            if del_count >= 0 and del_count <= quote_count:
                for li in dict_list:
                    for qu in li["quotes"]:
                        if del_count == quote_del:
                            li["quotes"].remove(qu)
                            print("Quote deleted")
                            found = True
                            break
                        del_count += 1
                    print("\n")
                if not found:
                    print("Quote does not exist")

            else:
                print("Quote does not exist")
        else:
            print("invalid input")
    elif inp == "q":
        print("Program terminated")
        break

    else:
        print("invalid input")


