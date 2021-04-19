n, k = map(int, input().split(" "))
arr1 = list(map(int, input().split(" ")))
arr2 = list(map(int, input().split(" ")))
arr1.sort()
arr2.sort(reverse=True)
print(arr1)
print(arr2)
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] < arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        else

print(arr1)
print(arr2)

print(sum(arr1))