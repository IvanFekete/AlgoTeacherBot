from urllib.request import urlopen
from pprint import pprint
import json

haventArticleMessage = "With possibilities: This is a redirect from a title that potentially could be expanded into a new article or other type of associated page such as a new template."

def formatLink(link) :
    return link.replace(" ", "%20")


def rebuildInfo(wikiInfo) :
    rebuildedWikiInfo = []
    try :
        rebuildedWikiInfo = [[wikiInfo[0]] + [wikiInfo[j][i] for j in range(1, 4)] for i in range(len(wikiInfo[1]))]
    except :
        return rebuildedWikiInfo
    return rebuildedWikiInfo


def getWikiInfo(token) :
    link = formatLink('https://en.wikipedia.org/w/api.php?action=opensearch&search=%s&prop=info&format=json&inprop=url' % token)
    response = json.loads(urlopen(link).read().decode("UTF-8"))
    return rebuildInfo(response)

def isLetter(c) :
    return 'a' <= c.lower() and c.lower() <= 'z'

def parseCommand(text) :
    print("parsing :", text)
    i = 0
    while i < len(text) :
        if text[i] == '/' :
            result = "/"
            i += 1
            while i < len(text) and isLetter(text[i]) :
                result += text[i]
                i += 1
            return result
        else :
            i += 1

def have(text, pattern) :
    return text.find(pattern) != -1

def aboutAlgorithms(text) :
    text = text.lower()
    result = have(text, "algorithm") or have(text, "data struct")
    if have(text, "method") and(have(text, "program") or have(text, "comp")) :
        result = True
    return result

def prepareWikiInfo(wikiInfo) :
    info = """
    %s
    Read more : %s
    """
    try:
        shortInfo = wikiInfo[2]
        wikiLink = formatLink(wikiInfo[3])
        print(shortInfo, wikiLink)
        if shortInfo == haventArticleMessage or not aboutAlgorithms(shortInfo) :
            info = ""
        else:
            info %= (shortInfo, wikiLink)
    except:
        info = ""
    print(info)
    return info

def isWord(token) :
    for c in token :
        if not isLetter(c) :
            return False
    return True

def splitIntoWords(text) :
    tokens = text.split()
    words = []
    for token in tokens :
        if isWord(token) :
            words.append(token)
    return words

def searchInfo(text) :
    print("searching : ",text)

    wikiInfo = getWikiInfo(text)
    pprint(wikiInfo)
    result = []
    for record in wikiInfo :
        if aboutAlgorithms(record[2]) :
           result.append(record)
    return result


def searchInfoBetter(text) :
    words = splitIntoWords(text)
    results = []
    for mask in range(1, 1 << len(words)) :
        bit = lambda x, i : (x >> i) & 1
        text = []
        cost = 0
        for i in range(0, len(words)) :
            if bit(mask, i) == 1 :
                text.append(words[i])
                cost += len(words[i]) ** 2
        results.append([cost, searchInfo(' '.join(text))])
