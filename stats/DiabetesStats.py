"""Statistics implementation"""
from abc import ABCMeta, abstractproperty, abstractmethod

from sortedcontainers import SortedList, SortedDict


class Stats(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def glucose_level(self):
        pass

    @abstractmethod
    def pGrouping(self, group_strategy):
        pass


class DiabetesStats(Stats):
    @property
    def glucose_level(self):
        return self._glucose

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, pid):
        self._pid = pid

    @property
    def nextPt(self):
        return self._nextPt

    @nextPt.setter
    def nextPt(self, nextPt):
        self._nextPt = nextPt

    @property
    def headStat(self):
        return self._head_marker

    @headStat.setter
    def headStat(self, headStat):
        self._head_marker = headStat

    @property
    def pcount(self):
        return self._pcount

    @pcount.setter
    def pcount(self, pcount):
        self._pcount = pcount


class Glucose(DiabetesStats):
    def __init__(self, pid=None, glucose=None):
        self._pid = pid
        self._glucose = glucose
        self._nextPt = None
        self._head_marker = None
        self._pcount = -1

    def add_participant(self, pid, glucose):
        if self._head_marker == None:
            self._head_marker = Glucose(None, None)
            self._head_marker.nextPt = self._head_marker
            self._head_marker.pcount += 1

        probe = self._head_marker
        for pindex in range(probe.pcount):
            probe = probe.nextPt

        new_participant = Glucose(pid, glucose)
        probe.nextPt = new_participant
        new_participant.headStat = self._head_marker

        self._head_marker.pcount += 1

        return new_participant

    def pGrouping(self, group_strategy):
        assert isinstance(group_strategy, GroupStrategy)
        return group_strategy.group(self.headStat)


class GroupStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def group(self, headstat):
        pass

    def check_grouping(self, headstat):
        assert isinstance(headstat, DiabetesStats)
        icount = headstat.pcount
        if icount <= 0:
            raise ValueError('Stats need at least one element for grouping')
        return icount


class DecimalGroupStrategy(GroupStrategy):
    def __init__(self):
        self._bgroup_dict = SortedDict()

    def group(self, headstat):
        icount = super(DecimalGroupStrategy, self).check_grouping(headstat)

        marker = headstat
        while icount > 0 and marker.nextPt != None:
            marker = marker.nextPt
            strkey = str(marker.glucose_level)
            if strkey in self._bgroup_dict:
                plist = self._bgroup_dict[strkey]
                plist.add(marker.pid)
            else:
                newPidList = SortedList()
                newPidList.add(marker.pid)
                self._bgroup_dict[strkey] = newPidList

            icount -= 1

        return self._bgroup_dict


class IntegerGroupStrategy(GroupStrategy):
    def __init__(self):
        self._glucose_key_dict = SortedDict()

    def group(self, headstat):
        icount = super(IntegerGroupStrategy, self).check_grouping(headstat)

        marker = headstat
        while icount > 0 and marker.nextPt.pid != None:
            marker = marker.nextPt
            gkey = int(float(marker.glucose_level))
            if gkey in self._glucose_key_dict:
                plist = self._glucose_key_dict[gkey]
                plist.add(marker.pid)
            else:
                newPidList = SortedList()
                newPidList.add(marker.pid)
                # use integer values of glucose level as keys
                self._glucose_key_dict[gkey] = newPidList

            icount -= 1

        return self._glucose_key_dict


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
Examples using the following algorithms: Composite pattern, Strategy pattern, Singly linked list
"""
