import telebot
import config
import replies
from spellchecker import SpellChecker
from word_finder import WordFinder
from ai_helper import LanguageAIHelper

bot = telebot.TeleBot(config.TOKEN, parse_mode=None)
helper = LanguageAIHelper()

@bot.message_handler(commands=["define"])
def define_word(message):
	word = message.text.split()[1]
	x = WordFinder(word).find()
	if not x:
		bot.send_message(message.chat.id, replies.WORD_NOT_FOUND)
		return
      
	bot.send_message(message.chat.id, str(x), parse_mode='Markdown')
	bot.send_message(message.chat.id, replies.USE_IN_SENTENCE)


@bot.message_handler(commands=["check"])
def spell_check(message):
	word = " ".join(message.text.split()[1::])
	bot.send_message(message.chat.id, replies.PROCESSING)
	bot.send_message(message.chat.id, helper.check_sentence(word))


@bot.message_handler(commands=["details", "detail", "info"])
def more_detail_for_word(message):
	msg = message.text.split()
	if len(msg) > 2:
		bot.send_message(message.chat.id, replies.ONE_WORD)
		return
	
	word = msg[1]
	bot.send_message(message.chat.id, replies.PROCESSING)
	bot.send_message(message.chat.id, helper.give_info_for_word(word))

@bot.message_handler(commands=["translate"])
def translate(message):
	msg = message.text.split()
	if len(msg) < 3:
		bot.send_message(message.chat.id, replies.SENTENCE)
		return
	
	sentence = " ".join(msg[1::])
	bot.send_message(message.chat.id, replies.PROCESSING)
	bot.send_message(message.chat.id, helper.translate_sentence(sentence))


@bot.message_handler(commands=["commands", "help"])
def help(message):
	bot.send_message(message.chat.id, replies.COMMANDS)


@bot.message_handler(commands=["game"])
def game(message):
	request = message.text.split()
	if len(request) != 2:
		bot.send_message(message.chat.id, replies.LEVEL_NOT_GIVEN)
		return
	if not request[1].isnumeric():
		bot.send_message(message.chat.id, replies.LEVEL_NOT_GIVEN)
		return
	level = int(request[1])
	if level < 1 or level > 3:
		bot.send_message(message.chat.id, replies.LEVEL_NOT_GIVEN)
		return
	
	bot.send_message(message.chat.id, replies.PROCESSING_GAME)
	origin = helper.generate_sentence(level)

	bot.send_message(message.chat.id, origin)
	bot.send_message(message.chat.id, replies.TRANSLATE)
	bot.register_next_step_handler(message, game_followup, origin)


def game_followup(message, origin):
	translation = message.text
	bot.send_message(message.chat.id, helper.check_translation(origin, translation))

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.infinity_polling()