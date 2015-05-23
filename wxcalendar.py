'''
Created on May 23, 2015

@author: jeremy
'''

import wx, calendar
from pywinauto.application import cur_item

calendar.setfirstweekday(6) #First day of week = Sunday

BACKGROUND_COLOR = (255,255,255) #White
DIM_COLOUR = (200,200,200) #Gray
NORMAL_FONT = (14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL) #14pt
SELECTED_FONT = (14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) #14pt Bold

class Day(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.day = None
        self.month = None
        self.year = None
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.day_label = wx.StaticText(self, label="NULL")
        self.day_font = wx.Font(*NORMAL_FONT)
        
        self.day_label.SetFont(self.day_font)
        
        sizer.Add((0,0), 1, wx.EXPAND)
        sizer.Add(self.day_label, 0, wx.CENTER)
        sizer.Add((0,0), 1, wx.EXPAND)
        
        self.SetBackgroundColour(wx.Colour(*BACKGROUND_COLOR))
        
        self.SetSizer(sizer)
    
    def setDay(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.day_label.SetLabel(str(day))
    
    def dimDay(self):
        self.SetBackgroundColour(wx.Colour(*DIM_COLOUR))
        
    def setColour(self, r, g, b):
        colour = wx.Colour((r, g ,b))
        self.SetBackgroundColour(colour)

class Calendar(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.days_sizer = wx.GridSizer(rows=1, cols=7)
        for day in ["Sun", "Mon", "Teu", "Wed", "Thu", "Fri", "Sat"]:
            day_sizer = wx.BoxSizer(wx.HORIZONTAL)
            day_label = wx.StaticText(self, label=day)
            day_sizer.Add((0,0), 1)
            day_sizer.Add(day_label, 0)
            day_sizer.Add((0,0), 1)
            self.days_sizer.Add(day_sizer, 1, wx.EXPAND)
            
        self.calendar_sizer = wx.GridSizer(rows=6, cols=7)
        
        self.main_sizer.Add(self.days_sizer, 0, wx.EXPAND)
        self.main_sizer.Add(self.calendar_sizer, 1, wx.EXPAND)
        
        self.fillCalendar()
        
        self.SetSizer(self.main_sizer)
        
    def fillCalendar(self):
        self.calendar_list = []
        for row in range(6):
            self.calendar_list.append([])
            for col in range(7):
                day_cell = Day(self, style=wx.SIMPLE_BORDER)
                self.calendar_list[row].append(day_cell)
                self.calendar_sizer.Add(day_cell, 1, wx.EXPAND)
    
    def setMonth(self, year, month):
        month_list = getMonth(year, month)
        prev_set, next_set = getSurroundingMonths(year, month)
        prev_year = prev_set[0]
        prev_month = prev_set[1]
        next_year = next_set[0]
        next_month = next_set[1]
        
        prev_month_length = calendar.monthrange(prev_year, prev_month)[1]
        
        week_index = 0
        for week in self.calendar_list:
            day_index = 0
            prev_month_date = prev_month_length - month_list[week_index].count(0)
            next_month_date = 0
            print month_list[week_index].count(0)
            for day in week:
                date = month_list[week_index][day_index]
                if week_index == 0 and date == 0:
                    prev_month_date += 1
                    day.setDay(prev_year, prev_month, prev_month_date)
                    day.dimDay()
                elif week_index >= 5 and date == 0:
                    next_month_date += 1
                    day.setDay(next_year, next_month, next_month_date)
                    day.dimDay()
                else:
                    day.setDay(year, month, date)
                day_index += 1
            week_index += 1

def getSurroundingMonths(year, month):
    if month == 1:
        prev_month = 12
        prev_year = year - 1
        next_month = month + 1
        next_year = year
    elif month == 12:
        prev_month = month - 1
        prev_year = year
        next_month = 1
        next_year = year + 1
    else:
        prev_month = month - 1
        prev_year = year
        next_month = month + 1
        next_year = year
    
    return ([prev_year, prev_month], [next_year, next_month])

def getMonth(year, month):
    month_list = calendar.monthcalendar(year, month)
    month_list.append([0,0,0,0,0,0,0])
            
    return month_list

if __name__ == '__main__':
    app = wx.App()
     
    frame = wx.Frame(None)
     
    sizer = wx.BoxSizer(wx.VERTICAL)
     
    cal = Calendar(frame)
     
    sizer.Add(cal, 1, wx.EXPAND|wx.ALL, 10)
    frame.SetSizer(sizer)
     
    cal.setMonth(2015, 5)
     
    frame.Show()
    app.MainLoop()