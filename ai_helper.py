from llamaapi import LlamaAPI
import json
import config
import os

class LanguageAIHelper:
    def __init__(self, model='llama-13b-chat'):
        self.__llama = LlamaAPI(config.AI_TOKEN)
        self.__model = model

    def check_sentence(self, sentence: str) -> str:
        api_request_json = {
        "model": self.__model,
            "messages": [
                {"role": "system", "content": "You are a highly qualified English teacher, you are going to provide help to learners."},
                {"role": "user", "content": "Check if this sentence has any grammar mistakes, if it does, correct the sentence and explain your reasoning" + sentence},
            ]
        }
        response = self.__llama.run(api_request_json)
        r = dict(json.loads(json.dumps(response.json())))
        answer = r['choices'][0]['message']['content']

        return answer
    
    def give_info_for_word(self, word: str) -> str:
        api_request_json = {
        "model": self.__model,
            "messages": [
                {"role": "system", "content": "You are a highly qualified English teacher, you are going to provide help to learners."},
                {"role": "user", "content": "Find antonyms, synonyms (providing their meaning and example of usage) for the word " + word},
            ]
        }
        response = self.__llama.run(api_request_json)
        r = dict(json.loads(json.dumps(response.json())))
        answer = r['choices'][0]['message']['content']

        return answer
    
    def translate_sentence(self, sentence: str) -> str:
        api_request_json = {
        "model": self.__model,
            "messages": [
                {"role": "system", "content": "You are a highly qualified English teacher, you are going to provide help to learners."},
                {"role": "user", "content": "Translate this sentence to Russian, do not write anything else other than the translation: " + sentence},
            ]
        }
        response = self.__llama.run(api_request_json)
        r = dict(json.loads(json.dumps(response.json())))
        answer = r['choices'][0]['message']['content']

        return answer

    def generate_sentence(self, level: int) -> str:
        equivalent = ''
        if level == 1:
            equivalent = 'B1'
        if level == 2:
            equivalent = 'B2'
        if level == 3:
            equivalent = 'C1/C2'

        api_request_json = {
        "model": self.__model,
            "messages": [
                {"role": "system", "content": "You are about to play a game: you need to come up with unique sentences for the user to translate, do not write anything else except for the generated sentence"},
                {"role": "user", "content": "Form a random unique sentence on one of these topics: IT, Math, Science, Psychology, in English for " + equivalent + " learners that you have not generated before. Do not write anything else except for the sentence. Example of answer: Hello, this is a simplte sentence"},
            ]
        }
        response = self.__llama.run(api_request_json)
        r = dict(json.loads(json.dumps(response.json())))
        answer = r['choices'][0]['message']['content']

        return answer
    
    def check_translation(self, origin, tr: int) -> str:
        api_request_json = {
        "model": self.__model,
            "messages": [
                {"role": "system", "content": "You are a translator, you need to check the correctness of a translation provided by user, give feedback on the translation and do not say anything else"},
                {"role": "user", "content": "Check if this sentence: '" + origin + "'" + " is translated to Russian correctly: " + tr + ". Answer following this form: original sentence, user translation, feedback on the translation on a scale of 1 to 10"},
            ]
        }
        response = self.__llama.run(api_request_json)
        r = dict(json.loads(json.dumps(response.json())))
        answer = r['choices'][0]['message']['content']

        return answer