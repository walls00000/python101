alienWords = {}
alienWords["we"] = "dwerl"
alienWords["come"] = "forze"
alienWords["in"] = "pak"
alienWords["peace"] = "schnerl"
while True:
    toBeTranslated = input("Enter a word or phrase: ")
    translated = []
    wordList = toBeTranslated.lower().split()
    for word in wordList:
        if word in alienWords:
            translated.append(alienWords[word])
        else:
            print("Unknown word ", word)
            yn = input("Would you like to add a new translation? (y/n) ")
            if (yn == "y"):
                print("Adding translation for ", word)
                newTranslation = input("Enter the translation: ")
                print("Adding ", word, "=", newTranslation)
                alienWords[word] = newTranslation
                translated.append(alienWords[word])
            else:
                translated.append(word)
            
    print("Translated: ", " ".join(translated))
        