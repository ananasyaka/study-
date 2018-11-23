#Напишите программу, которая считывает из файла строку, соответствующую тексту,
#сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
#Sample Input:
#a3b4c2e10b1
#Sample Output:
#aaabbbbcceeeeeeeeeeb
def decode(string):
    list = []
    count = -1
    for i in range(len(s)):
        if ('a' <= s[i] <= 'z') or ('A' <= s[i] <= 'Z'):
            list.append([s[i]])
            count += 1
        else:
            list[count].append(s[i])
    for i in range(len(list)):
        str2 = ''
        for j in list[i][1::]:
            str2 = str2 + j
        print(list[i][0] * int(str2), end='')
f = open('file.txt', 'r')
s = f.readline()

decode(s)