# 使用者決定隨機數字的範圍
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 “恭喜猜中！”
# 猜錯的話 告訴使用者 比答案大／小
# 會顯示猜的次數

import random

start = input("請決定隨機數字範圍的開始值 => ")
end = input("請決定隨機數字範圍的結束值 => ")
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0 # 計數器
while True:
	count += 1 # count = count + 1 # 每進迴圈計數器就+1
	num = input("請猜數字（1~100）：") # num：number
	num = int(num) # casting（型別轉換）
	if num == r:
		print("恭喜猜中！")
		print("你總共猜了", count, "次")
		break
	elif num > r:
		print("比答案大")
	elif num < r:
		print("比答案小")
	print("這是你猜的第", count, "次")
