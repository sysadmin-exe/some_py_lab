# WHAT DOES THIS SCRIPT DO? 
# Uses recursion to sort the items of a list - Bubble sort algorithm
# Start with the array length and decrement each time
def bubblesort(dataset):
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j + 1]:
                temp = dataset[j]
                dataset[j] = dataset[j + 1]
                dataset[j + 1] = temp
        print("Current state: ", dataset)  

def main():
    list1  = [3, 65, 32, 12, 23, 78, 100]
    bubblesort(list1)
    print("Result: ", list1)

if __name__ == "__main__":
    main()