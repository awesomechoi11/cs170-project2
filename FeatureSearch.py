import random
import copy
# get features in arr

# empty node
# create children
# evaluate children
# expand best child
# repeat till last set

class BackwardElimination:
    def __init__(self, all_features):
        self.all_features = all_features
        self.initialFeatures = all_features

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
        print(f"Using all features and “random” evaluation, I get an accuracy of {current_node.accuracy:.1f}%")

    def evaluate(self, node):
        # Assign a random evaluation value to each feature subset
        return random.uniform(0, 1) * 100
    
class ForwardSelection:
    def __init__(self, all_features):
        self.all_features = all_features
        self.initialFeatures = []

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
        print(f"Using no features and “random” evaluation, I get an accuracy of {current_node.accuracy:.1f}%")

    def evaluate(self, node):
        # Assign a random evaluation value to each feature subset
        return random.uniform(0, 1) * 100

class FeatureSearch:
    def __init__(self, alg):
        # empty array for intial features
        self.root = Node(alg.initialFeatures)
        self.expand = alg.expand
        self.evaluate = alg.evaluate
        self.all_features = alg.all_features
        self.alg = alg

    def search(self):
        # default best node is root
        current_node = self.root
        best_node = current_node
        node_Trace = [current_node]
        current_node.accuracy = self.evaluate(current_node)
        prev_accuracy = 0
        self.alg.initial_print(current_node)
        print("Beginning search.")

        # loop will only last the length of features
        for i in self.all_features:
            self.expand(current_node)
            children = current_node.children
            # update accuracy for all children
            best_child = None
            for child in children:
                accuracy = self.evaluate(child)
                child.accuracy = accuracy
                if best_child == None:
                    best_child = child
                else:
                    if(best_child.accuracy < child.accuracy):
                        best_child = child
                print(f"    Using feature(s) {child.features} accuracy is {child.accuracy:.1f}%")
            best_feature = best_child.features
            node_Trace.append(best_child)
            print(f"Feature set {best_feature} was best, accuracy is {best_child.accuracy:.1f}%")
            if(best_node.accuracy < best_child.accuracy):
                best_node = best_child
            current_node = best_child
            if(prev_accuracy > best_child.accuracy):
                print("(Warning, Accuracy has decreased!)")
            prev_accuracy = best_child.accuracy

        print(f"Finished search!! The best feature subset is {best_node.features}, which has an accuracy of {best_node.accuracy:.1f}%")
        return best_node

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



