from FeatureSearch import BackwardElimination, ForwardSelection, FeatureSearch

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
