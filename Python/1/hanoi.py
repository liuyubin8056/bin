#这是只计数的版本
counter = 0
def hanoi(n,x,y,z):
    global counter
    if n==1:
        print(x,"-->",z)
        counter+=1
    else:
        #将n-1的盘子从x移动到y
        hanoi(n-1,x,z,y)
        #将最底下的盘子从x移动到z
        print(x,'-->',z)
        #再将n-1个盘子从y移动到z
        hanoi(n-1,y,x,z)
        counter+=1
num = input("请输入汉诺塔层数\n")
if num.isdigit():
    hanoi(int(num),'x','y','z')
print("总共移动了",counter,"次")

#这是实际定义柱子的版本（但无法自定义盘子数量）
counter = 0
x=[5,4,3,2,1]
y=[]
z=[]
def hanoi(n,x,y,z):
    global counter
    if n==1:
        z.append(x.pop())
        print("x --> z")
        print(f"x={x},y={y},z={z}")
        counter+=1
    else:
        #将n-1的盘子从x移动到y
        hanoi(n-1,x,z,y)
        #将最底下的盘子从x移动到z
        z.append(x.pop())
        print("x --> z")
        print(f"x={x},y={y},z={z}")
        #再将n-1个盘子从y移动到z
        hanoi(n-1,y,x,z)
        counter+=1
num = 5
hanoi(num,x,y,z)
print("总共移动了",counter,"次")

#这个真的他妈可以自定义盘子数量
counter = 0
x=[]
y=[]
z=[]
num = input("请输入汉诺塔层数\n")
if num.isdigit():
    for i in range(int(num),0,-1):
        x.append(i)
def hanoi(n,x,y,z):
    global counter
    if n==1:
        z.append(x.pop())
        print("x --> z")
        print(f"x={x},y={y},z={z}")
        counter+=1
    else:
        hanoi(n-1,x,z,y)
        z.append(x.pop())
        print("x --> z")
        print(f"x={x},y={y},z={z}")
        hanoi(n-1,y,x,z)
        counter+=1
hanoi(int(num),x,y,z)
print("总共移动了",counter,"次")