from FeatureSearch import BackwardElimination, ForwardSelection, FeatureSearch


print("Welcome to Ojasvi, William, Hailie, and Brandon's Feature Selection Algorithm.")

file_num = int(input(f"""
Type the number of the file to test :
(1)    CS170_Spring_2024_Large_data__40.txt
(2)    CS170_Spring_2024_Small_data__40.txt
(3)    large-test-dataset.txt
(4)    small-test-dataset.txt
"""))

if file_num == 1:
    filename = "CS170_Spring_2024_Large_data__40.txt"
elif file_num == 2:
    filename = "CS170_Spring_2024_Small_data__40.txt"
elif file_num == 3:
    filename = "large-test-dataset.txt"
elif file_num == 4:
    filename = "small-test-dataset.txt"
else:
    print("Invalid file selection.")
    exit(1)

alg_num = int(input(f"""
Type the number of the algorithm you want to run.
(1)    Forward Selection
(2)    Backward Elimination
"""))

if alg_num == 1:
    alg = ForwardSelection
elif alg_num == 2:
    alg = BackwardElimination
else:
    print("Invalid algorithm selection.")
    exit(1)

normalize_data = True
feature_search = FeatureSearch(alg,filename, normalize_data)
feature_search.search()

# feature_search.draw_plot(7,2) #74
# feature_search.draw_plot(5,3) # 93
