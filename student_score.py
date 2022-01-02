#第三组
#组员是杨鑫鑫、汤卫生、王玮怡、李轲、熊慕宇
#学生成绩分析系统（函数图像）

import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
df=pd.read_csv('student_score.csv',encoding='GBK') #读取student_score.csv文件为DataFrame字符流
Python_max=df.Python.max() #python最大值
math_max=df.Math.max()  #Math最大值
english_max=df.English.max()  #English最大值

Python_min=df.Python.min() #python最小值
math_min=df.Math.min() #Math最小值
english_min=df.English.min() #English最小值  

name=df.num
students_scores=df.Math+df.Python+df.English #学生总成绩     

Python_avg=df.Python.mean()#python平均分
math_avg=df.Math.mean() #Math平均分
english_avg=df.English.mean() #English平均分

def main():
    while True:
        menm()
        choice=int(input('请选择：'))
        if choice in [0,1,2,3,4]:
            if choice==0:
                answer=input('您确定要退出系统吗？y/n')
                if answer=='y' or answer=='Y':
                    print('感谢您的使用！！')
                    break#退出系统
                else:
                    continue
            elif choice == 1:
                score()  # 学生总成绩分布图
            elif choice == 2:
                score_avg()  # 每门课程平均分展示图
            elif choice == 3:
                score_max()  # 每门课程最高分展示图
            elif choice == 4:
                score_min()  # 每门课程最低分展示图

def menm():
    print('===========================学生成绩分析系统=================================')
    print('----------------------------功能菜单----------------------------------------')
    print('\t\t\t\t\t\t1.学生总成绩分布图')
    print('\t\t\t\t\t\t2.每门课程平均分展示图')
    print('\t\t\t\t\t\t3.每门课程最高分展示图')
    print('\t\t\t\t\t\t4.每门课程最低分展示图')
    print('\t\t\t\t\t\t0.退出')
    print('----------------------------------------------------------------------------')

def score():#录入学生信息功能，save（student）函数，用于将学生信息保存到文件，insert（）函数，用于录入学生信息
    plt.title('学生总成绩分布图')
    plt.xlabel('学号')
    plt.ylabel('总分')
    plt.bar(name, students_scores)
    plt.figure()
    plt.show()

def score_avg():
    plt.title('每门课程平均分展示图')
    plt.xlabel('课程名')
    plt.ylabel('平均分')
    plt.bar('Python', Python_avg)
    plt.bar('Math', math_avg)
    plt.bar('English', english_avg)
    plt.figure()
    plt.show()

def score_max():
    plt.title('每门课程最高分展示图')
    plt.xlabel('课程名')
    plt.ylabel('最高分')
    plt.bar('Python', Python_max)
    plt.bar('Math', math_max)
    plt.bar('English', english_max)
    plt.figure()
    plt.show()

def score_min():
    plt.title('每门课程最低分展示图')
    plt.xlabel('课程名')
    plt.ylabel('最低分')
    plt.bar('Python', Python_min)
    plt.bar('Math', math_min)
    plt.bar('English', english_min)
    plt.figure()  # 可以删除
    plt.show()

if __name__ == '__main__':
    main()
