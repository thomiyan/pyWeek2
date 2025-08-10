# Python List Operations Example

## Overview

This project demonstrates basic and intermediate operations you can perform on Python lists. It is intended for beginners who want to get hands-on experience with Python's list data structure and its useful methods for manipulating data.

---

## Table of Contents

- [Features](#features)
- [Code Walkthrough](#code-walkthrough)
- [How to Run](#how-to-run)
- [Output Example](#output-example)
- [Customization](#customization)
- [Further Reading](#further-reading)
- [License](#license)

---

## Features

- Creating and initializing lists
- Appending elements to a list
- Inserting elements at a specific index
- Extending a list with another list
- Removing elements (using `pop`)
- Sorting a list
- Finding the index of a specific element
- Printing the state of the list after each operation

---

## Code Walkthrough

The script performs the following steps:

1. **Create an Empty List**  
   Initializes an empty list called `myList`.

2. **Append Elements**  
   Adds the values 10, 20, 30, and 40 to the end of `myList`.

3. **Insert at a Specific Position**  
   Inserts the value 15 at the second position (index 1).

4. **Extend with Another List**  
   Extends `myList` with `[50, 60, 70]` by concatenating the lists.

5. **Remove the Last Element**  
   Removes the last element from `myList` using the `pop()` method.

6. **Sort the List**  
   Sorts the list in ascending order.

7. **Find the Index of a Value**  
   Finds and prints the index of the value `30` in the sorted list.

Each step prints the state of the list or the result, helping you follow the changes.

---

## How to Run

1. **Copy the Code**

   Save the following code to a file, for example, `list_operations.py`:

   ```python
   # list operations

   # 1: create an empty list
   myList = []
   print(myList, f" : My List Before Append")

   # 2: Append elements 10, 20, 30, 40 to the list
   myList.append(10)
   myList.append(20)
   myList.append(30)
   myList.append(40)
   print(myList, f" : My List After Append")

   # 3: Insert the value 15 at the second position
   myList.insert(1, 15)
   print(myList, f" : My List After Inserting 15")

   # 4: Extend the list with another list [50, 60, 70]
   mySecondList = [50, 60, 70]
   myList.extend(mySecondList)
   print(myList, f" : My List After Extending")

   # 5: Remove the last element from the list
   myList.pop()
   print(myList, f" : My List Ater Removing the last")

   # 6: Sort the list in ascending order
   myList.sort()
   print(myList, f" : My List After Sorting")

   # 7: Find and print the index of the value 30
   index_of_30 = myList.index(30)
   print("Index of 30:", index_of_30)
   ```

2. **Run the Script**

   Open your terminal or command prompt, navigate to the folder containing the file, and run:

   ```sh
   python list_operations.py
   ```

---

## Output Example

Example output when running the script:

```text
[]  : My List Before Append
[10, 20, 30, 40]  : My List After Append
[10, 15, 20, 30, 40]  : My List After Inserting 15
[10, 15, 20, 30, 40, 50, 60, 70]  : My List After Extending
[10, 15, 20, 30, 40, 50, 60]  : My List Ater Removing the last
[10, 15, 20, 30, 40, 50, 60]  : My List After Sorting
Index of 30: 3
```

---

## Customization

- **Change Elements**: Edit the elements being added, inserted, or extended to see how the behavior changes.
- **Try Other List Methods**: Experiment with methods like `remove`, `reverse`, or slicing for more practice.
- **Add Error Handling**: For example, try to find the index of an element that is not in the list and handle the resulting exception.

---

## Further Reading

- [Python Lists - Official Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python List Methods](https://docs.python.org/3/library/stdtypes.html#list)

---

## License

This script is provided for educational purposes. Feel free to modify and use it as you like.

---
