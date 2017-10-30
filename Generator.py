# Python 3 format
import codecs

fileInPath = './_input/input.txt'
fileOutPath = './_result/result.txt'


def importArray():
    global arr01, arr02, arr03, arr04
    fileStream = codecs.open(fileInPath, encoding='utf-8', mode='r')
    string = fileStream.read()
    # print(string)
    stringArray = string.split('\r\n\r\n')
    arr01 = stringArray[0].split('|')
    arr02 = stringArray[1].split('|')
    arr03 = stringArray[2].split('|')
    arr04 = stringArray[3].split('|')

def proccessing():
    temp = []
    for a in arr01:
        for b in arr02:
            temp.append("{} {}".format(a, b))
        
        for c in arr03:
            temp.append("{} {}".format(a, c))

        for d in arr04:
            temp.append("{} {}".format(a, d))
    return temp

def fileOut():
    fileStream = codecs.open(fileOutPath, encoding='utf-8', mode='w')
    for i in proccessing():
        fileStream.write('{}\n'.format(i))
    print('Done!')    

if __name__ == '__main__':
    importArray()
    # proccessing()    
    fileOut()