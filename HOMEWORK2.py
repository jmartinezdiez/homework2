
import dictionary

print (dictionary.d)

text = "I have a really good friend from Romania what his name is Bogdan and who is teaching me to programming really well"
translate = ""
words = text.split ()
for w in words:
    translate = translate + " " + dictionary.d[w]

print(translate)

