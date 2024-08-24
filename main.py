def have_same_letters (word1, word2):
    if sorted(word1) == sorted(word2):
        return(True)
 
thisstring = """emlco1ew
gbetord
gcaicoh
mwealxl
lhweas
tnsheep
plvhduiir
eilpan
apdailn
kpreips
"""
scrambled1 = thisstring.splitlines()
unscrambled = []
wordlist = []
wordlistpath = "C:\\Users\\USER\\downloads\\\\wordlist\\wordlist.txt"

f = open(wordlistpath)

wordlist2 = (f.read().splitlines( ))

for word1 in scrambled1:
    for word2 in wordlist2:
        if have_same_letters(word1, word2):
            unscrambled.append((word2))


final = ', '.join(unscrambled)
print(final)