# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruites=["яблоко", "банан", "киви", "арбуз"]
for _ in fruites:
    print("{0:>30}) {1}".format(fruites.index(_), _))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

lst0=[' ','element0','element1','element2','element0']
lst1=['nelement0','element0']
print('list0: {0} \n list1: {1}'.format(lst0,lst1))
input('Press Enter to modify')
for x in lst1:
    a=lst0.count(x)
    if a>0:
        for i in range(a):	     
            lst0.remove(x)
print('list0: {0} \n list1: {1}'.format(lst0,lst1))
		

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

lst=[5,4,99,76,12,32,56,22,7,63,85]
print(lst);
for _ in lst:
    if _%2==0:
        a=lst.index(_)
        lst.pop(a)
        lst.insert(a,_/4)
    else:
        a=lst.index(_)
        lst.pop(a)
        lst.insert(a,_*2)
print(lst)