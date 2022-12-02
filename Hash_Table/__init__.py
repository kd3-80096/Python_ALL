## importing the required libraries
class HashTable:
    def __init__(self):
        self.MAX = 9  ## setting the max elements that we need for hash table
        ## List Comprehension
        self.arr = [None for i in range(self.MAX)]

    ## Method to calculate the hash function for a given value
    def get_hash(self, key):
        hash = 0
        for char in key:
            ## ord function in python helps us to get ascii value of
            ## any character
            hash += ord(char)
        return hash % self.MAX

    ## Method definition of standard operators as functions in Python
    ## getitem - to fetch the value of given index inside hash table

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    ## setitem - to set the value corresponding to key inside hash table
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    ## delitem - to delete the values inside the hash table for a given key
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

s = HashTable()
s['AI20MTECH14018'] = 69
s['AI20MTECH14023'] = 66

## getting the index of element
print("Index of number AI20MTECH14018 = ",s.get_hash('AI20MTECH14018'))

## getting the index of element
print("Index of number AI20MTECH14023 = ",s.get_hash('AI20MTECH14023'))

print("Array values to be printed:-")
print(s.arr)


## reading the student_score.csv file
student_score = []
with open("C:\\Users\\ASUS\\Desktop\\pandas-demo\\Ineuron\\Python_DSA\\Code\\student_score.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        roll_num = tokens[0]
        score = float(tokens[1])
        student_score.append([roll_num,score])

print("All student numbers in the csv file = ",student_score,end="\n")

