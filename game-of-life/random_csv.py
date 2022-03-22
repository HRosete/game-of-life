import csv

import random
import sys

all_list = []
# columns = 10
# rows = 10
# for x in range(rows):
#     a_list = []
#     for i in range(columns):
#         a_list.append(str(random.randint(0, 1)))
#     values = ",".join(str(i) for i in a_list)
#     print(values)
#     all_list.append(a_list)

# sys.stdout = open('random_num.csv', 'w')
# for a_list in all_list:
#     print(", ".join(map(str, a_list)))

rows = 10
columns = 10

for _ in range(rows):
    line = []
    for _ in range(columns):
        line.append(random.randint(0, 1))
    all_list.append(line)

print(all_list)
