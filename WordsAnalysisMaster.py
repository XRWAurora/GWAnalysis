import sys
import re

guanjianzilist = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum',
                  'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed',
                  'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile',
                  'while']
yunsuanfulist = ['+', '-', '*', '/', '>', '%', '<', '=', '>=', '<=', '!=']
jiexianfulist = [',', ';', '.', '(', ')', '[', ']', '{', '}']
feifazifulist = ['~', '`', '@', '$', '￥']


def readtesttxt():  # 读取测试文件
    f = open('test.txt', encoding='UTF-8')
    rawwords = []
    for line in f:
        rawword = line.strip()
        rawwords.append(rawword)
    # print(rawwords)
    return rawwords


def isSpace(Char):
    if Char == ' ':
        return True
    else:
        return False


def isnumber(Char):
    if '0' <= Char <= '100':
        return True
    else:
        return False


def ischar(Char):
    if ('a' <= Char <= 'z') or ('A' <= Char <= 'Z'):
        return True
    else:
        return False


def standerdoutput(resultlist):  # 输出文件
    f = open("output.txt", "w+")
    for word in resultlist:
        if word in yunsuanfulist:
            print("种别码:4" + "  类型:运算符" + " 单词:" + word, file=f, flush=True)
            print("种别码:4" + "  类型:运算符" + " 单词:" + word, file=sys.stdout)
        elif word in jiexianfulist:
            print("种别码:5" + "  类型:界限符" + " 单词:" + word, file=f, flush=True)
            print("种别码:5" + "  类型:界限符" + " 单词:" + word, file=sys.stdout)
        elif word in guanjianzilist:
            print("种别码:1" + "  类型:关键字" + " 单词:" + word, file=f, flush=True)
            print("种别码:1" + "  类型:关键字" + " 单词:" + word, file=sys.stdout)
        elif word.isdigit():
            print("种别码:11" + " 类型:常数" + "   单词:" + word, file=f, flush=True)
            print("种别码:11" + " 类型:常数" + "   单词:" + word, file=sys.stdout)
        elif word.isalnum():
            print("种别码:10" + " 类型:标识符" + " 单词:" + word, file=f, flush=True)
            print("种别码:10" + " 类型:标识符" + " 单词:" + word, file=sys.stdout)
    f.close()


def wordssegmentation(rawwords):  # 字符分割函数
    resultlist = []
    line = 0
    f = open("ErrorLog.txt", "w+")
    for String in rawwords:
        Letter = ''
        letter = ''
        index = 0
        line += 1
        for Char in String:
            if index < len(String) - 1:
                index += 1
            if ischar(Char) or isnumber(Char):  # 判断当前取得字符是字符还是数字
                if ischar(String[index]) or isnumber(String[index]):
                    Letter += Char  # 将下标为index的字符加入到字符串Letter中
                elif isSpace(String[index]) or (String[index] in jiexianfulist) or (
                        String[index] in yunsuanfulist) or (
                        String[index:index + 2] in yunsuanfulist):  # 若遇到非数字非字符的字符直接截断
                    Letter += Char
                    resultlist.append(Letter)
                    Letter = ''  # 重置Letter
            elif Char in jiexianfulist:  # 判断当前取得字符是否是界限符
                resultlist.append(Char)
            elif Char in yunsuanfulist:  # 判断当前取得字符是否是运算符
                letter += Char
                if String[index] in yunsuanfulist:
                    letter += String[index]
                    resultlist.append(letter)
                    letter = ''
                else:
                    resultlist.append(letter)
                    letter = ''
            elif Char in feifazifulist:
                letter += String[index]
                print("错误！非法字符:" + Char + " 错误行数:" + str(line) + " 列数:" + str(index), file=f, flush=True)
                print("错误！非法字符:" + Char + " 错误行数:" + str(line) + " 列数:" + str(index), file=sys.stdout)
                letter = ''
            elif isSpace(Char):  # 判断当前取得字符是否是空格
                pass
            else:
                print("警告！无法识别当前字符:" + Char + " 错误行数:" + str(line) + " 列数:" + str(index), file=f, flush=True)
                print("警告！无法识别当前字符:" + Char + " 错误行数:" + str(line) + " 列数:" + str(index), file=sys.stdout)
    return resultlist


if __name__ == '__main__':
    rawwords = readtesttxt()
    resultlist = wordssegmentation(rawwords)
    print(resultlist)
    standerdoutput(resultlist)
