import requests
import json
from word import Word, Definition, Meaning

class WordFinder:
    def __init__(self, word):
        self.word = word

    def find_opposite(self):
        w = self.find()
        if not w:
            return None
        
        return "Opposite words: " + "\n".join([k for i in w.meanings for j in i.definitions for k in j.antonyms])

    
    def find(self) -> Word:
        request_res = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + self.word)
        js = json.loads(request_res.text)
        if type(js) != list:
            return None
        data = dict(js[0])
        word = data.get('word')
        phonetic = data.get('phonetic')
        origin = data.get('origin')
        meanings = []
        for meaning_data in data.get('meanings', []):
            part_of_speech = meaning_data.get('partOfSpeech')
            definitions = []
            for definition_data in meaning_data.get('definitions', []):
                definition = definition_data.get('definition')
                example = definition_data.get('example')
                synonyms = definition_data.get('synonyms', [])
                antonyms = definition_data.get('antonyms', [])
                definitions.append(Definition(definition, example, synonyms, antonyms))
            meanings.append(Meaning(part_of_speech, definitions))

        return Word(word, phonetic, origin, meanings)
    