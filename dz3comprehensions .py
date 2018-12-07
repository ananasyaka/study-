first_array = [4,3,9,7,2,1]
n_array = [int(x**(1 / 2)) if int(x**(1 / 2)) == x**(1 / 2) else x**2 for x in first_array ]
print(n_array)