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

