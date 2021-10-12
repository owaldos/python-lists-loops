
spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }


list_to_add={'love':'amor','code':'codigo','smart':'inteligente'}
for word in list_to_add.items():
    spanish_translations[word[0]]= word[1]
print("Translation", spanish_translations["dog"])
print("All", spanish_translations)

