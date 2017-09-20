import codecs

fileInPath = './_input/input.txt'
fileOutPath = './_result/result.txt'
arr01 = []
arr02 = []
arr03 = []
arr04 = []

def importArray():
    fileStream = codecs.open(fileInPath, encoding='utf-8', mode='r')
    string = fileStream.read()
    # print(string)
    stringArray = string.split('\r\n\r\n')
    arr01 = stringArray[0].split('|')
    arr02 = stringArray[1].split('|')
    arr03 = stringArray[2].split('|')
    arr04 = stringArray[3].split('|')
    print(arr01)
    print(arr02)
    print(arr03)
    print(arr04)


def fileOut():
    fileStream = codecs.open(fileOutPath, encoding='utf-8', mode='w')
    fileStream.write(arr01[0])
    print('Success!')

if __name__ == '__main__':
    importArray()
    # fileOut()