#Напишите программу, удаляющую из текста все слова, содержащие "абв".

# text = 'абв  продабвукт воабвла  абвввв аавабв  '
text=input('Введите текст: ')
list1 = text.split(' ')
print(list1)

i = len(list1)-1

while i >= 0:
    if 'абв' in list1[i]:
        list1.remove(list1[i])
    i -= 1
    
print(list1)        