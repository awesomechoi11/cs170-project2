import random
import copy
from Classifier import Validate
import numpy as np 
import matplotlib.pyplot as plt


class BackwardElimination:
    def __init__(self, all_features):
        self.all_features = all_features
        self.initialFeatures = all_features
        # pass

    def expand(self, current_node):
        # we expand by checking if current node has a feature for each feature in all_features
        # and add that new node
        for feature in self.all_features:
            if feature in current_node.features:
                # reset child
                child = copy.deepcopy(current_node)
                child.accuracy = None
                # add parent to child
                child.parents = [current_node]
                child.children = []
                child.features.remove(feature)

                # add child to parent
                current_node.add_child(child)
    
    def initial_print(self,current_node):
        print(f"Using all features and 1-NN evaluation, I get an accuracy of {current_node.accuracy:.1f}%")

    def evaluate(self, node, data, labels):
        return Validate(node.features, data, labels)

    
class ForwardSelection:
    def __init__(self, all_features):
        self.all_features = all_features
        self.initialFeatures = []
        # pass

    def expand(self, current_node):
        # we expand by checking if current node has a feature for each feature in all_features
        # and add that new node
        for feature in self.all_features:
            if feature not in current_node.features:
                # reset child
                child = copy.deepcopy(current_node)
                child.accuracy = None
                # add parent to child
                child.parents = [current_node]
                child.children = []
                child.add_feature(feature)

                # add child to parent
                current_node.add_child(child)
        
    def initial_print(self,current_node):
        print(f"Using no features and 1-NN evaluation, I get an accuracy of {current_node.accuracy:.1f}%")

    def evaluate(self, node, data, labels):        
        return Validate(node.features, data, labels)

class FeatureSearch:
    def __init__(self, Alg_class,filename, normalize = False):
        # load data first
        self.instance_labels = []
        self.instance_vectors = []
        self.loadData(filename, normalize)

        features = list(range(1,  len(self.instance_vectors[0])))
        alg = Alg_class(features)
        # empty array for intial features
        self.root = Node(alg.initialFeatures)
        self.expand = alg.expand
        self.evaluate = alg.evaluate
        self.all_features = alg.all_features
        self.alg = alg

    def loadData(self, filename, normalize):
        with open(filename, 'r') as file:
            # Read all lines from the file
            data = file.readlines()

        for row in data: 
            row = row.strip().split()

            label = int(float(row[0]))
            self.instance_labels.append(label)
            # convert to number
            instance = [float(val) for val in row[1:]]
            self.instance_vectors.append(instance)
        if(normalize):
            data = np.array(self.instance_vectors)
            data_min = np.min(data, axis=0)
            data_max = np.max(data, axis=0)
            data_normalized = (data - data_min) / (data_max - data_min)

            self.instance_vectors = data_normalized.tolist()

    def search(self):
        # default best node is root
        current_node = self.root
        best_node = current_node
        worst_node = current_node
        node_Trace = [current_node]
        current_node.accuracy = self.evaluate(current_node,self.instance_vectors,self.instance_labels)
        prev_accuracy = 0
        self.alg.initial_print(current_node)
        print("Beginning search.")

        # loop will only last the length of features
        for i in self.all_features:
            self.expand(current_node)
            children = current_node.children
            # update accuracy for all children
            best_child = None
            worst_child = None
            for child in children:
                accuracy = self.evaluate(child,self.instance_vectors,self.instance_labels)
                child.accuracy = accuracy
                if best_child == None:
                    best_child = child
                else:
                    if(best_child.accuracy < child.accuracy):
                        best_child = child
                if worst_child == None:
                    worst_child = child
                else:
                    if(worst_child.accuracy > child.accuracy):
                        worst_child = child
                print(f"    Using feature(s) {child.features} accuracy is {child.accuracy:.1f}%")
            best_feature = best_child.features
            node_Trace.append(best_child)
            print(f"Feature set {best_feature} was best, accuracy is {best_child.accuracy:.1f}%")
            if(best_node.accuracy < best_child.accuracy):
                best_node = best_child
            if(worst_node.accuracy > worst_child.accuracy):
                worst_node = worst_child
            if(prev_accuracy > best_child.accuracy):
                print("(Warning, Accuracy has decreased!)")
            current_node = best_child
            prev_accuracy = best_child.accuracy
            # current_node = worst_child
            # prev_accuracy = worst_child.accuracy

        print(f"Finished search!! The best feature subset is {best_node.features}, which has an accuracy of {best_node.accuracy:.1f}%")
        self.best_node = best_node
        self.worst_node = worst_node
        return best_node, worst_node

    def draw_plot(self, feature1, feature2):
        subsetData = np.array(self.instance_vectors)[:, (np.array([feature1,feature2]) - 1).tolist()]
        plt.figure(figsize=(4,4))
        
        labels = np.array(self.instance_labels)
        data = np.array(self.instance_vectors)

        for label in np.unique(labels):
            plt.scatter(
                data[labels == label, feature1], 
                data[labels == label, feature2], 
                label=f'Class {label}',
                alpha=0.6
            )

        plt.xlabel(f'Feature {feature1}')
        plt.ylabel(f'Feature {feature2}')
        plt.legend()
        plt.title(f'Feature {feature1} vs Feature {feature2}')
        plt.grid(True)
        # Save the plot to a file
        plt.savefig(f'Feature {feature1} vs Feature {feature2}')
        plt.close()

class Node:
    def __init__(self, features):
        self.parents = []
        self.children = []
        self.features = features
        self.accuracy = None

    def add_child(self, obj):
        self.children.append(obj)
        obj.add_parent(self)
    
    def add_parent(self, obj):
        self.parents.append(self)

    def add_feature(self, feature):
        self.features.append(feature)



