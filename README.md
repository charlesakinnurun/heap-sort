<h1 align="center">Heap Sort</h1>

## Overview

**Heap Sort** is an efficient comparison-based sorting algorithm that uses a binary heap data structure.

It works by first converting the list into a max heap, then repeatedly removing the largest element and placing it at the end of the array.

It is known for being:

* ✅ O(n log n) in all cases
* ✅ In-place (no extra memory needed)
* ✅ Good for large datasets
* ❌ Not stable

<a href="/src/main.py">Check out for source code</a>

---

## ⚙️ How Heap Sort Works

Heap Sort consists of two main phases:

### 1️⃣ Build a Max Heap

Rearrange the array so that it satisfies the max-heap property:

* Every parent node is greater than its children
* The largest element is at the root

Example array:

```
[4, 10, 3, 5, 1]
```

After building max heap:

```
[10, 5, 3, 4, 1]
```

---

### 2️⃣ Extract Elements from Heap

1. Swap the root (largest element) with the last element
2. Reduce heap size by one
3. Heapify the root again
4. Repeat until sorted

Step example:

```
[10, 5, 3, 4, 1]
→ swap 10 with 1
[1, 5, 3, 4, 10]
→ heapify remaining
[5, 4, 3, 1, 10]
```

Continue until sorted.

Final result:

```
[1, 3, 4, 5, 10]
```

---

## ⏱️ Time & Space Complexity

| Case       | Time Complexity |
| ---------- | --------------- |
| Best Case  | O(n log n)      |
| Average    | O(n log n)      |
| Worst Case | O(n log n)      |

**Space Complexity:** O(1) (in-place)

---

## 🧠 Python Implementation

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue heapifying if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


# Example usage
numbers = [4, 10, 3, 5, 1]
print(heap_sort(numbers))
# Output: [1, 3, 4, 5, 10]
```

---

## 🧪 Example Runs

### Example 1

Input:

```
[12, 11, 13, 5, 6, 7]
```

Output:

```
[5, 6, 7, 11, 12, 13]
```

### Example 2

Input:

```
[9, 4, 7, 1, 3, 6]
```

Output:

```
[1, 3, 4, 6, 7, 9]
```

---

## 👍 Advantages

* Guaranteed O(n log n) performance
* In-place sorting (no extra memory needed)
* Works well when memory is limited
* Good worst-case performance

---

## 👎 Disadvantages

* Not stable
* Slower in practice than quicksort for many datasets
* Heap structure adds conceptual complexity

---

## 📌 When to Use Heap Sort

Use Heap Sort when:

* Memory usage must be minimal
* Worst-case performance must be guaranteed
* Working with priority queues or heap structures
* Sorting very large datasets in-place

---

## 🏁 Summary

Heap Sort is a powerful and memory-efficient sorting algorithm with guaranteed performance. While it is not stable and can be slightly slower than quicksort in practice, its in-place operation and consistent O(n log n) runtime make it valuable in many real-world applications.
