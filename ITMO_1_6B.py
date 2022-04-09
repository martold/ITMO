import pandas, datetime, shutil, os, numpy, sys

requiredFiles = ['orderdata_sample.csv', 'input.csv', 'data1.csv', 'bikes.csv', 'data2.csv']
logfile = ('/Users/admin/Desktop/Python/data/logfile.log')
path = ('/Users/admin/Desktop/Python/data/')
currentTime = datetime.datetime.today().strftime("%Y_%m_%d-%H.%M.%S")

for i in requiredFiles:
    try:
        file = open(path + i)
        shutil.copyfile(path + i, path + currentTime + '_' + i)
        sys.stdout = open(logfile, 'a')
        print(currentTime, "- file", i, "has been succefully copied\n")
        os.remove(path + i)
        sys.stdout = open(logfile, 'a')
        print(currentTime, "- original file", i, "has been succefully deleted\n")
    except:
        sys.stdout = open(logfile, 'a')
        print(currentTime, "- ERROR: file", i, "does not exist\n")
