from DiabetesStats import PCounter, Glucose, IntegerGroupStrategy, DecimalGroupStrategy
from sortedcontainers import SortedList, SortedDict

import random
import unittest
import json


class PTestCase(unittest.TestCase):
    def setUp(self):
        print 'new setup'
        self.pListControl = SortedList()

        self.pDecimalControlDict = SortedDict()

        self.pDecmialControlDict = SortedDict()

        self.pGlucoseTest = Glucose()

        self.pIntegerGroupTest = IntegerGroupStrategy()

        self.pDecimalGroupTest = DecimalGroupStrategy()

        # Calls to PCounter increments counter
        self.id = PCounter()

        # ADA recommendation for fasting plasma glucose is 3.9 to 7.2 mmol/L
        # random float between 1 and 10, eg, 1.1800146073117523
        # PyFormat 1 decimal place
        # Example at PyFormat.info
        # '{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3)
        # Gib = 2.718
        for i in range(10):
            mmol = '{:.1f}'.format(random.uniform(1, 2))
            new_pid = self.id()
            print 'pid = {0} : mmol = {1}'.format(new_pid, mmol)
            participant = self.pGlucoseTest.add_participant(pid=new_pid, glucose=mmol)
            # Creates a control participants list and dictionary for testing
            self.pListControl.add(participant)

            mmolStr = str(mmol)

            if self.pDecmialControlDict.get(mmolStr) == None:
                dec_list = SortedList()
                dec_list.add(participant.pid)
                self.pDecmialControlDict[mmolStr] = dec_list
            else:
                dec_pid_list = self.pDecmialControlDict[mmolStr]
                self.assertIsInstance(dec_pid_list, SortedList)
                dec_pid_list.add(participant.pid)

            mmolKey = int(float(mmol))

            if self.pDecimalControlDict.get(mmolKey) == None:
                int_glucose_List = SortedList()
                int_glucose_List.add(participant.pid)
                self.pDecimalControlDict[mmolKey] = int_glucose_List
            else:
                pid_list = self.pDecimalControlDict[mmolKey]
                self.assertIsInstance(pid_list, SortedList)
                pid_list.add(participant.pid)

        print '\n'

    def test_PCounter(self):
        controlCount = len(self.pListControl)
        testCount = self.pGlucoseTest.headStat.pcount
        print 'test_PCounter: Control result = {} : Test result = {}'.format(controlCount, testCount)
        self.assertEqual(controlCount, testCount)
        self.tearDown()
        print '\n'

    def test_int_group_strategy(self):
        test_int_dict = self.pGlucoseTest.pGrouping(self.pIntegerGroupTest)
        print 'test integer grouping strategy'

        control_key_iter = iter(self.pDecimalControlDict)

        for pkey in control_key_iter:
            control_list = self.pDecimalControlDict[pkey]
            test_int_list = test_int_dict[pkey]
            print('mmol key: {0}'.format(pkey))
            control_list_items = []
            for control_item in control_list:
                control_list_items.append(control_item)
            test_int_items = []
            for test_int in test_int_list:
                test_int_items.append(test_int)

            self.assertListEqual(control_list_items, test_int_items)
            print 'Control list = {}'.format(control_list_items)
            print 'Test list = {}'.format(test_int_items)

    def test_decimal_group_strategy(self):
        test_decimal_dict = self.pGlucoseTest.pGrouping(self.pDecimalGroupTest)
        print 'test decmial grouping strategy'

        control_key_iter = iter(self.pDecmialControlDict)

        for pkey in control_key_iter:
            control_list = self.pDecmialControlDict[pkey]
            test_dec_list = test_decimal_dict[pkey]
            print('mmol key: {0}'.format(pkey))
            control_list_items = []
            for control_item in control_list:
                control_list_items.append(control_item)
            test_dec_items = []
            for test_dec in test_dec_list:
                test_dec_items.append(test_dec)

            self.assertListEqual(control_list_items, test_dec_items)
            print 'Control list = {}'.format(control_list_items)
            print 'Test decimal list = {}'.format(test_dec_items)

    def test_ValueError(self):
        test_glucose = Glucose(None, None)
        with self.assertRaises(ValueError):
            self.pIntegerGroupTest.group(test_glucose)

    if __name__ == '__main__':
        unittest.main()
