class Park(object):
    def __init__(self):
        pass

    def interset(self):
        s1 = set([1,2,3,4,5])
        s2 = set([3,4,5])
        s3 = set([7])
        print(len(s1.intersection(s3)) is 0)

if __name__ == '__main__':
    park = Park()
    park.interset()