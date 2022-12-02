import heapq

with open('data.txt', encoding='utf-8') as f:
    section = [x for x in f.read().split('\n\n')]
    sum_per_section =  [sum([int(y) for y in x.split('\n') if y]) for x in section]
    print(max(sum_per_section))
    print(sum(heapq.nlargest(3, sum_per_section)))
