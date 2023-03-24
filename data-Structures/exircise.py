from pprint import pprint
sentence ="This is a common interview question"
char_frequencsy ={
}

for char in sentence:
    if char in char_frequencsy:
        char_frequencsy[char] += 1
    else:
        char_frequencsy[char] = 1


pprint(sorted( char_frequencsy.items(),key=lambda kv:kv[1],reverse=True))