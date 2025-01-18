---

### **2. Python Code**

```python
# Linear and Binary Search Implementation

# Linear Search
def linear_search(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search
def binary_search(arr, target):
    
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Main Function
if __name__ == "__main__":
    # Input array
    numbers = [1, 3, 5, 7, 9, 11, 13, 15]
    print("Array:", numbers)
    target = int(input("Enter a number to search: "))

    # Linear Search
    linear_index = linear_search(numbers, target)
    print(f"Linear Search: {'Found at index ' + str(linear_index) if linear_index != -1 else 'Not Found'}")

    # Binary Search
    binary_index = binary_search(numbers, target)
    print(f"Binary Search: {'Found at index ' + str(binary_index) if binary_index != -1 else 'Not Found'}")
