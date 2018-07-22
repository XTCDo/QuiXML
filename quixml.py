import hashlib
import os
import time
import datetime

ATTR_SEPARATOR = ";;"

def getLooseText(str):
    if str.lstrip().startswith(";t "):
        return str.split(";t ")[1].strip("\n")
    else:
        return ''

def getText(str):
    str = ' '.join(str.split(ATTR_SEPARATOR)[0].split()[1:])
    return str

def getAttributes(str):
    if ATTR_SEPARATOR not in str:
        return ''
    attributes = str.split(ATTR_SEPARATOR)[1:]
    attributesOut = []
    for attr in attributes:
        attr = attr.split()
        attrName = attr[0]
        attrVal = ' '.join(attr[1:]).strip()
        attributesOut.append('%s="%s"' % (attrName, attrVal))
    return ' '.join(attributesOut)

def getTags(str):
    attributes = getAttributes(str)
    if attributes != '':
        attributes = ' ' + attributes
        
    str = str.split()[0]
    
    return '<%s%s>' % (str, attributes), '</%s>' % str


def flattenEmptyTags(tags):
    print('--------') 
    i = 0
    for t in tags:
        
        if i + 1 != len(tags):
            tag = tags[i]
            nextTag = tags[i+1]
            
            if not("\n" in tag or "\n" in nextTag) and \
               "</" not in tag.split('>')[0] and \
               "<" in nextTag.split('>')[0] and \
               tag.split('>')[0].strip()[1:].split(" ")[0] == nextTag.split('>')[0].strip()[2:].split(" ")[0]:
                tags[i] = tags[i][:-1] + "/>"
                tags.pop(i+1)
            i = i + 1
    return tags

def createXML(filename):
    out = []
    with open(filename) as f:
        line = f.readline()
        cnt = 0
        while line:
            currentSpaceCount = len(line) - len(line.lstrip(' '))
            line = line.strip('\n')
            while line.endswith(";n"):
                line = line[:-2] + f.readline().strip('\n')
                

            if getLooseText(line) != '':
                out.insert(cnt - currentSpaceCount, ' '*currentSpaceCount + getLooseText(line))
                cnt = cnt + 1
            else:
                openingTag, closingTag = getTags(line)
                out.insert(cnt - currentSpaceCount, ' '*currentSpaceCount + closingTag)
                if len(getText(line)) != 0:
                    out.insert(cnt - currentSpaceCount, ' '*currentSpaceCount + openingTag + "\n" + ' '*(currentSpaceCount + 1) + getText(line))
                else:
                    out.insert(cnt - currentSpaceCount, ' '*currentSpaceCount + openingTag)
                cnt = cnt + 2
            
            line = f.readline()
            while line.isspace():
                line = f.readline()

        
        out = flattenEmptyTags(out)
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
