from flask import Flask
from tokenizer.coroutils import coroutine
import os, re
from concurrent import futures
import time


"""
    Demonstrates the following concepts:
    1. Get resource from Flask instance folder
    2. Regular expression to tokenize string
    3. How to use functools.wrap a co-routine to prime a generator
    4. How to use concurrency futures
    5. How to use ThreadPoolExecutor 
"""
# app's default instance path works when running from command-line
# app = Flask(__name__)
# absolute path has to be provided when running application from PyCharm

app = Flask(__name__, instance_path='/Users/matthewlee/zulu/pycon/instance')
WORKERS = 3

class Tolkienizer(object):
    def __init__(self):
        self.swift_files = []
        self.brace_files = []

        for indx in range(1, 4):
            file_name = os.path.join(app.instance_path, indx.__str__())
            brace_name = os.path.join(app.instance_path, 'b{}'.format(indx))
            self.swift_files.append(file_name)
            self.brace_files.append(brace_name)

    def tolkienify_single(self, file_name):
        with app.open_instance_resource(file_name, mode='rt') as f1:
            print('tolkienify_one: {}'.format(file_name))
            contents = f1.read()
            self.tolken_basic_block(contents)

    def brace_multiple(self):
        print('brace_multiple start')
        workers = min(WORKERS, len(self.brace_files))
        with futures.ThreadPoolExecutor(workers) as executor:
            list_brace_futures = []
            for b in self.brace_files:
                future = executor.submit(self.brace_single, b)
                list_brace_futures.append(future)
                msg = 'Scheduled for brace={} future{}'.format(b, future)
                print(msg)

            print('brace_muliple executor complete submit')

            for f in list_brace_futures:
                single_result = f.result()
                msg = 'future:{} result:{!r} '.format(f, single_result)
                print(msg)
            print('brace_multiple complete')

    def tolkienify_multiple(self):
        print('tolkienify_multiple')
        workers = min(WORKERS, len(self.swift_files))
        with futures.ThreadPoolExecutor(workers) as executor:
            executor.map(self.tolkienify_single, self.swift_files)

    """  Tokenizer for the SWIFT message blocks 
          {1:} Basic Header Block
          {2:} Application Header Block
          {3:} User Header Block
          {4:} Text Block
          {5:} Trailer Block
    """
    def tolken_basic_block(self, block):
        print("tolken_basic_block")
        p1 = re.compile('{\d:')
        for sbj in re.split(p1, block):
            sbj = sbj.strip()
            print(sbj[0:len(sbj) - 1])

    def brace_single(self, brace):
        p2 = re.compile('(?s){(.*?)}')
        result = []
        for sbj in re.split(p2, brace):
            sbj = sbj.strip()
            result.append(sbj)
        return result

    @coroutine
    def averager(self):
        total = 0.0
        count = 0
        average = None
        while True:
            term = yield average
            total += term
            count += 1
            average = total / count
            print(average)


if __name__ == '__main__':
    # averager parenthesis else it is a function and will not work
    tstart = time.time()
    tolkien = Tolkienizer()
    coro_avg = tolkien.averager()
    coro_avg.send(40)
    coro_avg.send(100)
    tolkien.tolkienify_multiple()
    tolkien.brace_multiple()
    tend = time.time()
    print('Total time taken {}'.format(tend - tstart))
