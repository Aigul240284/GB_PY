name = input('Your name: ')
score = input('Your score: ')
try:
    scores = open("scores.txt")
except (OSError, IOError):
    scores = open('scores.txt', 'w')
    scores.write('1. AAA 1000\n2. CCC 700\n3. BBB 200')
    scores.close()
    scores = open("scores.txt")
scores = open("scores.txt")
content = ['{} {}'.format(s.split()[1],
                          s.split()[2]) for s in scores.read().split('\n')]
scores.close()
content.append('{} {}'.format(name, score))
content.sort(key=get_key, reverse=True)
def get_key(item):
    return int(item.split()[1])
text = '\n'.join(['{}. {}'.format(i, item) for i, item in enumerate(content[:10], start=1)])
text = ''
for i, item in enumerate(content[:10], start=1):
    text += '{}. {}\n'.format(i, item)
print(text)
scores = open("scores.txt", 'w')
scores.write(text)
scores.close()    
                 