import numpy as np 

class NNClassifier:
    def __init__(self):
        self.trainingData = None
        self.trainingLabels = None

    def Train(self, trainingData, trainingLabels):
        #storing the data and labels 
        self.trainingData = np.array(trainingData)
        self.trainingLabels = np.array(trainingLabels)

    def Test(self, testInstance, testIndex):
        #classifying a test instance based on the NN from the training data
        testInstance = np.array(testInstance)
        distances = np.linalg.norm(self.trainingData - testInstance, axis=1)
    
        min_distance = float('inf')
        min_index = -1
        # print(distances)
        for i, distance in enumerate(distances):
            if i != testIndex and distance < min_distance:
                min_distance = distance
                min_index = i

        nnIndex = min_index
        # print(min_distance)
        return self.trainingLabels[nnIndex]
    

    
def Validate(featureSubset, data, labels, classifier = NNClassifier()):
    correctPredictions = 0
    totalInstances = len(data)
    #extracting the feature subset from the data
    subsetData = np.array(data)[:, (np.array(featureSubset) - 1).tolist()]
    classifier.Train(subsetData, labels)


    for i in range(totalInstances):
        prediction = classifier.Test(subsetData[i],i)
        if prediction == labels[i]:
            correctPredictions += 1
    
    accuracy = correctPredictions / totalInstances
    return accuracy * 100