import string

def split_bag_in_half(bag: str):
    m = len(bag) // 2
    return bag[:m], bag[m:]

def get_bag_size(bag):
    left_compartment, right_compartment = split_bag_in_half(bag)
    intersection = set(left_compartment) & set(right_compartment)
    if intersection:
        article = list(intersection)[0]
        return string.ascii_letters.index(article) + 1
    return 0

def get_grouped_bags_size(bags):
    i, j, k = bags
    intersection = set(i) & set(j) & set(k)
    if intersection:
        article = list(intersection)[0]
        return string.ascii_letters.index(article) + 1
    return 0


with open('data.txt', encoding='utf-8') as f:
    bags = [bag.replace('\n', '') for bag in f.readlines() if bag.replace('\n', '')]
    bags_grouped = zip(*(iter(bags),) * 3)
    bags_sizes = [get_bag_size(bag) for bag in bags]
    print(sum(bags_sizes))
    bags_grouped_sizes = [get_grouped_bags_size(group) for group in bags_grouped]
    print(sum(bags_grouped_sizes))
