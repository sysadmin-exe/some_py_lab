# WHAT DOES THIS SCRIPT DO? 
# Uses recursion to sort a list of numbers by splitting the list to individual numbers
# and merging it back together starting with the smallest numbers

items = [3, 65, 32, 12, 23, 78, 100]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
    
    # recursively break down the array
        mergesort(leftarr)
        mergesort(rightarr)

        i = 0
        j = 0
        k = 0

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1


        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1
        
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1
                
print(items)
mergesort(items)
print(items)