from urllib.request import urlopen
import json
haventArticleMessage = "With possibilities: This is a redirect from a title that potentially could be expanded into a new article or other type of associated page such as a new template."

def formatLink(link) :
    return link.replace(" ", "%20")

def getWikiInfo(token) :
    link = formatLink('https://en.wikipedia.org/w/api.php?action=opensearch&search=%s&prop=info&format=json&inprop=url' % token)
    response = json.loads(urlopen(link).read().decode("UTF-8"))
    return response