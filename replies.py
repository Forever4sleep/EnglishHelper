USE_IN_SENTENCE = "💡 New knowledge is retained better if it is used! Try using this word in a sentence, don't worry about making mistakes, I will correct you!"
WORD_NOT_FOUND = "Unfortunately, I wasn't able to find the word you requested, did you meaning something else?"
PROCESSING = "Processing..."
PROCESSING_GAME = "Processing... After sentence is generated, you will have to provide translation for it in Russian"
LEVEL_NOT_GIVEN = "You should have provided the level of difficulty (1/2/3)"
TRANSLATE = "Now translate the sentence to Russian!"
ONE_WORD = "Give exactly one word!"
RESPONSE_DICT = {
		"/define": "Define word (дать определение слову, его часть речи и т.д.)",
		"/check": "Check if sentence is correct (определить, верно ли составлено предложение)",
		"/details, /detail, /info": "Provide antonyms, synonyms for word with examples (определить антонимы и синонимы слова с примерами)",
		"/translate": "Translate sentence to Russian (перевести предложение на русский язык)",
		"/game (level from 1 to 3)": "Play a game with the bot by translating sentences from English to Russian (игра, в которой вам надо переводить сгенерированные предложения на русский язык)"
	}
COMMANDS = "\n".join([key + " - " + value for key, value in RESPONSE_DICT.items()])
SENTENCE = "You should have provided a sentence"