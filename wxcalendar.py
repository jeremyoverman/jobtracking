'''
Created on May 23, 2015

@author: jeremy
'''

import wx, calendar
import datetime

calendar.setfirstweekday(6) #First day of week = Sunday

BACKGROUND_COLOUR = (255,255,255) #White
ACTIVE_COLOUR = (204,255,255) #Light Blue
DIM_COLOUR = (200,200,200) #Gray
NORMAL_FONT = (14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL) #14pt
SELECTED_FONT = (14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) #14pt Bold

class Day(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.date = None
        self.bg_colour = BACKGROUND_COLOUR
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.day_label = wx.StaticText(self, label="NULL")
        self.day_font = wx.Font(*NORMAL_FONT)
        
        self.day_label.SetFont(self.day_font)
        self.day_label.font = wx.Font(*NORMAL_FONT)
        
        sizer.Add((0,0), 1, wx.EXPAND)
        sizer.Add(self.day_label, 0, wx.CENTER)
        sizer.Add((0,0), 1, wx.EXPAND)
        
        self.SetBackgroundColour(wx.Colour(*BACKGROUND_COLOUR))
        
        self.SetSizer(sizer)
        
    def setActive(self):
        self.SetBackgroundColour(wx.Colour(*ACTIVE_COLOUR))
        self.Refresh()
        self.day_label.SetFont(wx.Font(*SELECTED_FONT))
        
    def setInactive(self):
        self.SetBackgroundColour(wx.Colour(*self.bg_colour))
        self.Refresh()
        self.day_label.SetFont(wx.Font(*NORMAL_FONT))
        
    def setDay(self, date):
        self.date = date
        self.day_label.SetLabel(str(date.day))
    
    def dimDay(self, dimday=True):
        if dimday: self.setColour(*DIM_COLOUR)
        else: self.setColour(*BACKGROUND_COLOUR)
        
    def setColour(self, r, g, b):
        self.bg_colour = (r, g, b)
        self.SetBackgroundColour(wx.Colour(r, g ,b))

class Calendar(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.days_sizer = wx.GridSizer(rows=1, cols=7)
        for day in ["Sun", "Mon", "Teu", "Wed", "Thu", "Fri", "Sat"]:
            day_sizer = wx.BoxSizer(wx.HORIZONTAL)
            day_label = wx.StaticText(self, label=day)
            day_font = wx.Font(*NORMAL_FONT)
            day_label.SetFont(day_font)
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
        self.date_dict = {}
        
        x = 0
        for week in month_list:
            y = 0
            for date in week:
                obj = self.calendar_list[x][y] 
                obj.setDay(date)
                if date.month != month:
                    obj.dimDay()
                else:
                    obj.dimDay(False)
                self.date_dict[date] = obj
                y += 1
            x += 1
        
        self.Layout()
        self.Refresh()

def getMonth(year, month):
    month_list = calendar.Calendar(6).monthdatescalendar(year, month)
    last_date = month_list[-1][-1]
    for i in range(6 - len(month_list)):
        week = []
        for day in range(7):
            last_date += datetime.timedelta(days=1)
            week.append(last_date)
        month_list.append(week)
    
    return month_list

if __name__ == '__main__':
#     getMonth(2015, 2)
    app = wx.App()
       
    frame = wx.Frame(None)
       
    sizer = wx.BoxSizer(wx.VERTICAL)
       
    cal = Calendar(frame)
       
    sizer.Add(cal, 1, wx.EXPAND|wx.ALL, 10)
    frame.SetSizer(sizer)
       
    #cal.setMonth(2014, 2)
    cal.setMonth(2015, 5)
    
    frame.Show()
    app.MainLoop()