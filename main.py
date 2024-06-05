from FeatureSearch import BackwardElimination, ForwardSelection, FeatureSearch

#from Harrison Cooper found on class Piazza 
def loadData(self, filename = "small-test-dataset.txt"):
    self.dataVals= {} #dictionary to hold the data

    file = open(filename, 'r')
    data = file.readline() #read all the lines into a list 

    for row in data: 
        row = row.split('\n')
        row = row[0].split(' ')
        row.remove('')

        classVal = int(row[0][0]) #getting the instance class 

        for i in row[1:]:
            for j in i.split():
                instances = self.dataVals.get(classVal, [])
                instances.append(float[j]) 
                self.dataVals[classVal] = instances

print("Welcome to Ojasvi, William, Hailie, and Brandon's Feature Selection Algorithm.")

num_features = int(input("Please enter total number of features: "))
features = list(range(1, num_features + 1))

alg_num = int(input(f"""
Type the number of the algorithm you want to run.
    Forward Selection
    Backward Elimination
"""))

if alg_num == 1:
    alg = ForwardSelection(features)
elif alg_num == 2:
    alg = BackwardElimination(features)
else:
    print("Invalid algorithm selection.")
    exit(1)


feature_search = FeatureSearch(alg)
feature_search.search()
