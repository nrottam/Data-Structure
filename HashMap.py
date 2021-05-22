# Need to impliment

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for x in range(self.MAX)]

    def print(self):
        print(self.arr)

    def gethash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self,key,data):
        self.arr[self.gethash(key)] = data

    def __getitem__(self,key):
        return self.arr[self.gethash(key)]


if __name__ == '__main__':
    t = HashTable()
    t["march 6"] = 120
    t["march 8"] = 67
    t["march 9"] = 4
    t["march 17"] = 459
    t.print()
    print(t["march 6"])