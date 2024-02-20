pencil = 65
pack = 350
pencilspack = 6

total = int(input("Введите количество карандашей: "))

packs = total // pencilspack
pencils = total % pencilspack

totalwithpacks = packs * pack + pencils * pencil
totalwithoutpacks = total * pencil

savings = totalwithoutpacks - totalwithpacks

print("Количество упаковок с карандашами:", packs)
print("Количество карандашей поштучно:", pencils)
print("Выгода с покупки:", savings, " рублей")