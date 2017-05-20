import telebot, config, helper

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
def handle_category(message) :
    print(message.chat.id, "command : category", "text : %s" % message.text)
    command = helper.parseCommand(message.text)
    keyboard = config.categoriesInlineKeyboardMarkup[command]
    bot.send_message(chat_id = message.chat.id, text = "Select an algorithms that you need :\n",  reply_markup = keyboard)


@bot.callback_query_handler(func=lambda call : True)
def handle_callback_query(call) :
    print(call.message.chat.id, "command : callback", "type : %s" % call.data)

    directory = call.data
    categoryName, algorithmName = directory.split("/")
    implementationLink = helper.formatLink("https://github.com/PetarV-/Algorithms/tree/master/%s" % (directory + ".cpp"))
    wikiInfo = helper.getWikiInfo(algorithmName)
    print(wikiInfo)
    info = helper.prepareWikiInfo(wikiInfo[0])
    messageText = """ %s : %s
    %s
    Implementation : %s
    """ % (categoryName, algorithmName, info, implementationLink)

    bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = messageText)

@bot.message_handler(func = lambda message : True)
def searchByText(message) :
    messageText = helper.prepareWikiInfo(helper.searchInfo(message.text))
    if messageText == "" :
        messageText = "Cannot find algorithm or data structure that you want."
    bot.send_message(chat_id = message.chat.id, text = messageText)

if __name__ == "__main__" :
    bot.polling()