text = input("Введіть ваш текст: ")
transliteration = ''
spec = 3
dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'ґ': 'ĝ', 'д': 'd', 'е': 'e', 'є': 'je', 'ж': 'ž', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'ji', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č', 'ш': 'š', 'щ': 'šč', 'ь': "'", 'ю': 'ju', 'я': 'ja','А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Ґ': 'Ĝ', 'Д': 'D', 'Е': 'E', 'Є': 'Je', 'Ж': 'Ž', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'Ji', 'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č', 'Ш': 'Š', 'Щ': 'Šč', 'Ь': "'", 'Ю': 'Ju', 'Я': 'Ja'}
digraf = {'ьо': 'jo'}
fullybigantidygraf = {'Я': 'JA', 'Є': 'JE', 'Ї': 'JI', 'Ю': 'JU'}
for output in text:
    if output in "АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя":
        if spec == 0:
            if output == 'о':
                transliteration = transliteration + digraf.get('ьо')
                spec = 1
            else: spec = 3
        if output == 'ь':
            spec = 0
        if spec == 3:
                transliteration = transliteration + dict.get(output)
        if spec == 1:
            spec = 3
    else:
         transliteration = transliteration + output
print("Vyhid: " + transliteration)
