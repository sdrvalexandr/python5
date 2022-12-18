def fileWrite():
    path = 'coding.txt'
    text = input('Введите текст: ')
    data = open(path, 'a')
    open(path, 'w').close()
    data.write(text + '\n')
    data.close()

def coding():
    path = 'coding.txt'
    data = open(path, 'r')
    txt = data.readline()
    data.close()
    print('txt: ', txt)
    codingTXT = ''
    count = 0
    i = 0
    char = txt[0]
    while i < len(txt):
        if char == txt[i]:
            count += 1
        else:
            codingTXT = codingTXT + str(count) + char
            count = 1
            char = txt[i]
        i = i + 1
    codingTXT = codingTXT + str(count) + char
    codingTXT = codingTXT.replace(codingTXT[len(codingTXT) - 2],'')
    print(codingTXT)
    data = open(path, 'a')
    data.write(codingTXT)
    data.close()

def decoding():
    path = 'coding.txt'
    data = open(path, 'r')
    fileText = data.readlines()
    txtForDecoding = fileText[1]
    print('----------------------------')
    print('txt for decoding',txtForDecoding)
    data.close()
    decodedString = ''
    charCount = ''
    for i in range(len(txtForDecoding)):
        if not txtForDecoding[i].isalpha():
            charCount += txtForDecoding[i]
        else:
            decodedString = decodedString + txtForDecoding[i] * int(charCount)
            charCount = ''
    print(decodedString)
    data = open(path, 'a')
    data.write(decodedString)
    data.close()

fileWrite()
coding()
decoding()