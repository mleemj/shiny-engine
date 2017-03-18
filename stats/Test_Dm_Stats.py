import random
import unittest

from numpy import random as npr

from stats.Stats import PCounter, T2DmGroup, IntegerGroupStrategy, \
    DecimalGroupStrategy, ParticipantStats, Glucose_HDL_GroupStrategy


class TestDmStats(unittest.TestCase):
    def setUp(self):
        print('new setup')
        self.pListControl = list()

        self.pInteger_Group_Test_Glucose_level = dict()

        self.pDecimal_Group_Test_Glucose_level = dict()

        self.testT2DmGroup = T2DmGroup()

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
            # The standard lipid profile, as recommended by the
            # Adult Treatment Panel III (ATP III), consists of direct
            # measurement of total cholesterol, HDL-C, and triglycerides,
            # with a calculated LDL-C, obtained after a 9-hour to 12-hour
            # fast.
            # LDL cholesterol levels per ATP III guidelines are as follows:
            #  [1]
            # Less than < 100 mg/ dL - Optimal
            # 100-129 mg/dL - Near optimal/above optimal
            # 130-159 mg/dL - Borderline high
            # 160-189 mg/dL - High
            # >190 mg/dL - Very high
            Ldl = npr.randint(low=100, high=190)

            # The reference range of high-density lipoprotein cholesterol
            # (HDL-C) is 40-50 mg/dL in men and 50-60 mg/dL in women.
            Hdl = npr.randint(low=40, high=60)

            # The reference range for healthy adults is 4.8–5.9%.
            mmol = '{:.1f}'.format(random.uniform(4, 7))
            new_pid = self.id()
            print('pid = {0} : mmol = {1}'.format(new_pid, mmol))
            participant = self.testT2DmGroup.add_participant(pid=new_pid,
                                                             glucose=mmol,
                                                             hdl=Hdl, ldl=Ldl)
            # Creates a control participants list and dictionary for testing
            self.pListControl.append(participant)

            mmolStr = str(mmol)

            if self.pDecimal_Group_Test_Glucose_level.get(mmolStr) == None:
                dec_list = list()
                dec_list.append(participant.pid)
                self.pDecimal_Group_Test_Glucose_level[mmolStr] = dec_list
            else:
                dec_pid_list = self.pDecimal_Group_Test_Glucose_level[mmolStr]
                self.assertIsInstance(dec_pid_list, list)
                dec_pid_list.append(participant.pid)

            mmolKey = int(float(mmol))

            if self.pInteger_Group_Test_Glucose_level.get(mmolKey) == None:
                int_glucose_List = list()
                int_glucose_List.append(participant.pid)
                self.pInteger_Group_Test_Glucose_level[
                    mmolKey] = int_glucose_List
            else:
                int_pid_list = self.pInteger_Group_Test_Glucose_level[mmolKey]
                self.assertIsInstance(int_pid_list, list)
                int_pid_list.append(participant.pid)

        print('\n')

    def test_PCounter(self):
        controlCount = len(self.pListControl)
        testCount = self.testT2DmGroup.head_marker.pcount
        print('test_PCounter: Control result = {} : Test result = {}'.format(
            controlCount, testCount))
        self.assertEqual(controlCount, testCount)
        self.tearDown()
        print('\n')

    def test_int_group_strategy(self):
        test_int_dict = self.testT2DmGroup.groupBy(self.pIntegerGroupTest)
        print('test integer grouping strategy')

        control_key_iter = iter(self.pInteger_Group_Test_Glucose_level)

        for pkey in control_key_iter:
            control_list = self.pInteger_Group_Test_Glucose_level[pkey]
            test_int_list = test_int_dict[pkey]
            print('mmol key: {0}'.format(pkey))
            control_list_items = []
            for control_item in control_list:
                control_list_items.append(control_item)
            test_int_items = []
            for test_int in test_int_list:
                test_int_items.append(test_int)

            self.assertListEqual(control_list_items, test_int_items)
            print('Control list = {}'.format(control_list_items))
            print('Test list = {}'.format(test_int_items))

    def test_decimal_group_strategy(self):
        for pt in self.testT2DmGroup.get_participant():
            self.assertIsInstance(pt, ParticipantStats)
            print("test_generator")
            print("pid={pid}:glucose={glucose};hdl={hdl}:ldl={ldl}"
                  .format(pid=pt.pid, glucose=pt.A1c_level,
                          hdl=pt.hdl_level,
                          ldl=pt.ldl_level))
            print()

        test_decimal_dict = self.testT2DmGroup.groupBy(self.pDecimalGroupTest)
        print('test decmial grouping strategy')

        control_key_iter = iter(self.pDecimal_Group_Test_Glucose_level)

        for pkey in control_key_iter:
            control_list = self.pDecimal_Group_Test_Glucose_level[pkey]
            test_dec_list = test_decimal_dict[pkey]
            print('mmol key: {0}'.format(pkey))
            control_list_items = []
            for control_item in control_list:
                control_list_items.append(control_item)
            test_dec_items = []
            for test_dec in test_dec_list:
                test_dec_items.append(test_dec)

            self.assertListEqual(control_list_items, test_dec_items)
            print('Control list = {}'.format(control_list_items))
            print('Test decimal list = {}'.format(test_dec_items))

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            self.pIntegerGroupTest.group(group=None)

    def test_ValueError(self):
        test_group = T2DmGroup(None, None, None, None)
        test_group.head_marker = ParticipantStats()
        with self.assertRaises(ValueError):
            self.pIntegerGroupTest.group(group=test_group)

    def test_A1c_HDL(self):
        print('test_A1c_HDL')
        self.assertTrue(True)
        sample_data = dict()
        for i in range(10):
            mmol = '{:.1f}'.format(random.uniform(4, 7))
            sample_data[mmol] = i

        for k in sample_data.keys():
            print('{key}:{value}'.format(key=k, value=sample_data[k]))

    def test_glucose_hdl(self):
        patient_group = T2DmGroup()

        patient_id = PCounter()

        for i in range(100):
            Hdl = npr.randint(low=40, high=60)
            Ldl = npr.randint(low=100, high=190)
            A1c = '{:.1f}'.format(random.uniform(4, 7))
            patient_group.add_participant(pid=patient_id(), glucose=A1c,
                                          hdl=Hdl, ldl=Ldl)

        a1c_hdl_dict = patient_group.groupBy(Glucose_HDL_GroupStrategy())
        self.assertIsInstance(a1c_hdl_dict, dict)
        print('test_glucose_hdl')
        for a1c_key in a1c_hdl_dict.keys():
            print('key:value = {key}:{value}'.format(key=a1c_key,
                                                     value=a1c_hdl_dict[
                                                         a1c_key]))
            print()

if __name__ == '__main__':
    unittest.main()
