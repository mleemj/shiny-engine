class Overlapper(object):
    def __init__(self):
        self.one_day = \
            set({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23})


    def overlap(self, arr_1, arr_2):
        start_array_1 = arr_1[0]
        end_array_1 = arr_1[1]

        start_array_2 = arr_2[0]
        end_array_2 = arr_2[1]

        for indx_a in range(start_array_1, end_array_1):
            for indx_b in range(start_array_2, end_array_2):
                if indx_a == indx_b:
                    return True

        return False

    def free_time_individual(self, start, end):
        start_time = start
        end_time = end + 1
        for indx in range(start_time, end_time):
            print('remove {}'.format(indx))
            if indx in self.one_day:
                self.one_day.remove(indx)
        print(self.one_day)

    def free_time_multiple(self, single_person_list_busy_time):
        for sbt in single_person_list_busy_time:
            sbt_start = sbt[0]
            sbt_end = sbt[1]
            print('{} {}'.format(sbt_start, sbt_end))
            self.free_time_individual(sbt_start, sbt_end)


if __name__ == '__main__':
    lap = Overlapper()
    lap.free_time_multiple([[4,5],[6,10],[12,14]])
    lap.free_time_multiple([[4,9],[13,16]])
    lap.free_time_multiple([[11,14]])

    # Example input (busy times)t:
    # [
    #   [[4,5],[6,10],[12,14]],
    #   [[4,9],[13,16]],
    #   [[11,14]]
    # ]

    # Example Output (free times):
    # [[0,4],[10, 11],[16,24]]


    # for i in range(0, 4):
    #     print(i)
    # is_overlap = lap.overlap([0,4], [2,5])
    # assert (is_overlap == True)
    # is_overlap = lap.overlap([1,2], [2,5])
    # assert (is_overlap == False)
    # is_overlap = lap.overlap([0,10], [11,13])
    # assert (is_overlap == False)




# Please write a function that given two intervals, determine whether they overlap.
# >>> overlap([0, 4], [2, 5])
"""
0, 1, 2, 3, 4
range(0, 4) -> 0, 1, 2, 3
2, 3, 4, 5
range(2, 5) -> 2, 3, 4
2, 3, 4
returns true if 2, 3 can be found in 2, 3, 4


"""
# True
# >>> overlap([1,2], [2, 5])
# False
# >>> overlap([0, 10], [11, 13])
# False