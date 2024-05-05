def insert_max_heap(heap: list[int], val: int):
    index = len(heap)
    heap.append(val)
    while True:
        parent = get_parent(index)
        if parent == -1:
            break

        if heap[parent] >= heap[index]:
            break

        aux = heap[parent]
        heap[parent] = heap[index]
        heap[index] = aux
        index = parent

    return heap


def insert_min_heap(heap: list[int], val: int):
    index = len(heap)
    heap.append(val)

    while True:
        parent = get_parent(index)
        if parent == -1:
            break

        if heap[parent] <= heap[index]:
            break

        aux = heap[parent]
        heap[parent] = heap[index]
        heap[index] = aux
        index = parent

    return heap


def get_parent(x): return (x - 1) // 2
def get_left(x): return x * 2 + 1
def get_right(x): return x * 2 + 2


def main():
    print("start inserting numbers on the heap")
    heap = []
    while True:
        x = input()
        try:
            x = int(x)
            heap = insert_max_heap(heap, x)
            print(heap)
        except:
            print('bye!')
            break


if __name__ == "__main__":
    main()
