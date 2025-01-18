# Binary Search and Linear Search Project

## Project Overview
This project showcases the implementation of two fundamental searching algorithms: **Binary Search** and **Linear Search**. 
It is designed to reinforce understanding of algorithmic efficiency and demonstrate the ability to write clean, efficient, and well-documented code.

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Running the Program
1. Clone this repository:
   ```bash
   git clone (https://github.com/Ahmed-1042/Searching-Algorithms-)
   ```
2. Navigate to the project directory:
   ```bash
   cd Searching Algorithms
   ```
3. Execute the script:
   ```bash
   python search_algorithms.py
   ```

---

## Algorithm Details

### **Binary Search**
- Works on sorted arrays by dividing the search interval in half.
- **Best Case**: O(1)  
- **Worst Case**: O(log n)  
- **Example Worst Case**: Searching for a non-existent element like `100` in `[1, 3, 5, 7, 9]`.

### **Linear Search**
- Traverses the list sequentially to find the target.
- **Best Case**: O(1)  
- **Worst Case**: O(n)  
- **Example Worst Case**: Searching for the last element or a non-existent element.

---

## Output Example

For an array `[1, 3, 5, 7, 9]` and target `7`:
- **Binary Search Output**: `Element found at index 3`
- **Linear Search Output**: `Element found at index 3`

---

## Notes
- Binary Search is faster for sorted arrays but requires preprocessing (sorting).
- Linear Search works on both sorted and unsorted arrays.
