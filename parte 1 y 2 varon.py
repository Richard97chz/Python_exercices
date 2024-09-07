def toLowerCase(text):
    lowerCase = text.lower()
    return lowerCase


def cleanText(textLower):
    cleanedText = textLower.replace(',', ' ').replace('.', ' ')
    separatedText = cleanedText.split(" ")
    return separatedText


def countWords(cleanedText):
    dictionary = {}
    for word in cleanedText:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar."

lowerCase = toLowerCase(text)
cleanedText = cleanText(lowerCase)
countedWords = countWords(cleanedText)

print(countedWords)
