def all_variant(text):
    j = 0
    while j <= len(text):
        i = 0
        while i >= 0 and i <= (len(text) - j):
            yield text[i:i+j]
            i += 1
        j += 1


k =  all_variant('abcd')
for i in k:
    print (i)