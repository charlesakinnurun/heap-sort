import math

def heap_sort(arr):
    """
    Main function to perform Heap Sort on an array.
    
    Heap Sort has two main phases:
    1. Build a Max Heap: Reorganize the array into a heap structure.
    2. Extract elements: Repeatedly remove the largest element from the heap 
       and move it to the end of the array, then rebuild the heap.
    """
    n = len(arr)

    print("--- PHASE 1: BUILDING MAX HEAP ---")
    # Build a maxheap.
    # We start from the last non-leaf node and work our way up.
    # The last non-leaf node is at index (n//2 - 1).
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print_visual_heap(arr, n)

    print("\n--- PHASE 2: EXTRACTING ELEMENTS ---")
    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Move current root (largest element) to the end of the array
        # This effectively 'sorts' that element into its final position.
        arr[i], arr[0] = arr[0], arr[i]
        
        print(f"Swap root {arr[i]} with end {arr[0]}. Sorted portion: {arr[i:]}")
        
        # Call max heapify on the reduced heap (excluding the already sorted elements)
        heapify(arr, i, 0)
        print_visual_heap(arr, i)

def heapify(arr, n, i):
    """
    To heapify a subtree rooted with node i which is an index in arr[].
    n is size of heap.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index = 2*i + 1
    right = 2 * i + 2  # right child index = 2*i + 2

    # If left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # If right child of root exists and is greater than the largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def print_visual_heap(arr, n):
    """
    A utility function to print a visual representation of the binary heap.
    Only prints the active heap portion (size n).
    """
    if n == 0:
        return
    
    # Calculate the depth of the tree
    depth = int(math.log2(n)) + 1
    index = 0
    
    print("\nCurrent Heap Structure:")
    for level in range(depth):
        # Calculate spacing for visual alignment
        level_nodes = 2**level
        padding = " " * (2**(depth - level + 1))
        gap = " " * (2**(depth - level + 2) - 2)
        
        line = padding
        for _ in range(level_nodes):
            if index < n:
                # Print the number with padding for consistent width
                line += f"{arr[index]:02d}" + gap
                index += 1
        print(line)
    print("-" * 30)

def main():
    # Example 1: Standard Unsorted Array
    example_1 = [12, 11, 13, 5, 6, 7]
    print(f"Initial Array: {example_1}")
    heap_sort(example_1)
    print(f"Final Sorted Array: {example_1}")
    
    # Example 2: Reverse Sorted Array
    print("\n" + "="*40)
    example_2 = [1, 2, 3, 4, 5]
    print(f"Initial Array (Worst Case): {example_2}")
    heap_sort(example_2)
    print(f"Final Sorted Array: {example_2}")

if __name__ == "__main__":
    main()