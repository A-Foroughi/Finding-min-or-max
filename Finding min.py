# This code shows the minimum element of the list and for changing it go to line 6.
A = [int(i) for i in input().split()]
m = A[0]
p = 1
for i in range(1, len(A)):
    # If you replace A[i] < m with A[i] > m it will show you the maximum element.
    if A[i] < m:
        m = A[i]
        p = i + 1
print(f"The minimum number in this list is {m} and it is the {p}th number.")