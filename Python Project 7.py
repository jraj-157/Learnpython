# 1
i = input("Enter the number:")
for a in range(1,11):
    print(a*int(i))
# 2
l1 = ["herry","sohan","sachin","rahul"]
for name in l1:
    if name.startswith("s"):
     print("good morning "+name)
# 3
z = input("Enter Integer:")
v = 0
while v < 10:
    v = v + 1
    print(v*int(z))
# 4
b = input("Enter the number:")
n = 1
while n < int(b)-1:
    n = n + 1
    if (int(b)%n == 0):
      print(" Not Prime  ")
      break
else:
    print("  Prime  ")
# 5
h = int(input("Enter the number:"))
j = 1
k = 0
while j <= h:
   k = k + j
   j = j + 1
print(k)
# 6
i = int(input("Enter the number:"))
m = 1
s = 1
while m <= i:
    s = s * m
    m = m + 1
print(s)
# 7
v = 0
while v < 3:
    v = v + 1
    print(" " * v,end="")

    print(((2 * v)-1)*"*")
# 8
f = 0
while f < 3:
    f = f + 1
    print(f*"*")








   


