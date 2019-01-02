from random import randint

class CommonElements:

    size = 0
    arr1 = []
    arr2 = []

    def init(self):
        print("Size of arrays")
        # take input from console
        self.size = int(input())
        print(self.size)
        # Initialize two same size array and asign some random values
        self.arr1 = [randint(0,100)for i in range(0,self.size)]
        self.arr2 = [randint(0,100)for i in range(0,self.size)]

    # Basic Thinking : iterate every element in first array and check in second array if element exists.
    def findCommonElementSolution1(self,arr1,arr2):
        numberOfCommenElements = 0
        for i in range(0,self.size):
            for j in range(0,self.size):
                if arr1[i]==arr2[j]:
                    numberOfCommenElements+=1
                    break
        return numberOfCommenElements
        

obj = CommonElements()
obj.init()
commonElements = obj.findCommonElementSolution1(obj.arr1,obj.arr2)
print("Total comman elements are %d" %(commonElements))
