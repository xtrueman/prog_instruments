sc1 = "🏻"
sc2 = "🏼"
sc3 = "🏽"
sc4 = "🏾"
sc5 = "🏿"

smile = "😀"
face1 = "👩"
love = "❤️"
zwj = "\u200D"


print(smile+sc5)
print(face1+zwj+love+zwj+face1)


# (U+1F600)
# U+1F3FB 
# 🏻 Emoji Modifier Fitzpatrick Type-1-2
# U+1F3FC
# 🏼 Emoji Modifier Fitzpatrick Type-3
# U+1F3FD
# 🏽 Emoji Modifier Fitzpatrick Type-4
# U+1F3FE
# 🏾 Emoji Modifier Fitzpatrick Type-5
# U+1F3FF
# 🏿 Emoji Modifier Fitzpatrick Type-6



In [342]: print("\U0001F469\u200D\U0001F37C")
👩‍🍼

In [343]: print("\U0001F469\U0001F37C")
👩🍼
