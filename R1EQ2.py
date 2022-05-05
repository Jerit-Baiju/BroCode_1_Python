word = 'B R O T O T Y P E'.split()
for x in range(len(word)):
    x = x + 1
    print(str(word[0:x]).replace(',','').replace("'",'').replace('[','').replace(']',''))
