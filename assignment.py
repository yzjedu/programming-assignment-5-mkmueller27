# Programmer: Kristina Mueller
# Course: CS701/GB-731, Dr. Yalew
# Date: 08/18/2024
# Programming Assignment: 5
# Function that creates a 2D list filled with consecutive integers starting from 1.
# Function that returns the sum of the elements in a specified row of a 2D list.
# Function that returns the maximum value in a specified column of a 2D list.
# Function that returns a 1D list containing all elements of the 2D list.


def main():
    # Task 1: Create a 2D list of 4x4 initialized with numbers from 1 to 16
    COLUMNS = 4
    ROWS = 4
 
    rows = [
        "Row 1",
        "Row 2",
        "Row 3",
        "Row 4"]
    

    content = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    def new_table(rows, content):
        table = []
        for i in range(ROWS):
            print("%6s" % rows[i], end = " ")
            row = []
            for j in range(COLUMNS):
                print("%4d" % content[i][j], end = " ")
                row.append(content[i][j])
            table.append(row)
            print()
        return table
    
    my_table = new_table(rows, content)
    
    print(my_table)

    print(isinstance(my_table, list))


    # Task 2: Calculate the sum of the third row
    sum_row3 = sum(my_table[2])
    print(sum_row3)

    # Task 3: Find the maximum element in the last column
    
    col4 = list(row[-1] for row in my_table)
    print(col4)
    print(max(col4))
    
    # Task 4: Flatten the matrix into a 1D list
    flat_list0 = list(my_table)
    print(flat_list0)
    flat_list = sum(flat_list0, [])
    print(flat_list)

    print(isinstance(flat_list, list))
    
    # Task 5: Perform list modifications
    # Append an element to the list
    flat_list.append(- 1)
    print(flat_list)
    
    # Insert an element at a specific position
    flat_list.insert(0, 0)
    print(flat_list)
    
    # Sort the list
    
    flat_list.sort()
    print(flat_list)

    # Reverse the list
    flat_list [ : : -1]
    print(flat_list)
    #or
    flat_list.sort(reverse = True)
    print(flat_list)
    
    # Find the minimum and maximum elements
    #Minimum
    minimum = flat_list[0]
    for i in range(1, len(flat_list)) :
         if flat_list[i] < minimum :
            minimum = flat_list[i]
    print(minimum, " is minimum")
    #Maximum
    maximum = flat_list[0]
    for i in range(1, len(flat_list)) :
         if flat_list[i] > maximum :
            maximum = flat_list[i]
    print(maximum, " is maximum")

    # Find the index of a specific element
    res= flat_list.index(10)
    print(res)

    # Print all results: 
        #results are printed after respective code snippet

    # Task 6: Decision making - Check if the minimum value in the modified list is greater than 0
    if min(flat_list) > 0:
        print("Yes, minimum is greater than 0")
    else:
        print("No, minimum is not greater than 0")
    
    pass

if __name__ == "__main__":
    main()