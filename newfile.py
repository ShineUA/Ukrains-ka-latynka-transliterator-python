text = input("Введіть ваш текст: ")
transliteration = ''
dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'ґ': 'ĝ', 'д': 'd', 'е': 'e', 'є': 'je', 'ж': 'ž', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'ji', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č', 'ш': 'š', 'щ': 'šč', 'ь': "'", 'ю': 'ju', 'я': 'ja', "'": "'", 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Ґ': 'Ĝ', 'Д': 'D', 'Е': 'E', 'Є': 'Je', 'Ж': 'Ž', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'Ji', 'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č', 'Ш': 'Š', 'Щ': 'Šč', 'Ь': "'", 'Ю': 'Ju', 'Я': 'Ja', '.': '.',';': ';', ':': ':', ',': ',', '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', ' ': ' ', '"': '"'}
for output in text:
    transliteration = transliteration + dict.get(output)
print("Vyhid: " + transliteration)
