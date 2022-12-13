import zipfile

def extractFile(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print('wrong pass')
        return


def main():
    zFile = zipfile.ZipFile('test.zip')
    passFile = open('passlist.txt')
    for line in passFile.readLines():
        password = line.strip('\n')
        guess = extractFile(zfile, password)
        if guess:
            print('password = ' + password)
            break
