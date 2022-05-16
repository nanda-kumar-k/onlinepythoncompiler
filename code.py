def bubblesort(elements):
  # Looping from size of array from last index[-1] to index [0]
  for n in range(len(elements)-1, 0, -1):
    for i in range(n):
      if elements[i] > elements[i + 1]:
        # swapping data if the element is less than next element in the array
        elements[i], elements[i + 1] = elements[i + 1], elements[i]
elements = [39,12,18,85,72,10,2,18]
print("Unsorted list is,") 
print( elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)