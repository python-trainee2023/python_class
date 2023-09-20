user_word=str(input("please enter a word:: "))
rev=user_word[::-1]
if user_word==rev:
    print("it is a palindrome where ",user_word, "is equal to the reversed ",rev)
elif user_word!=rev:
    print("it is not a palindrome where ", user_word, "is not equal to the reversed", rev)
else:
    print("please provide a better word")
