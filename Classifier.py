import numpy as np 

class Classifier:
    def __init__(self):
        self.trainingData = None
        self.trainingLabels = None

    def Train(self, trainingData, trainingLabels):
        #storing the data and labels 
        self.trainingData = np.array(trainingData)
        self.trainingLabels = np.array(trainingLabels)

    def Test(self, testInstance):
        #classifying a test instance based on the NN from the training data
        testInstance = np.array(testInstance)
        distances = np.linalg.norm(self.trainingData - testInstance, axis=1)
        nnIndex = np.argmin(distances)
        return self.trainingLabels[nnIndex]
    
    
#class Validator: