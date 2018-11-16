#Сортировка выбором
def selection_sort(array):
    a = array
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        tmp = a[min]
        a[min] = a[i]
        a[i] = tmp
    return a

ary = [0,3,5,1,2,3,5,4,2,34,43,24]
selection_sort(ary)
print(ary)