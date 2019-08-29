direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def scan(words):
    words = words.split()
    count = len(words)
    lower_words = []
    sentence = []
    for i in range(count):
        lower_words.append(words[i].lower())
    for i in range(count):
        error = False
        try:
            index = direction.index(lower_words[i])
            if(index >= 0):
                sentence.append(('direction', direction[index]))
            i = i + 1
            error = True
            continue
        except ValueError:
            error = False
        
        try:
            index = verbs.index(lower_words[i])
            if(index >= 0):
                sentence.append(('verb', verbs[index]))
            i = i + 1
            error = True
            continue
        except ValueError:
            error = False

        try:
            index = stop_words.index(lower_words[i])
            if(index >= 0):
                sentence.append(('stop', stop_words[index]))
            i = i + 1
            error = True
            continue
        except ValueError:
            error = False

        try:
            index = nouns.index(lower_words[i])
            if(index >= 0):
                sentence.append(('noun', nouns[index]))
            i = i + 1
            error = True
            continue
        except ValueError:
            error = False
        
        try:
            int(lower_words[i])
            sentence.append(('number', lower_words[i]))
            i = i + 1
            error = True
            continue
        except ValueError:
            error = False

        if(error == False):
            sentence.append(('error', words[i]))
            i = i + 1
    return sentence