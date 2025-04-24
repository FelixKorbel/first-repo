print("life-science-experiments on CubeSats")
print("what ist possible? What is not possible?")
print("What parameters are needed?")

file_path = "exemple.txt"

try: 
    with open(file_path, 'x') as file:
        file.write("life_science_experimets on CubeSats. What is possible? What is not possible?"
                  "What parameters are needed?")
except FileExistsError:
    print("the file '{file_path}' already exists")