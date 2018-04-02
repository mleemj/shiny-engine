class PNode(object):
    def __init__(self, L, R):
        self._left = L
        self._right = R

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, L):
        self._left = L

    def find_odd_number(self, left, right):
        odd_number = []
        for indx in range(left, right + 1):
            if indx % 2 is not 0:
                odd_number.append(indx)
        return odd_number

    def findNumber(self, arr, k):
        for indx in range(1, len(arr)-1):
            if arr[indx] is k:
                print('YES')
                return
        print('NO')

if __name__ == '__main__':
    node = PNode(3, 5)
    node.findNumber([5,1,2,3,4,5], 1)
    node.findNumber([3,4,5],1)

    list_odd_numbers = node.find_odd_number(3, 5)
    print(list_odd_numbers)
