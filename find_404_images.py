import os
import glob
import re

path = './unilever-platform/app/dove/svgs/sprites/'

txtfiles = []
for fileName in glob.glob("./unilever-platform/app/dove/sass/views/*/*.scss"):
    #txtfiles.append(fileName)
    file_read = open(fileName, "rt") # open lorem.txt for reading text
    file_txt = file_read.read()
    svgName = re.findall('sprites/(.+?).svg', file_txt)
    for svg in svgName:
        isExist = os.path.exists(path+svg+'.svg')
        if not isExist:
            print(fileName)
            print(svg+".svg")
    # for st in m:
        # if st:
            # print(m)
    # with open(file) as file:
    #     for line in file:
    #         urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
    #         print(urls)

# isExist = os.path.exists(path)

# print(txtfiles);
