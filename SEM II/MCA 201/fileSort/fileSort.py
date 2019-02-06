import os, random, pickle

class Node:
    '''
    Objective: To represent a record entity
    '''
    def __init__(self, key):

        self.key = key
        self.others = str(self.key)*random.randint(50, 250)

    def getKey(self):
        return self.key

    def getOthers(self):
        return self.others

    def __str__(self):
        return ("Key: " + str(self.getKey()) + "\nOthers: " + str(self.getOthers()))




def generateKey(keys, startRange, endRange):
        '''
        Objective: To generate a unused key in the list in the given range.
        '''
        if len(keys) >= endRange - startRange:
            print("Maximum keys generated already.")
            return

        while True:
            key = random.randint(startRange, endRange)
            if key not in keys:
                keys.append(key)
                return key



def saveRecords(filename, noOfNodes):
    '''
    Objective: To create a file and create and save noOfNodes records in given file . If
                file exists already, delete the file and create new again.
    Input Parameter:
           filename: Name of file in which records to be saved.
          noOfNodes: Number of records to be saved in the file.
    '''
    if os.path.isfile(filename):
        os.remove(filename)

    f = open(filename, 'wb')

    keys = []
    startRange = 1000000
    endRange = 2000000
    
    for i in range(noOfNodes):
        key = generateKey(keys, startRange, endRange)
        n = Node(key)
        pickle.dump(n, f)

    print(str(noOfNodes) + " records saved in " + filename)


def printRecords(filename, noOfRecords):
    '''
    Objective: To retrieve and print noOfNodes records in the given file.
    Input Parameter:
           filename: Name of file in which records to be saved.
           noOfRecords: Number of records to be retrieved from the file.
    '''
    try:    
        f = open(filename, 'rb')
        for i in range(noOfRecords):
            n = pickle.load(f)
            print(str(i) + " key : " + str(n.getKey()))
    except EOFError:
        pass

def makeFilesF1F2(filename, blockSize = 4):
    f = open(filename, "rb")
    f1 = open("f1.txt", "wb")
    f2 = open("f2.txt", "wb")
    
    endWhile = 0
    flag = 1
    while endWhile == 0:
        lst = []
        for i in range(blockSize):
            try:
                rec = pickle.load(f)
                lst.append(rec)
            except EOFError:
                endWhile = 1
                pass
        lst.sort(key = lambda Node: Node.getKey())
            
        for i in range(len(lst)):
            if flag == 1:
                pickle.dump(lst[i], f1)
            else: 
                pickle.dump(lst[i], f2)

        if flag == 1:
            flag = 2
        else:
            flag = 1

        
                
    


def mergeSort(file1, file2, blockSize = 4 , fileCount = 3):
    '''
    Objective: To sort the records in the given file using mergeSort.
               *** This function changes the content of the file entered.
    Input Parameter:
           filename: The file in which records are to be sorted.
    '''
    '''
    Approach: We set a variable named blockSize initially to 4. Then read first blockSize records from the file entered, sort them 
    '''
    if blockSize>10:
        printRecords(file1,blockSize)
        return
    else:
        f1 = open(file1, 'rb')
        f2 = open(file2, 'rb')
        f3 = open("f"+str(fileCount)+".txt", 'wb')
        f4 = open("f"+str(fileCount+1)+".txt", 'wb')

        rec1 = None
        rec2 = None

        endWhile = 0
        while endWhile == 0:
            p = 0

            for i in range(blockSize * 2):
                try:
                    if p==0:
                        rec1 = pickle.load(f1)    
                        rec2 = pickle.load(f2)
                    elif p==1:
                        rec1=pickle.load(f1)
                    else:
                        rec2=pickle.load(f2)
                except EOFError:
                    endWhile = 1
                    pass
                
                if rec1.getKey() < rec2.getKey():
                    p=1
                    pickle.dump(rec1,f3)
                else:
                    p=2
                    pickle.dump(rec2,f3)

            p = 0

            for i in range(blockSize * 2):
                try:
                    if p==0:
                        rec1 = pickle.load(f1)    
                        rec2 = pickle.load(f2)
                    elif p==1:
                        rec1=pickle.load(f1)
                    else:
                        rec2=pickle.load(f2)
                except EOFError:
                    endWhile = 1
                    pass

                if rec1.getKey() < rec2.getKey():
                    p=1
                    pickle.dump(rec1,f4)
                else:
                    p=2
                    pickle.dump(rec2,f4)
    mergeSort("f"+str(fileCount)+".txt","f"+str(fileCount+1)+".txt",blockSize*2,fileCount+2)
            

saveRecords("f.txt", 10)
printRecords("f.txt", 10)
makeFilesF1F2("f.txt")
mergeSort("f1.txt","f2.txt")
#printRecords("f1.txt", 6)
#printRecords("f2.txt", 6)

