#!python3

import re
import unicodedata
from jinja2 import Environment, FileSystemLoader

zwj_sequences = []

file = open('emoji-sequences.txt', 'r')
for line in file:
    if len(line) < 10 or line[0] == '#':
        continue

    code_points, type_field, description = re.split(r'\s*;\s*', line)
    description, comment = re.split(r'\s*#\s*', description)
    match = re.match(r'(E\d+\.\d)\s*\[1\] \((.+?)\)', comment)
    if not match:
        print('!!!!', code_points, comment)
        exit(1)

    version, combined_emoji = match.groups()

    #print(code_points, version, combined_emoji, sep = "\t")
    zwj_sequences.append({
        "code_points" : code_points,
        "codepoints" : '<br/>'.join([f'<b>{code}</b>: { unicodedata.name(chr(int(code, base=16))) }' for code in code_points.split()]),
        "decomposed" : ''.join([f'&#x{code};' if code != '200D' else '&#x299A;' for code in code_points.split()]),
        "version" : version,
        "combined_emoji" : combined_emoji,
        "description" : description,
    })


# Загружаем шаблоны из текущей директории
env = Environment(loader=FileSystemLoader('.'))

# Загружаем шаблон multiplication_table.html
template = env.get_template('zwj_table_tmpl.html')

# Рендерим шаблон с нашей таблицей умножения
rendered_template = template.render( zwj_sequences = zwj_sequences )
print(rendered_template)
