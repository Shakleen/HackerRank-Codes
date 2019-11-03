n, m = map(int, input().split())
person_knowledge = [input() for _ in range(n)]
knowledge_level = {}
max_knowledge_level = -1

for i in range(n):
    for j in range(i+1, n):
        no_i = int(eval('0b' + person_knowledge[i]))
        no_j = int(eval('0b' + person_knowledge[j]))
        total = no_i | no_j
        max_knowledge_level = max(max_knowledge_level, total)
        knowledge_level[total] = knowledge_level.get(total, 0) + 1

max_known = len([bit for bit in bin(max_knowledge_level)[2:] if bit == '1'])
print(max_known)

teams = knowledge_level[max_knowledge_level]
print(teams)