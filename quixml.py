import hashlib
import os
import time
import datetime

def getText(str):
    return ' '.join(str.split()[1:])

def getTags(str):
    str = str.split()[0]
    return '<%s>' % str, '</%s>' % str

def createXML(filename):
    out = []
    with open(filename) as f:
        line = f.readline()
        cnt = 0
        while line:
            currentSpaceCount = len(line) - len(line.lstrip(' '))
            openingTag, closingTag = getTags(line)
            
            out.insert(cnt*2 - currentSpaceCount, ' '*currentSpaceCount + closingTag)
            if len(getText(line)) != 0:
                out.insert(cnt*2 - currentSpaceCount, ' '*currentSpaceCount + openingTag + "\n" + ' '*(currentSpaceCount + 1) + getText(line))
            else:
                out.insert(cnt*2 - currentSpaceCount, ' '*currentSpaceCount + openingTag)
            
            cnt = cnt + 1
            line = f.readline()
            while line.isspace():
                line = f.readline()


        outputString = '\n'.join(out)
        
        f = open("%s.xml" % filename.split('.')[0], "w+")
        f.write(outputString)
        f.close()

# https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def getTxtFiles():
    ret = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            ret.append(file)
    return ret

def convertFiles(txtFiles):
    for file in txtFiles:
        createXML(file)

def getHashes(txtFiles):
    hashes = {}
    for file in txtFiles:
        hashes[file] = md5(file)
    return hashes

def printConversionLog(file):
    fileName = file.split('.')[0]
    now = datetime.datetime.now()
    print("{:02d}:{:02d}:{:02d} Converted {}.txt to {}.xml".format(now.hour, now.minute, now.second, fileName, fileName))

def main():
    txtFiles = getTxtFiles()
    convertFiles(txtFiles)
    hashes = getHashes(txtFiles)
    while True:
        time.sleep(1)
        txtFiles = getTxtFiles()
        for file in txtFiles:
            if file in hashes:
                if md5(file) != hashes[file]:
                    createXML(file)
                    hashes[file] = md5(file)
                    printConversionLog(file)
            else:
                createXML(file)
                hashes[file] = md5(file)
                printConversionLog(file)
        hashes = getHashes(txtFiles)
        
main()
