import telebot, config

bot = telebot.TeleBot(config.TOKEN)

print("Bot is initialized")

@bot.message_handler(commands=["start"])
def handle_start(message) :
    print(message.chat.id, "command : /start")
    bot.send_message(message.chat.id, config.startMessage)

@bot.message_handler(commands=["help"])
def handle_help(message) :
    print(message.chat.id, "command : /help")
    bot.send_message(message.chat.id, config.helpMessage)

@bot.message_handler(commands=[s[1:] for s in config.categoriesList])
def hanndle_category(message) :
    print(message.chat.id, "command : category")
    bot.send_message(chat_id = message.chat.id, text = "Select an algorithms that you need :\n",  reply_markup = config.categoriesInlineKeyboardMarkgrup[message.text])


bot.polling()