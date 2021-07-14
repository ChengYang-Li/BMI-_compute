# 這是一個BMI計算器
print('BMI計算')
name = input('請輸入名字: ')
print('你好啊', name)
height = float(input('你的身高是多少公分?'))
weight = float(input('你的體重是多少公斤?'))
bmi = weight/((height/100)**2) # BMI公式
print(name, '你的BMI為', bmi)
if bmi < 18.5:
	print('你的體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('你的體重正常')
elif bmi >= 24 and bmi < 27:
	print('你的體重過重')
elif bmi >= 27 and bmi < 30:
	print('你有輕度肥胖')	
elif bmi >= 30 and bmi < 35:
	print('你有中度肥胖')
else :
	print('你有重度肥胖')		