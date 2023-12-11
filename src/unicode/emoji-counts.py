#!python3

import re
from defaultlist import defaultlist
from collections import defaultdict
#import unicodedata
#from jinja2 import Environment, FileSystemLoader

codepoints_cnt_hist = defaultlist(int)
zwj_codepoints_cnt_hist = defaultlist(int)
class_cnt = defaultdict(int)
count = 0

file = open('emoji-test.txt', 'r')
for line in file:
    if len(line) < 10 or line[0] == '#':
        continue

    components = re.split(r'\s+[;#]\s+(?!$)', line)
    if len(components) != 3:
        print(count, '!!', len(components), components, line)
        exit(1)

    codepoints, qualified, comment = components
    if not all([codepoints, qualified, comment]):
        print(count, '!!!', line)
        exit(1)

    match = re.match(r'(\S+) (E\d+\.\d)\s*(.+)', comment)
    if not match:
        print(count, '!!!!', codepoints, comment)
        exit(1)

    emoji, version, descr = match.groups()

    codepoints_list = codepoints.split()
    codepoints_cnt = len(codepoints_list)
    codepoints_cnt_hist[codepoints_cnt] += 1

    if codepoints_cnt == 1:
        if len(codepoints_list[0]) <= 4:
            class_cnt['BMP'] += 1
        else:
            class_cnt['SMP'] += 1
    elif '200D' in codepoints_list:
        class_cnt['ZWJ'] += 1
        zwj_codepoints_cnt_hist[codepoints_cnt] += 1
        #if codepoints_cnt == 10:
        #    print(codepoints, version, emoji, descr)
    else:
        class_cnt['COM'] += 1
        if re.match('^flag: ', descr):
            class_cnt['COM-flag'] += 1
        elif codepoints_cnt == 2 and re.search( '1F3F[BCDEF]$', codepoints):
            class_cnt['COM-skin'] += 1
        elif re.search( ' FE0F', codepoints):
            class_cnt['COM-vs16'] += 1
        else:
            print(codepoints, version, emoji, descr)

    count += 1

print(count)
print(class_cnt)
print(codepoints_cnt_hist)
print(zwj_codepoints_cnt_hist)
