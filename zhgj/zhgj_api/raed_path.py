# *_*coding:utf-8 *_*
import os


def get_path():
    file_list = []
    os_path = os.path.split(os.path.realpath(__file__))[0]
    file_path = os.path.join(os_path,"TestCase")
    for root,dirs,files in os.walk(file_path):
        for file in files:
            str = os.path.join(root,file)
            if str.endswith(".py") and not str.endswith("__init__.py"):
                str1 = str.split("module\\")[1]
                file_list.append(str1)
            else:
                pass
    return file_list

def get_imsg_pash(img_path):
    imsg_list = []
    os_pash = os.path.split(os.path.realpath(__file__))[0]
    imsg_path = os.path.join(os_pash,"TestFile","imag")
    for root,dirs,flies in os.walk(imsg_path):
        for file in flies:
            str = os.path.join(root,file)
            if not str.endswith("__init__.py"):
               imsg_list.append(str)
            for test in imsg_list:
                if test.endswith(img_path):
                    break
    return test


def get1_path():
    file_list = []
    os_path = os.path.split(os.path.realpath(__file__))[0]
    file_path = os.path.join(os_path,"TestCase")
    for root,dirs,files in os.walk(file_path):
        for file in files:
            str = os.path.join(root,file)
            if str.endswith(".py") and not str.endswith("__init__.py"):
                file_list.append(str)
            else:
                pass
    return file_list
#a = get_imsg_pash('1.jpg')
#print(a)

#b = get_path()
#print(b)

'''
# 方法的重写
# 当我们调用一个对象的方法时
#    会优先去当前对象中寻找是否具有该方法，如果有则直接调用
#    如果没有则去对象的父类中寻找，如果父类中有则直接调用父类中的方法
#    如果还是没有则去父类中的父类中寻找，以此类推，直到找到object ,
#    如果始祖父类也没有， 就报错
class Animal:
    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')

class Dog(Animal):
    def bark(self):
        print('汪汪汪~~~')

    def run(self):
        print('狗跑~~~~')

d = Dog()
d.run()
d1 = Animal()
d1.run()

#重载

#重载方法的名称是相同的，但在方法的声明中一定要有彼此不相同的成
#份，以使编译器能够区分这些方法。重载的方法必须遵循下列原则：
#➢方法的参数必须不同，包括参数的类型或个数，以此区分不同方法
#体；
#➢方法的返回类型、修饰符可以相同，也可以不同。
#实例：两个同名的函数，传参不同
def a(x):
    return x

def a(x,y):
    return x+y

print(a(1,2))
print(a(1))
#python是没有重载的，第二个同名的函数会把第一个覆盖掉
#第一因为python没有类型，第二python有可变参数
'''
'''
import requests
import json
ur = "https://sys.zhihuigongjiang.com//web/employee/save"
headers = {
           'token':'web12bc3c633e3f44b6abc97777c4888f20'}
data = {"myCompanyEmployeeId": None,
        "workerName": "万三",
        "myPhone": "13712714111",
        "nation": None,
        "address": None,
        "myDepartmentId": "1073",
        "isLogin": "1",
        "idcardNumber": "421123199008084511",
        "birthday": None
        }
files = {'file':('2.jpg',open('D:\\Training_interface1111111\\TestFile\\imag\\2.jpg','rb'),'image/jpeg')}
print(files)
re = requests.post(url=ur,headers = headers,files=files,data =data,verify=False )
print(re.text)
'''
