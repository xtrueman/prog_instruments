import unicodedata as ud

srcchar = "\u0063\u0327"
# -> 'ç'

len(srcchar)
# -> 2

# == normalize

ud.normalize('NFD', srcchar)
# -> 'ç'

ud.normalize('NFD', srcchar)
# -> 'ç'

len(ud.normalize('NFD',srcchar))
# -> 2

len(ud.normalize('NFC',srcchar))
# -> 1

ud.normalize('NFC', srcchar) == srcchar
# -> False

ud.normalize('NFD',srcchar) == srcchar
# -> True

ud.normalize('NFKD','①︷⁹¼™')
# '1{91⁄4TM'


# == decomposition

ud.decomposition('a')  # Обычная буква
# -> ''

ud.decomposition('á')  # Буква с акцентом
# -> '0061 0301'

# Пример 3: Другой декомпозированный символ
ud.decomposition('ę')  # Буква с огоньком
# -> '0065 0328'
