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

    f = open(filename, 'rb')
    for i in range(noOfRecords):
        n = pickle.load(f)
        print(str(i) + " key : " + str(n.getKey()))

def mergeSort(filename):
    '''
    Objective: To sort the records in the given file using mergeSort.
               *** This function changes the content of the file entered.
    Input Parameter:
           filename: The file in which records are to be sorted.
    '''
    '''
    Approach: We set a variable named blockSize initially to 4. Then read first blockSize records from the file entered, sort them 
    '''
    


saveRecords("f.txt", 100)
printRecords("f.txt", 100)
