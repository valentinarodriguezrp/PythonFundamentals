# CodeAlongTranslatePirate.py

english_pirate_dict = {
    "hello": "ahoy",
    "to": "ta",
    "was": "be",
    "cheat": "hornswaggle",
    "cheating": "hornswaggle'n",
    "toilet": "head",
    "hi": "yo-ho-ho",
    "man": "matey",
    "pardon": "avast",
    "excuse": "arrrgh",
    "yes": "aye",
    "my": "me",
    "friend": "matey",
    "drunk": "three sheets to the wind",
    "food":"grub",
    "nose":"prow",
    "leave":"weigh anchor",
    "cheat":"hornswaggle",
    "forward":"fore",
    "child":"sprog",
    "children":"sprogs",
    "sailor":"swab",
    "lean":"careen",
    "find":"come across",
    "mother":"dear ol mum, bless her black soul",
    "drink":"barrel o rum",
    "of":"o", "there":"thar",
    "my":"me", "mine":"me",
    "gun": "cannon",
    "monkey": "tailed imp",
    "expert": "old smartly",
    "flag": "Jolly Roger",
    "dad": "capn",
    "teacher": "wise sage",
    "phone": "cursed device",
    "computer": "magic box",
    "speak": "parley",
    "person": "landlubber",
    "people": "landlubbers",
    "sir": "matey",
    "hotel": "fleabag",
    "student": "swabbie",
    "boy": "matey",
    "professor": "foul blaggart",
    "restaurant": "galley",
    "students": "swabbies",
    "bathroom": "head"
}

# translateWord translates a single word from English into Pirate
# parameter: word
# return: the pirate version of the word or the original word if it doesn't exist in the dictionary
def translateWord(word):
    word = word.lower()
    if word in english_pirate_dict:
        return english_pirate_dict[word]
    else:
        return word

# translateSentence: take an English sentence and return the Pirate sentence
# parameter: sentence
# return sentence in Pirate
def translateSentence(sentence):
    pirateSentence = ""
    words = sentence.split()
    for i in words:
        i = translateWord(i)
        pirateSentence += i + " "
    return pirateSentence.strip().capitalize() + "."


sentence = ""
while sentence.lower() != "q" and sentence.lower() != "quit":
    sentence = input("Enter the phrase you wish to translate into pirate, or (q)quit: ")
    if sentence.lower() not in ["q", "quit"]:
        print(translateSentence(sentence))
