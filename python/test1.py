import sys
import itertools

n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
list1 = list(map(int, line.split()))
line = sys.stdin.readline().strip()
list2 = list(map(int, line.split()))
m = int(sys.stdin.readline().strip())
list1.sort()
list2.sort()

# met=0
# for i in itertools.permutations(list2):
#     for j in range(n):
#         if list2[j]>list1[j]:
#             break
#     else:
#         met+=1
# print(met%m)

def ans(list1, list2, n):
    answer = []
    for i in range(n):
        answer.append(0)
    i, j = 0, 0
    while j < n:
        if list1[i] < list2[j] and i == j:
            return 0
        if list1[i] >= list2[j]:
            j += 1
            answer[i] += 1
        if i < j < n and list1[i] < list2[j]:
            i += 1
            answer[i] = answer[i - 1]
    while i < n - 1:
        i += 1
        answer[i] = answer[i - 1]
    temp = 1
    for k in range(n):
        temp *= (answer[k] - k)
    return temp

print(ans(list1, list2, n))
