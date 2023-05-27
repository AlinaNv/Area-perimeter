#coding=windows-1251
print("Введите длину и ширину прямоугольника через пробел")
a,b=map(float, input().split())
S=a*b
P=(a+b)*2
print("Площадь прямоугольника:", S)
print("Периметр прямоугольника:", P)
