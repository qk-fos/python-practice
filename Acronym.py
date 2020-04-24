#Simple Acronym Program

phrase = input("Enter a phrase for the acronym: ")
acronym = phrase.upper().split()
for word in acronym:
    print(word[0], end='')  #random access memory