"""
讓使用者決定一個範圍，產生一個隨機整數(不要印出來)
讓使用者重複輸入數字去猜，並且印出 猜第幾次
猜對的話，印出"終於猜對了!"
猜錯的話，要告訴他 比答案大/小
"""

import random

x = int(input("請輸入起始值: "))
y = int(input("請輸入終止值: "))

num = random.randint(x, y)
#print(pwd)

pwd = int(input("請輸入密碼: "))
count = 0

while pwd != num:
	count += 1
	if pwd < num:
		print("猜錯，比答案小，再猜!(猜第", count, "次)", sep="", end="")
		pwd = int(input("請輸入密碼: "))
	elif pwd > num:
		print("猜錯，比答案大，再猜!(猜第", count, "次)", sep="", end="")
		pwd = int(input("請輸入密碼: "))
print("終於猜對了! 總共猜",count,"次", sep="")

"""
參考解答:
import random
start = input("請決定隨機數字範圍開始值: ")
end = input("請決定隨機數字範圍結束值: ")
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	count += 1
	num = input("請猜數字: ")
	num = int(num)
	if num == r:
		print("你猜中了!")
		print("這是你猜的第", count, "次")
		break
	elif num > r:
		print("比答案大")
	elif num < r:
		print("比答案小")
	print("這是你猜的第", count, "次")
"""