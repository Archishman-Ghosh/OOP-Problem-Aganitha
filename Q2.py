class X:
    def __init__(self, name):
        self.name = name
    
    def execute(self, dic):
        for key, value in dic.items():
            print(key,value)

    def shutdown():
        pass

class A:
    def __init__(self, name):
        self.obj = X(name)
        print("Class A object created.")

    def execute(self, dic):
        self.obj.execute(dic)
        print(self.obj.name)
        print("Class A")
    
    def shutdown(self):
        print(self.obj.name)
        print("Class A")
    
class B:
    def __init__(self, name):
        self.obj = X(name)
        print("Class B object created.")

    def execute(self, dic):
        self.obj.execute(dic)
        print(self.obj.name)
        print("Class B")
    
    def shutdown(self):
        print(self.obj.name)
        print("Class B")

class C:
    def __init__(self, name):
        self.obj = X(name)
        print("Class C object created.")

    def execute(self, dic):
        self.obj.execute(dic)
        print(self.obj.name)
        print("Class B")
    
    def shutdown(self):
        print(self.obj.name)
        print("Class B")

if __name__=="__main__":
    objList = []
    execCnt = 0
    ACnt = 0
    BCnt = 0
    CCnt = 0
    while True:
        print("Enter 1 for new object.\nEnter 2 to delete an object.\nEnter 3 run execute method.\nEnter 4 to quit.\n")
        n = input()
        if n=='1':
            inp = input("Enter Class name(A/B/C): ")
            if inp=="A":
                objList.append(A(input("Enter object name: ")))
                ACnt += 1
            elif inp=="B":
                objList.append(B(input("Enter object name: ")))
                BCnt += 1
            elif inp=="C":
                objList.append(C(input("Enter object name: ")))
                CCnt += 1
            else:
                print("Wrong input.")

        elif n=='2':
            inp = input("Enter object name to delete: ")
            for item in objList:
                if inp == item.obj.name:
                    objList.remove(item)
                    del item.obj
                    del item

                    print("Object deleted.")
        
        elif n=='3':
            inp = input("Enter object name to run execute method: ")
            for item in objList:
                if inp == item.obj.name:
                    d = int(input("Enter no. of dictionary elements: "))
                    print("Enter dictionary content:\n")
                    dic = {}
                    for _ in range(d):
                        dic[input("Key:")] = input("Value:")
                    item.execute(dic)
                    execCnt += 1
        
        elif n=='4':
            print("No. of times Class A object invoked =",ACnt)
            print("No. of times Class B object invoked =",BCnt)
            print("No. of times Class C object invoked =",CCnt)
            print("No. of times execute() method invoked =",execCnt)
            break

        else:
            print("Wrong input.")
    