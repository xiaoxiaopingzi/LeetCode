x, y, z = map(int, input().split())
#
#
# def isTrig(x1, x2, x3):
#     if x1 + x2 > x3 and x1 + x3 > x2 and x2 + x3 > x1:
#         return True
#     else:
#         return False
#
#
myCount = 0
# for a in range(1, x + 1):
#     for b in range(1, y + 1):
#         for c in range(1, z + 1):
#             if isTrig(a, b, c):
#                 myCount += 1
# print(myCount)


# x, y, z = map(int, input().split())

# total = 0

for i in range(1, x + 1):
    for j in range(1, y + 1):
        z_d = (max(abs(i - j) + 1, 1)) % 1000000007
        z_u = min(i + j - 1, z) % 1000000007
        i = i % 1000000007
        j = j % 1000000007

        myCount += max(z_u - z_d + 1, 0)
print(myCount)
