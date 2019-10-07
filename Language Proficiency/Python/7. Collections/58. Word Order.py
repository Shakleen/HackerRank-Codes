from collections import OrderedDict
words = OrderedDict()
N = int(input())

for i in range(N):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
for word in words:
    print(words[word], end=' ')