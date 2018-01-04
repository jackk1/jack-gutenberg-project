from collections import Counter
import string
import urllib.request
import re
import os


def getURLString():
    url = "http://www.gutenberg.org/cache/epub/10148/pg10148.txt"
    resource = urllib.request.urlopen(url)
    content = resource.read().decode()
    return content

#data = urllib.request.urlopen('http://www.gutenberg.org/files/236/236-0.txt')
#data1=str(data.read())
#file1 = open('\\Users\\bscs\\Desktop\\jack gutenberg project\\jungle_book1.txt' , "w")
#file1.write(data1)
#file1.close()

def find_between( s, first, last ):
    print(s[s.find(first)+len(fi):s.rfind(end)])
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        print('working12',first,last,'\n',s[start:end])
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

def setbook(text):
    story=dict()
    novel=dict()
    chapters=["how robin hood came to be an outlaw ","robin hood and the tinker","the shooting match at nottingham town","will stutely rescued by his companions","robin hood turns butcher ","little john goes to nottingham fair","how little john lived at the sheriff's ","little john and the tanner of blyth ","robin hood and will scarlet ","the adventure with midge the miller's son ","SHIV AND THE GRASSHOPPER","HER MAJESTY'S SERVANTS","PARADE-SONG OF THE CAMP ANIMALS","Transcriber's Notes:"]
    story[0]=text
    novel[0]=text
    for x in range(8):
        story[x+1]=find_between(text,chapters[x],chapters[x+1])
        novel[x+1]=find_between_r(text,chapters[x],chapters[x+1])
    print(story[0])
    return story,novel
        
def get_ebook_content(file):
    #file = open(file, 'r')
    #text = str(file.read())
    #file.close()
    a='PROLOGUE'
    b='*** END OF THIS PROJECT GUTENBERG EBOOK THE MERRY ADVENTURES OF ROBIN HOOD ***'
    #text=text.split('THEN I HEARD AN OLD, GRIZZLED, LONG-HAIRED CENTRAL ASIAN CHIEF ASKING QUESTIONS OF A NATIVE OFFICER',1)[0]
    #text=text.split('*** END OF THIS PROJECT GUTENBERG EBOOK THE JUNGLE BOOK ***',1)[0]
    #text=find_between(text,'The Project Gutenberg EBook of The jungle book, by Rudyard Kipling','*** END OF THIS PROJECT GUTENBERG EBOOK THE JUNGLE BOOK ***')
    text=file.split(a)[1]
    text=text.split(b)[0]
    text = "".join(l for l in text if l not in string.punctuation)
    text=text.lower()
    print(text)
    story,novel=setbook(text)
    return story,novel

content=getURLString()
#print(content)
story,novel=get_ebook_content(content)


def count_word_freq(text,words):
    word=dict()
    word['freqs'] = Counter(text.split())
    #write_list(word['freqs'])
    #print(Counter(word['freqs']).most_common(10))
    for special_words_counter in range(len(words)):
        print(word['freqs'][words[special_words_counter]])
count_word_freq(story[0],['robin','man'])
count_word_freq(story[1],['robin','man'])
print('')
count_word_freq(novel[0],['robin','man'])
count_word_freq(novel[1],['robin','man'])
print('printing',novel[1])
print('printing2',story[1])

