import json

#opening the dictionary json file in read mode
fin = open("PROJECTS/My_Dictionary/dictionary1.json", "r")
#reading the contents for json file to cont object
cont = json.load(fin)

#function to display the words that begins with a specifice letter
def dispwords():
    letter = input("Enter the letter to display that words with which it begins with: ")
    for i in cont:
        if i.startswith(letter):
            print(i)

#function to find a word and display whether its in the dictionary or not
def findword():
    word = input("Enter the word to check in the dictionary: ").lower()
    found = False
    for i in cont:
        if i == word:
            found = True
    if found == False:
        print("No such word exits in the dictionary.")
    else:
        print("It is there in the dictionary.")

#function to display the meaning
def dispm():
    word = input("Enter the word to check in the meaning of: ").lower()
    found = False
    for key, value in cont.items():
        if key == word:
            found = True
            print("{} word has meaning {}".format(key,value))
    if found == False:
        print("No such word exits.")

#function to display word-meanings for the specific word that is there in the meaning
def dispsm():
    word = input("Enter a word to be searched in the dictionay and to display the meaning there of: ")
    found = False
    for key,value in cont.items():
        if key == word or word in value:
            found == True
            print("Word {} - Meaning {}".format(key,value))
        if found == False:
            print("No such word in dictionary")

#function to search words by number of letters
def searchno():
    num = int(input("Enter number of letters of the length of the word: "))
    found == False
    for key in cont:
        if len(key) == num:
            print(key)
            found = True
    if found == False:
        print("No words with this specific length.")


#menu for interactive dictionary
while True:
    try:
        print("""
        I N T E R A C T I V E D I C T I O N A R Y
        =========================================
              
        1. Display the words that begin with a spectific letter
        2. Find a specific word
        3. Display the meaning of the specific word
        4. Display the words-meanings for the specific word that is there in the meaning
        5. Search and display words by number of letters
        6. Exit
        """)

        choice = int(input("Enter your choice of operation (1-6): "))
        if choice == 1:
            dispwords()
        elif choice == 2:
            findword()
        elif choice == 3:
            dispm()
        elif choice == 4:
            dispsm()
        elif choice == 5:
            searchno()
        elif choice == 6:
            break
        else:
            print("Invalid number! Enter any number between 1-6:")

    except:
        print("Invalid input")