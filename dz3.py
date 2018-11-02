def func(array, newarray) :
    for i in array:
        a = i ** (1 / 2)
        if a.is_integer():
            a = int(a)
            newarray.append(a)
        else:
            i **= 2
            newarray.append(i)
        i += 1
    print(array)
    print(newarray)
first_array = [4,3,9,7,2,1]
n_array = []
func(first_array, n_array)