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
    

class Validator:
    def __init__(self):
        pass

    def Validate(self, classifier, featureSubset, data, labels):
        correctPredictions = 0
        totalInstances = len(data)

        #extracting the feature subset from the data
        subsetData = np.array(data)[:, featureSubset]

        for i in range(totalInstances):
            prediction = classifier.Test(subsetData[i])
            if prediction == labels[i]:
                correctPredictions += 1
        
        accuracy = correctPredictions / totalInstances
        return accuracy