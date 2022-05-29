# Quick sort 

## Overview
  - Quick sort is an algorithm of reorder a list in ascending order.
  - Quick sort use the concept of divide and conquer algorithm.

## Quick sort main idea
The main idea of quicksort is to pick an element as a pivot and partition the array around the pivot. When we partition the array we sort the elements in a manner way to make all small elements before the pivot and all the greatest elements after the pivot, this is the core of partition part.

## What pivot mean?
Pivot is the value within the partitioning space that I want to find a position for.

## What does **i** variable do?
Remember the last position that an element was placed in , that was less than the pivot.

## What does **j** variable do?
Scan from left boundary to right - 1 boundary. 

## How to pick the pivot ?
- There are many different way of picking the pivot:
  1. Always pick first element as pivot.
  2. Always pick last element as pivot.
  3. Pick a random element as pivot.
  4. Pick median as pivot.

In this article I will pick the last element as a pivot. Other ways of picking pivot has a slightly different implementation.



## Pseudoscope 
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        DEFINE position <-- Partition(arr, left, right)
        QuickSort(arr, left, position - 1)
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    DEFINE pivot <-- arr[right]
    DEFINE i <-- left - 1
    for j <-- left to right do
        if arr[j] <= pivot
            i++
            Swap(arr, i, j)

     Swap(arr, i+1, right)
     return i + 1

ALGORITHM Swap(arr, i, j)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[j]
    arr[j] <-- temp
```

## Code implementation

```python
def quick_sort(arr, left, right):
    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position-1)
        quick_sort(arr, position+1, right)


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i+1, right)
    return i+1


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
```


## Let's trace the code
Assume this sample array `[8, 4, 3, 2]`

```python
quick_sort([8, 4, 3, 2], 0, len(arr)-1)

Pass 1:
    if left < right: # 0 < 3 ==> True
            position = partition(arr, left, right) # partition([8, 4, 3, 2], 0, 3) position = 0
            quick_sort(arr, left, position-1) # quick_sort([2, 4, 3, 8], 0, -1) @Pass 2
            quick_sort(arr, position+1, right) # quick_sort([2, 4, 3, 8], 1, 3) @Pass 3

    partition:
        arr: [8, 4, 3, 2], left: 0, right: 3
        pivot = 2, i = - 1
        for j in range(0, 3):
            if arr[j] <= pivot:
                i += 1
                swap(arr, i, j)
        j = 0, i = - 1
        if 8 <= 2 ==> False

        j = 1, i = - 1
        if 4 <= 2 False

        j = 2, i = - 1
        if 3 <= 2 ==> False

        swap([8, 4, 3, 2], 0, 3)
            temp = 8
            arr[0] = 2
            arr[3] = 8
        
        return 0

position = 0
arr = [2, 4, 3, 8]

Pass 2:
    quick_sort([2, 4, 3, 8], 0, -1)
    if 0 < -1  ==> False

Pass 3:
    quick_sort([2, 4, 3, 8], 1, 3)

    if 1 < 3: # 1 < 3 ==> True
            position = partition(arr, left, right) # partition([2, 4, 3, 8], 1, 3) position = 3
            quick_sort(arr, left, position-1) # quick_sort([2, 4, 3, 8], 1, 2) @Pass 4
            quick_sort(arr, position+1, right) # quick_sort([2, 3, 4, 8], 4, 3) @Pass 7

    Partition:
        arr: [2, 4, 3, 8], left: 1, right: 3
        pivot = 8, i = 0
        for j in range(1, 3):
            if arr[j] <= pivot:
                i += 1
                swap(arr, i, j)

        j = 1, i = 0
        if 4 <= 8 ==> True
            i = 1
            swap([2, 4, 3, 8], 1, 1) => The array will not change
        
        j = 2, i = 1 
        if 3 <= 8 ==> True
            i = 2
            swap([2, 4, 3, 8], 2, 2) => The array will not change
        
        swap([2, 4, 3, 8], 3, 3)
            temp = 8
            arr[3] = 8
            arr[3] = 8
        
        return 3

position = 3
arr = [2, 4, 3, 8]

Pass 4:
    quick_sort([2, 4, 3, 8], 1, 2)

    if 1 < 2:
        position = partition(arr, left, right) # partition([2, 4, 3, 8], 1, 2) position = 1
        quick_sort(arr, left, position-1) # quick_sort([2, 3, 4, 8], 1, 0) @Pass 5
        quick_sort(arr, position+1, right) # quick_sort([2, 3, 4, 8], 2, 2) @Pass 6

    Partition:
        arr = [2, 4, 3, 8], left: 1, right = 2
        pivot = 2, i = 0
        for j in range(1, 2):
            if arr[j] <= pivot:
                i += 1
                swap(arr, i, j)

        j = 1, i = 0
        if 4 <= 3 ==> False
                       
        swap([2, 4, 3, 8], 1, 2)
            temp = 4
            arr[1] = 3
            arr[2] = 4

        return 1
position = 1
arr = [2, 3, 4, 8]

Pass 5:
    quick_sort([2, 3, 4, 8], 1, 0)
    if 1 < 0  ==> False

Pass 6:
    quick_sort([2, 3, 4, 8], 2, 2)
    if 2 < 2 ==> False

Pass 7:
    quick_sort([2, 3, 4, 8], 4, 3)
    if 4 < 3 False 

```

## Efficiency
  - Time Big-O(n<sup>2</sup>)
  - Space Big-O(n)