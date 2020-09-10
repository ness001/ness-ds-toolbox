
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i-1] < a[i]:
                a[i],a[i-1] = a[i-1],a[i]
    return a
a = [1,2,3,4]
print(bubble_sort(a))