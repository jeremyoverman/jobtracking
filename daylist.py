'''
Created on May 24, 2015

@author: jeremy
'''

import wx, calendar

TITLE_FONT = (14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL) #14pt
JOB_FONT = (10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL) #10pt
SECTION_FONT = (8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) #8pt Bold
NORMAL_BACKGROUND = (255, 255, 255) #White
NOT_STARTED_BACKGROUND = (255, 255, 255) #White
NOT_FINISHED_BACKGROUND = (255, 255, 148) #Yellow
FINISHED_BACKGROUND = (102, 255, 51) #Green
ACTIVE_BACKGROUND = (204,255,255) #Light Blue

JOB_NOT_STARTED = 0
JOB_NOT_FINISHED = 1
JOB_FINISHED = 2

class Job(wx.Panel):
    def __init__(self, parent, jobid, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.setColour(*NOT_STARTED_BACKGROUND)
        
        self.jobid = jobid
        self.summary = None
        self.status = JOB_NOT_STARTED
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.summary_label = wx.StaticText(self, label="Summary")
        self.summary_label.SetFont(wx.Font(*JOB_FONT))
        self.main_sizer.Add(self.summary_label)
        
        self.SetSizer(self.main_sizer)
        
    def setSummary(self, summary): 
        self.summary_label.SetLabel(summary)
        self.summary = summary
    
    def setNormal(self):
        if self.status == JOB_FINISHED: self.setFinished()
        elif self.status == JOB_NOT_FINISHED: self.setNotFinished()
        elif self.status == JOB_NOT_STARTED: self.setNotStarted()
    
    def setActive(self):
        self.setColour(*ACTIVE_BACKGROUND)
        
    def setFinished(self):
        self.status = JOB_FINISHED
        self.setColour(*FINISHED_BACKGROUND)
        
    def setNotFinished(self):
        self.status = JOB_NOT_FINISHED
        self.setColour(*NOT_FINISHED_BACKGROUND)
    
    def setNotStarted(self):
        self.status = JOB_NOT_STARTED
        self.setColour(*NOT_STARTED_BACKGROUND)
        
    def setColour(self, r, g, b):
        self.SetBackgroundColour(wx.Colour(r, g, b))
        self.Refresh()

class DayList(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.jobs = {}
        
        self.finished_showing = True
        self.not_finished_showing = True
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.title_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.title_label = wx.StaticText(self, label="Today's Jobs")
        self.title_label.SetFont(wx.Font(*TITLE_FONT))
        
        self.finished_label = wx.StaticText(self, label="Finished (0)")
        self.finished_label.SetFont(wx.Font(*SECTION_FONT))
        self.finished_sizer = wx.BoxSizer(wx.VERTICAL)
        self.finished_label.SetBackgroundColour(wx.Colour(*NORMAL_BACKGROUND))
        
        self.not_finished_label = wx.StaticText(self, label="Not Finished (0)")
        self.not_finished_label.SetFont(wx.Font(*SECTION_FONT))
        self.not_finished_sizer = wx.BoxSizer(wx.VERTICAL)
        self.not_finished_label.SetBackgroundColour(wx.Colour(*NORMAL_BACKGROUND))
        
        self.not_started_label = wx.StaticText(self, label="Not Started (0)")
        self.not_started_label.SetFont(wx.Font(*SECTION_FONT))
        self.not_started_sizer = wx.BoxSizer(wx.VERTICAL)
        self.not_started_label.SetBackgroundColour(wx.Colour(*NORMAL_BACKGROUND))
        
        self.end_filler = wx.StaticText(self)
        self.end_filler.SetBackgroundColour(wx.Colour(*NORMAL_BACKGROUND))
        
        #self.title_sizer.Add((0,0), 1, wx.EXPAND)
        self.title_sizer.Add(self.title_label, 0)
        self.title_sizer.Add((0,0), 1, wx.EXPAND)
        
        self.main_sizer.Add(self.title_sizer, 0, wx.EXPAND)
        
        self.main_sizer.Add(self.finished_label, 0, wx.EXPAND)
        self.main_sizer.Add(self.finished_sizer, 0, wx.EXPAND)
        
        self.main_sizer.Add(self.not_finished_label, 0, wx.EXPAND)
        self.main_sizer.Add(self.not_finished_sizer, 0, wx.EXPAND)
        
        self.main_sizer.Add(self.not_started_label, 0, wx.EXPAND)
        self.main_sizer.Add(self.not_started_sizer, 0, wx.EXPAND)
        
        self.main_sizer.Add(self.end_filler, 1, wx.EXPAND)
        
        self.__init__bindings()
        self.SetSizer(self.main_sizer)
        
        self.Layout()
        self.Refresh()
        
    def __init__bindings(self):
        self.finished_label.Bind(wx.EVT_LEFT_DOWN, lambda x: self.toggleSection("finished"))
        self.not_finished_label.Bind(wx.EVT_LEFT_DOWN, lambda x: self.toggleSection("not finished"))
        self.not_started_label.Bind(wx.EVT_LEFT_DOWN, lambda x: self.toggleSection("not started"))
    
    def normalizeSelection(self):
        for job in self.jobs:
            self.jobs[job].setNormal()
    
    def setTitle(self, date, short=False):
        name = calendar.day_name[date.weekday()]
        if short: name = name[:3]
        self.title_label.SetLabel("%s, %d" % (name, date.day))
    
    def Clear(self):
        self.jobs = {}
        for section in [self.finished_sizer, self.not_finished_sizer, self.not_started_sizer]:
            section.Clear(True)
        self.setGroupLabels()
        self.Layout()
    
    def toggleSection(self, section):
        if section == "finished": sizer = self.finished_sizer
        if section == "not finished": sizer = self.not_finished_sizer
        if section == "not started": sizer = self.not_started_sizer
        if sizer.GetItemCount() > 0:
            if sizer.GetItem(0).IsShown():
                sizer.ShowItems(False)
            else:
                sizer.ShowItems(True)
        self.Layout()
        
    def setJobStatus(self, jobid, status):
        job = self.jobs[jobid]
        job.GetContainingSizer().Detach(job)
        if status == JOB_FINISHED:
            self.finished_sizer.Add(job, 0, wx.EXPAND)
            job.setFinished()
        elif status == JOB_NOT_FINISHED:
            self.not_finished_sizer.Add(job, 0, wx.EXPAND)
            job.setNotFinished()
        elif status == JOB_NOT_STARTED:
            self.not_started_sizer.Add(job, 0, wx.EXPAND)
            job.setNotStarted()
        
        self.Layout()
        self.Refresh()
        
        self.setGroupLabels()
    
    def addJob(self, jobid, summary):
        job = Job(self, jobid)
        job.setSummary(summary)
        self.not_started_sizer.Add(job, 0, wx.EXPAND)
        
        self.jobs[jobid] = job
        self.setGroupLabels()
        
        self.Layout()
        
        return job
        
    def setGroupLabels(self):
        finished_items = self.finished_sizer.GetItemCount()
        not_finished_items = self.not_finished_sizer.GetItemCount()
        not_started_items = self.not_started_sizer.GetItemCount()
        
        self.finished_label.SetLabel("Finished (%d)" % finished_items)
        self.not_finished_label.SetLabel("Not Finished (%d)" % not_finished_items)
        self.not_started_label.SetLabel("Not Started (%d)" % not_started_items)
        
        self.Layout()
        self.Refresh()
    
if __name__ == '__main__':
    app = wx.App()
    
    frame = wx.Frame(None)
    daylist = DayList(frame)
    daylist.addJob("1", "Billy Bob")
    daylist.addJob("2", "Uncle Randy")
    daylist.addJob("3", "Princess Lea, Alderan")
    daylist.addJob("4", "Little home on the range")
    
    daylist.jobs["1"].setActive()
    
    frame.Show()
    app.MainLoop()