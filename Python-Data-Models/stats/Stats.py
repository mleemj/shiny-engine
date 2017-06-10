"""Statistics implementation"""
from abc import ABCMeta, abstractproperty, abstractmethod
from typing import Type

from sortedcontainers import SortedDict


class Stats(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def A1c_level(self):
        pass

    @abstractproperty
    def hdl_level(self):
        pass

    @abstractproperty
    def ldl_level(self):
        pass

    @abstractmethod
    def groupBy(self, group_strategy):
        pass


class ParticipantStats(Stats):
    def __init__(self, pid=None, a1c_mmol=None, hdl=None, ldl=None):
        self._pid = pid
        self._a1c_mmol = a1c_mmol
        self._HDL = hdl
        self._LDL = ldl
        self._nextPt = None
        self._head_marker = None
        self._pcount = -1

    @property
    def A1c_level(self):
        return self._a1c_mmol

    @property
    def pid(self):
        return self._pid

    @property
    def nextPt(self):
        return self._nextPt

    @nextPt.setter
    def nextPt(self, nextPt):
        self._nextPt = nextPt

    @property
    def head_marker(self):
        return self._head_marker

    @head_marker.setter
    def head_marker(self, headMarker):
        self._head_marker = headMarker

    @property
    def pcount(self):
        return self._pcount

    @pcount.setter
    def pcount(self, pcount):
        self._pcount = pcount

    @property
    def hdl_level(self):
        return self._HDL

    @property
    def ldl_level(self):
        return self._LDL


class T2DmGroup(ParticipantStats):
    def __init__(self, pid=None, a1c_mmol=None, hdl=None, ldl=None):
        super().__init__(pid, a1c_mmol, hdl, ldl)

    def get_participant(self):
        probe = self._head_marker
        for pindex in range(probe.pcount):
            probe = probe.nextPt
            yield probe

    def add_participant(self, pid, glucose, hdl, ldl):
        if self._head_marker == None:
            self._head_marker = ParticipantStats(None, None, None, None)
            self._head_marker.nextPt = self._head_marker
            self._head_marker.pcount += 1

        probe = self._head_marker
        for pindex in range(probe.pcount):
            probe = probe.nextPt

        new_participant = ParticipantStats(pid, glucose, hdl, ldl)
        probe.nextPt = new_participant
        new_participant.head_marker = self._head_marker

        self._head_marker.pcount += 1

        return new_participant

    def groupBy(self, group_strategy):
        assert isinstance(group_strategy, GroupStrategy)
        return group_strategy.group(group=self)


class GroupStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def group(self, group, head_marker):
        pass

    def check_grouping(self, strategy_group: Type[T2DmGroup]):
        try:
            assert isinstance(strategy_group, T2DmGroup)
        except AssertionError:
            raise TypeError("group is not instance of T2mGroup")
        else:
            if strategy_group.head_marker.pcount <= 0:
                raise ValueError(
                    'Stats need at least one element for grouping')


class DecimalGroupStrategy(GroupStrategy):
    def __init__(self):
        self._decimal_group = dict()

    def group(self, group):
        super(DecimalGroupStrategy, self).check_grouping(strategy_group=group)
        icount = group.head_marker.pcount

        marker = group.head_marker
        while icount > 0 and marker.nextPt != None:
            marker = marker.nextPt
            glucose_level_key = str(marker.A1c_level)
            if glucose_level_key in self._decimal_group:
                plist = self._decimal_group[glucose_level_key]
                assert isinstance(plist, list)
                plist.append(marker.pid)
            else:
                newPidList = list()
                newPidList.append(marker.pid)
                self._decimal_group[glucose_level_key] = newPidList

            icount -= 1

        return self._decimal_group


class IntegerGroupStrategy(GroupStrategy):
    def __init__(self):
        self._glucose_key_dict = dict()

    def group(self, group):
        super(IntegerGroupStrategy, self).check_grouping(strategy_group=group)
        icount = group.head_marker.pcount

        marker = group.head_marker
        while icount > 0 and marker.nextPt.pid != None:
            marker = marker.nextPt
            gkey = int(float(marker.A1c_level))
            if gkey in self._glucose_key_dict:
                plist = self._glucose_key_dict[gkey]
                assert isinstance(plist, list)
                plist.append(marker.pid)
            else:
                newPidList = list()
                newPidList.append(marker.pid)
                # use integer values of glucose level as keys
                self._glucose_key_dict[gkey] = newPidList
            icount -= 1

        return self._glucose_key_dict


class Glucose_HDL_GroupStrategy(GroupStrategy):
    def __init__(self):
        self._glucose_hdl_dict = SortedDict()

    def group(self, group):
        super(Glucose_HDL_GroupStrategy, self).check_grouping(
            strategy_group=group)
        assert isinstance(group, T2DmGroup)
        for patient in group.get_participant():
            assert isinstance(patient, ParticipantStats)
            a1c_mmol = float(patient.A1c_level)
            hdl_values = self._glucose_hdl_dict.get(a1c_mmol)
            if hdl_values == None:
                hdl_values = set()
                hdl_values.add(patient.hdl_level)
                self._glucose_hdl_dict[a1c_mmol] = hdl_values
            else:
                hdl_values.add(patient.hdl_level)
        return self._glucose_hdl_dict


class PCounter(object):
    # static variable
    pidcount = 0

    # Helper class to get unique id
    # p = PCounter()
    # p() returns 0
    # p() returns 1
    def __call__(self, *args, **kwargs):
        PCounter.pidcount += 1
        return PCounter.pidcount


"""
Examples using the following algorithms: Composite pattern, Strategy
pattern, Singly linked list
"""
