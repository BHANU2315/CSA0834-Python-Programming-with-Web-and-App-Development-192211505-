def Nmaxelements(list1, N):
    final_list = []
    for _ in range(N):
        max1 = max(list1)
        list1.remove(max1)
        final_list.append(max1)
    return final_list

list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2
print(Nmaxelements(list1, N))  # Output: [85, 41]