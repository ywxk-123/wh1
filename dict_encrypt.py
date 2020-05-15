#coding:UTF-8
'''
目标：已知一字典dict= {‘a’:’d’,’b’:’p’,’c’:’1’,’d’:’m’,’e’:’3’,’f’:’w’,
                    ’g’:’n’,’h’:’n’,’i’:’o’,’j’:’n’,’k’:’4’,’l’:’9’,
                    ’m’:’p’,’n’:’7’,’o’:’6’,’p’:’0’,’q’:’r’,’r’:’!’,
                    ’s’:’4’,’t’:’7’,’u’:’5’,’v’:’8’,’w’:’p’,’x’:’q’,
                    ’y’:’3’,’z’:’0’}。通过自定义函数的方式，实现在屏幕上任
意输入一串英文字符，根据字典中的配对，在屏幕上输出其对应的加密字符。
作者：王浩
日期：2020.05.05
'''

dict = {'a':'d','b':'p','c':'1','d':'m','e':'3','f':'w','g':'n',
        'h':'n','i':'o','j':'n','k':'4','l':'9','m':'p','n':'7',
        'o':'6','p':'0','q':'r','r':'!','s':'4','t':'7','u':'5',
        'v':'8','w':'p','x':'q','y':'3','z':'0'}

def dict_encrypt(plaintext) :
    
    ciphertext = ''
    for char in plaintext :
        ciphertext += dict[char]
    #在输入的字符串里循环，并把其转换为对应的字符串进行加密
    
    return ciphertext

yours = input('请输入一串英文字符(小写)：')
print('其对应的加密字符为：'+str(dict_encrypt(yours)))