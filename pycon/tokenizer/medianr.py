class Medianr(object):

    def findMedian(self, array):
        median_indx = len(array) // 2
        sorted_array = self.merge_sort(array)
        print(sorted_array[median_indx])
    '''
    [1], [2]
    
    [0], [1, 2]
    
    [4], [6]
    
    [5], [3]
    
    [4, 6], [3, 5]
    
    [0, 1, 2], [3, 4, 5, 6]
    '''
    def merge(self, sublist_1, sublist_2):
        print(sublist_1)
        print(sublist_2)
        print()
        i = j = 0
        sorted_list = []
        while len(sublist_1) > i and len(sublist_2) > j:
            if sublist_1[i] < sublist_2[j]:
                sorted_list.append(sublist_1[i])
                i += 1
            else:
                sorted_list.append(sublist_2[j])
                j += 1

        while i < len(sublist_1):
            sorted_list.append(sublist_1[i])
            i += 1

        while j < len(sublist_2):
            sorted_list.append(sublist_2[j])
            j += 1

        return sorted_list


    def merge_sort(self, unsorted):
        if len(unsorted) == 1:
            return unsorted
        mid_point = len(unsorted) // 2 # mid_point is floor
        u1 = unsorted[:mid_point]
        u2 = unsorted[mid_point:]

        s1 = self.merge_sort(u1)
        s2 = self.merge_sort(u2)

        return self.merge(s1, s2)


if __name__ == '__main__':
    medianr = Medianr()
    arr = [0,1,2,4,6,5,3]
    medianr.findMedian(arr)