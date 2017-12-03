def find_last_letter(string):
    count = 0
    for letter in string:
        count +=1
    print("Total number of letter in the string is",count)
    letter = string[-1]
    print("Last letter of the string is",letter)
find_last_letter("Mahaballeswaram")

