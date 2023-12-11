import unicodedata as ud

ud.unidata_version
# '15.0.0'

# == lookup

ud.lookup('LATIN SMALL LETTER A')
# 'a'

ud.lookup('ROMAN NUMERAL EIGHT')
# 'Ⅷ'

ud.lookup('BLACK CHESS KNIGHT')
# '♞'

ud.lookup('GRINNING FACE')
# '😀'

# == name, category

ud.category(c), ud.name("\u0bf2")
# ('So', 'TAMIL NUMBER ONE THOUSAND')

for c in "\u00E9\u0bf2\u0f84\u1770\u33af":
    print('%04x' % ord(c), ud.category(c), ud.name(c))

# 00e9 Ll LATIN SMALL LETTER E WITH ACUTE
# 0bf2 No TAMIL NUMBER ONE THOUSAND
# 0f84 Mn TIBETAN MARK HALANTA
# 1770 Lo TAGBANWA LETTER SA
# 33af So SQUARE RAD OVER S SQUARED

# == decimal / digit / numeric

ud.decimal('٥')
# 5
ud.digit('٤')
# 4

ud.numeric('3')
# 3.0
ud.numeric('½')
# 0.5
ud.numeric('¾')
# 0.75
ud.numeric('Ⅳ')
# 4.0
ud.numeric('五')
# 5.0
ud.numeric('²')
# 2.0
ud.numeric('ↀ')
# 1000.0
