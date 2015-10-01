__author__ = 'FarzanehOrak'

key = "abcdefghijklmnopqrstuvwxyz"
sentence = "Hello Dear it is time to shine"
for char in key:
    count = sentence.count(char)
    if count >= 1:
        print(char , ": " ,count)

