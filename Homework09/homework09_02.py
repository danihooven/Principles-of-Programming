""" -------------------------------------------------------------------------------------------------------------------
ITEC 136: Homework 09 - 02

Provide different code snippets for
each of the following complexities.

O(n2)
O(n)
O(1)
O( nlog(n) )
O( log(n) )

@author: Dani Hooven
@version: 11/06/2020

-------------------------------------------------------------------------------------------------------------------- """


# O(n^2)
test = 0
for i in range(n):
    for j in range(n):
        test = test + i * j


# O(n)
test = 0
for i in range(n):
    test = test + 1

for j in range(n):
    test = test - 1


# O(log n)
i = n
while i > 0:
    k = 2 + 2
    i = i // 2


# O(1) - index assignment
mydict['x'] = mydict['x'] + 1


# O(nlog(n))
def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))