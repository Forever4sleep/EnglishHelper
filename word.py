class Phonetic:
    def __init__(self, text, audio=None):
        self.text = text
        self.audio = audio

class Definition:
    def __init__(self, definition, example, synonyms=None, antonyms=None):
        self.definition = definition
        self.example = example
        self.synonyms = synonyms or []
        self.antonyms = antonyms or []

    def __str__(self):
        return self.definition

class Meaning:
    def __init__(self, part_of_speech, definitions):
        self.part_of_speech = part_of_speech
        self.definitions = definitions
    
    def __str__(self):
        return "🙌 Part of speech: " + self.part_of_speech + ":\n" + " ".join([f"{i + 1}) {'*'+str(self.definitions[i])+'*'}\n" for i in range(min(len(self.definitions), 5))])

class Word:
    def __init__(self, word, phonetic, origin, meanings):
        self.word = word
        self.phonetic = phonetic
        self.origin = origin
        self.meanings = meanings
    
    def __str__(self):
        phonetics_str = self.phonetic
        meanings_str = "\n".join([str(meaning) for meaning in self.meanings])
        return f"Word: {self.word}\nPhonetic: {phonetics_str}\nOrigin: {self.origin}\nMeanings:\n{meanings_str}"

    