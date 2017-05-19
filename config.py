import os
from telebot import types
TOKEN = "397605652:AAEvceq-GSOpiiAH6yu3fGqkYO4qQiZWGJg"

categoriesList = ["/sorting", "/searching"]

def formSortingButton() :
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text = "Bubble Sort", callback_data = "/bubblesort"))
    return keyboard

categoriesInlineKeyboardMarkup = {
    "/sorting" : formSortingButton()
}



startMessage = """ Hi, I'm a AlgoTeacher bot. I will help you to know something about the most common algorithms. 
Please enter a name of an  algorithm or choose the category from this list :
%s
""" % ',\n'.join(categoriesList)

helpMessage = """ This bot can help you to know something about the most common algorithms. 
/start - start to work with me
/help - get a help information about me
Commands for categories :
%s
""" % ',\n'.join(categoriesList)
