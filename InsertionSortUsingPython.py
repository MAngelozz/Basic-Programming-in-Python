def insertionSort(List):
    for i in range(1, len(List)):
        currentNumber = List[i]
        for j in range(i - 1, -1, -1):
            if List[j] >currentNumber :
                List[j], List[j + 1] = List[j + 1], List[j]
            else:
                List[j + 1] = currentNumber
                break
    return List
if __name__ == '__main__':
    List = [3,7,2,8,4,1,9,5]
    print('Sorted List: ',insertionSort(List))