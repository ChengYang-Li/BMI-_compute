# 這是一個BMI計算器
print('BMI計算')
name = input('請輸入名字: ')
print('你好啊', name)
height = float(input('你的身高是多少公分?'))
weight = float(input('你的體重是多少公斤?'))
bmi = weight/((height/100)**2) # BMI公式
print('你的BMI為', bmi)