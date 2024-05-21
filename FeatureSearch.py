# get features in arr

# empty node
# create children
# evaluate children
# expand best child
# repeat till last set



class Node(object):
    def __init__(self, feature):
        self.parents = []
        self.children = []
        self.feature = feature
    def add_child(self, obj):
        self.children.append(obj)
    def add_parent(self, obj):
        self.parents.append(obj)
