import pandas as pd 
df = pd.read_csv('StudentsPerformance.csv')

df.info()
#ГИПОТЕЗЫ
#1)ЕСЛИ НЕ ПОЗАВТРАКАТЬ, РЕЗУЛЬТАТ ЭКЗАМЕНА МОЖЕТ БЫТЬ неуд.
#2)У ОБРАЗОВАННЫХ РОДИТЕЛЕЙ ДЕТИ СДАЮТ ЭКЗАМЕНЫ ЛУЧШЕ
# ЕСЛИ НЕ ПОЗАВТРАКАТЬ, РЕЗУЛЬТАТ ЭКЗАМЕНА МОЖЕТ БЫТЬ неуд. lunch test preparation course 
print(df['lunch'].value_counts())
'''
standard        645
free/reduced    355
'''
print(df['test preparation course'].value_counts())
'''
none         642
completed    358
'''
print(df.groupby(by='lunch')['test preparation course'].value_counts())
'''
lunch         test preparation course
free/reduced  none                       224
              completed                  131
standard      none                       418
              completed                  227
'''
temp = df.groupby(by='lunch')['test preparation course'].value_counts()
print(temp['free/reduced']['none'] / temp['free/reduced']['completed'])
print(temp['standard']['none'] / temp['standard']['completed'])
#1.7099236641221374 vs. 1.841409691629956
#ГИПОТЕЗА НЕ РАБОТАЕТ
#2)У ОБРАЗОВАННЫХ РОДИТЕЛЕЙ ДЕТИ СДАЮТ ЭКЗАМЕНЫ ЛУЧШЕ
#Как ты 
print(df['parental level of education'].value_counts())

'''
some college          226
associate's degree    222
high school           196
some high school      179
bachelor's degree     118
master's degree        59
'''
temp = df.groupby(by='parental level of education')['test preparation course'].value_counts()
print(temp)
print(temp["some high school"]["none"] / temp["some high school"]["completed"])#1.3246753246753247
print(temp["high school"]["none"] / temp["high school"]["completed"])#2.5
print(temp["associate's degree"]["none"] / temp["associate's degree"]["completed"])#1.7073170731707317
print(temp["some college"]["none"] / temp["some college"]["completed"])#1.9350649350649352
print(temp["bachelor's degree"]["none"] / temp["bachelor's degree"]["completed"])#1.565217391304348
print(temp["master's degree"]["none"] / temp["master's degree"]["completed"])#1.95

'''
associate's degree           none                       140
                             completed                   82
bachelor's degree            none                        72
                             completed                   46
high school                  none                       140
                             completed                   56
master's degree              none                        39
                             completed                   20
some college                 none                       149
                             completed                   77
some high school             none                       102
                             completed                   77
'''
