word = input('')

if not word.isdigit():
    
    first_letter = word[0]
    numbers = str(len(word) -2)
    last_letter = word[len(word) -1]

    short_word = first_letter + numbers + last_letter

    if len(word) <= 10:
        print(word)
    else:
        print(short_word)