def count_words():
    with open("book.txt", "r") as file:
        count = 0
        lines = file.readlines()

        for word in lines:
            val = word.strip().split(',')

            for w in val:
                # w = w.strip()
                # if w[-1] == 'e':
                if w.endswith('e'):
                    count += 1
                    # print(count)
                    print(w)
        print(f"the total count of words ending with e is : {count}")


count_words()
