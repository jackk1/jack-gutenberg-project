from collections import Counter
import string
import urllib.request
import re
import os



def getURLString():
    url = "http://www.gutenberg.org/cache/epub/35997/pg35997.txt"
    resource = urllib.request.urlopen(url)
    content = resource.read().decode()
    return content

def find_between( s, first, last ):
    return (s[s.find(first)+len(first):s.rfind(last)])
    #try:
        #start = s.index( first ) + len( first )
        #end = s.index( last, start )
        #print('working12',first,last,'\n',s[start:end])
        #return s[start:end]
    #except ValueError:
        #return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

def setbook(text):
    story=dict()
    #chapters=["how robin hood came to be an outlaw ","robin hood and the tinker","the shooting match at nottingham town","will stutely rescued by his companions","robin hood turns butcher ","little john goes to nottingham fair","how little john lived at the sheriff's ","little john and the tanner of blyth ","robin hood and will scarlet ","the adventure with midge the miller's son ","SHIV AND THE GRASSHOPPER","HER MAJESTY'S SERVANTS","PARADE-SONG OF THE CAMP ANIMALS","Transcriber's Notes:"]
    chapters=["MOWGLIS BROTHERS","HUNTING-SONG OF THE SEEONEE PACK","KAAS HUNTING","ROAD-SONG OF THE BANDAR-LOG","TIGER! TIGER!","MOWGLI'S SONG","THE WHITE SEAL","LUKANNON","RIKKI-TIKKI-TAVI","DARZEE'S CHAUNT"," TOOMAI OF THE ELEPHANTS","SHIV AND THE GRASSHOPPER","HER MAJESTY'S SERVANTS","PARADE-SONG OF THE CAMP ANIMALS","Transcriber's Notes:"]
    story[0]=text
    for i in range(0, len(chapters)):
        chapters[i] = chapters[i].lower()
        chapters[i] = "".join(l for l in chapters[i] if l not in string.punctuation)
    #print('printing1',chapters)
    for x in range(len(chapters)-1):
        story[x+1]=find_between(text,chapters[x],chapters[x+1])
    print(story[0])
    return story
        
def get_ebook_content(file):
    #file = open(file, 'r')
    #text = str(file.read())
    #file.close()
    a='_Night-Song in the Jungle._'
    b='*** START OF THIS PROJECT GUTENBERG EBOOK THE JUNGLE BOOK ***'
    #text=text.split('THEN I HEARD AN OLD, GRIZZLED, LONG-HAIRED CENTRAL ASIAN CHIEF ASKING QUESTIONS OF A NATIVE OFFICER',1)[0]
    #text=text.split('*** END OF THIS PROJECT GUTENBERG EBOOK THE JUNGLE BOOK ***',1)[0]
    #text=find_between(text,'The Project Gutenberg EBook of The jungle book, by Rudyard Kipling','*** END OF THIS PROJECT GUTENBERG EBOOK THE JUNGLE BOOK ***')
    text=file.split(a)[1]
    text=text.split(b)[0]
    text = "".join(l for l in text if l not in string.punctuation)
    text=text.lower()
    print(text)
    story=setbook(text)
    return story

content=getURLString()
#print(content)
story=get_ebook_content(content)


def count_word_freq(text,words):
    word=dict()
    word['freqs'] = Counter(text.split())
    #write_list(word['freqs'])
    print(Counter(word['freqs']).most_common(100))
    for special_words_counter in range(len(words)):
        print(word['freqs'][words[special_words_counter]])
count_word_freq(story[0],['bear','man'])
count_word_freq(story[6],['bear','man'])
print('')
#print('printing',story[2])

