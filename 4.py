''' 
    Задача взята из Я.Репетитор: https://yandex.ru/tutor/subject/problem/?problem_id=T29800
    Суть алгоритма в том, что разность двух чисел кратна 3, если остатки от деления этих чисел на 3 равны.
    Будем рассматривать каждое введённое число как правый элемент возможной пары (первые шесть чисел не могут быть таким элементом)
    и в зависимости от остатка при его делении на 3 определять количество подходящих пар и прибавлять его к общей сумме.
'''

N = int(input()) # Кол-во элементов
a = [] # Главный массив
ost = [] # Остатки
d = 6 # Дистанция в 6 элементов
k = 3 # Остатки 0, 1, 2

for i in range(0, d):
    a.append(int(input())) # Первые 6 чисел

for i in range(0, k):
    ost.append(0) # Наши остатки 0, 1, 2

curInd = 0 # Текущий индекс в массиве a
counter = 0 # Счётчик

for i in range(d, N):
    x = int(input()) # Вводим след число

    ost[a[curInd] % 3] += 1 # Увеличиваем счётчик чисел с этим же остатком
    counter += ost[x % 3] # Прибавляем то кол-во, которое удовлетворяет x % 3

    a[curInd] = x # Заменяем текущий элемент на следующий
    curInd = (curInd + 1) % d # Считаем новый остаток, который и будет следующим индексом

print(counter) # Выводим ответ
