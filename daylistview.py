'''
Created on May 24, 2015

@author: jeremy
'''

import wx, daylist

class DayListView(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.days_list = []
        
        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.SetSizer(self.main_sizer)
        
    def addLists(self):
        self.days_list = []
        for i in range(7):
            obj = daylist.DayList(self)
            if i < 6:
                self.main_sizer.Add(obj, 1, wx.EXPAND|wx.RIGHT, 5)
            else:
                self.main_sizer.Add(obj, 1, wx.EXPAND)
            self.days_list.append(obj)
            
    def setList(self, index, date):
        day = self.days_list[index]
        day.Clear()
        day.setTitle(date, True)
    
if __name__ == '__main__':
    pass