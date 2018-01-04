import urllib
content=urllib.urlopen("https://wordpress.org/plugins/about/readme.txt") 
for line in content: 
    print (line)
