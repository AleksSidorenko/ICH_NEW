# Verwenden Sie collections.Counter, um die Anzahl jedes Zeichens in einer Zeichenkette zu z√§hlen.
# Schreiben Sie eine Funktion count_characters, die eine Zeichenkette annimmt und ein
# Counter-Objekt mit der Anzahl der einzelnen Zeichen zur√Љckgibt.
# Geben Sie anschlie√Яend die 3 am h√§ufigsten vorkommenden Zeichen aus.

from collections import Counter


def count_characters(symbols):
    symbol_counter = Counter(symbols)
    return symbol_counter.most_common(3)


user_input = "Hallo world"

print(count_characters(user_input))

#



from collections import deque


def fixed_queue(data, max_l):
    queue = deque(maxlen=max_l)
    for num in data:
        queue.append(num)
    return list(queue)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_length = 5
print(fixed_queue(numbers, max_length))

#


from collections import defaultdict


def group_by_first_letter(words: list) -> dict:
    groups = defaultdict(list)


from collections import defaultdict


def group_by_first_letter(words: list) -> dict:
    groups = defaultdict(list)
    for word in words:
        groups[word[0]].append(word)

    return groups


words = ['abs', 'bnm', 'dsf', 'ads', 'boss']

grouped = group_by_first_letter(words)

print(grouped)


#

import math
from collections import namedtuple

coord_dict = namedtuple('Point', ['x', 'y', 'z'])


def calculate_distance(point1, point2):
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2 + (point2.z - point1.z) ** 2)


point1 = coord_dict(45, 56, 64)
point2 = coord_dict(56, 65, 77)

print(calculate_distance(point1, point2))