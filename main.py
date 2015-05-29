'''
Created on May 23, 2015

@author: jeremy
'''

import wx, datetime, calendar
import googleapi, wxcalendar, daylist
import gui

calendar.setfirstweekday(calendar.SUNDAY)
FIXED_WEEKDAYS = [1,2,3,4,5,6,0]

class JobList:
    def __init__(self, joblist):
        self.joblist = joblist
        self.curr_selected = None
        self.date = None
    
    def handleList(self, evt):
        selection = self.joblist.GetSelection()
        jobdetails.loadJob(self.jobs[selection])
    
    def getDaysEvents(self, date):
        self.date = date
        self.jobs = {}
        main.fetchEvents(date)
        self.events = gcal.getDayList(date)
        window.day_list.Clear()
        
        self.joblist.setTitle(date)
        
        i = 0
            
        for event in self.events:
            summary = event["summary"]
            jobid = event["id"]
            
            job = self.joblist.addJob(jobid, summary)
            job.Bind(wx.EVT_LEFT_DOWN, self.handleClick)
            job.summary_label.Bind(wx.EVT_LEFT_DOWN, self.handleClick)
            status = jobdetails.getJobStatus(jobid)
            
            self.joblist.setJobStatus(jobid, status)
            
            i += 1
    
    def handleClick(self, evt):
        obj = evt.GetEventObject()
        if type(obj) != daylist.Job:
            obj = obj.GetParent()
        
        if self.curr_selected:
            self.curr_selected.setNormal()
            
        for job in dayview.day_view.days_list:
            job.normalizeSelection()
            
        self.joblist.normalizeSelection()
        obj.setActive()
        self.curr_selected = obj
        
        jobdetails.loadJob(obj.jobid)
            
class JobDetails:
    def __init__(self):
        pass
    
    def getJobFromEvent(self, eventid):
        job = None
        for event in main.fetchEvents(main.curr_date):
            if event["id"] == eventid:
                job = event
        
        return job
    
    def loadJob(self, eventid):
        self.clearJob()
        
        job = self.getJobFromEvent(eventid)
                
        summary = job["summary"]
        window.job_title_label.SetLabel(summary)
        
        if job.has_key("description"):
            description = job["description"]
            self.fillServices(description)
        
        if job["start"].has_key("dateTime"):
            gstartdate = job["start"].get("dateTime")
            genddate = job["end"].get("dateTime")
            
            startdt = gcal.gDatetimeToDatetime(gstartdate)
            enddt = gcal.gDatetimeToDatetime(genddate)
            self.setStartEndTimes(startdt, enddt)
    
    def getJobStatus(self, eventid):
        job = self.getJobFromEvent(eventid)
        if job["start"].has_key("dateTime"):
            start = job["start"].get("dateTime")
            end = job["end"].get("dateTime")
            if start != end:
                return daylist.JOB_FINISHED
            else:
                return daylist.JOB_NOT_FINISHED
        else:
            return daylist.JOB_NOT_STARTED
        
    def clearJob(self):
        window.job_title_label.SetLabel("")
        window.job_services_listbox.Clear()
        
        window.job_start_time_hour_combo.SetValue(" ")
        window.job_start_time_min_combo.SetValue(" ")
        window.job_start_time_suffix_combo.SetValue(" ")
        window.job_end_time_hour_combo.SetValue(" ")
        window.job_end_time_min_combo.SetValue(" ")
        window.job_end_time_suffix_combo.SetValue(" ")
    
    def fillServices(self, description):
        for line in description.split("\n"):
            if line[0] == "*":
                window.job_services_listbox.Append(line[1:])
    
    def setStartEndTimes(self, startdt, enddt):
        start_hour = startdt.hour
        start_suffix = "AM"
        if start_hour > 12:
            start_hour = start_hour - 12
            start_suffix = "PM"
        
        window.job_start_time_hour_combo.SetValue(str(start_hour))
        window.job_start_time_min_combo.SetValue("%02d" % startdt.minute)
        window.job_start_time_suffix_combo.SetValue(str(start_suffix))
        
        if startdt != enddt:
            end_hour = enddt.hour
            end_suffix = "AM"
            if end_hour > 12:
                end_hour = end_hour - 12
                end_suffix = "PM"

            window.job_end_time_hour_combo.SetValue(str(end_hour))
            window.job_end_time_min_combo.SetValue("%02d" % enddt.minute)
            window.job_end_time_suffix_combo.SetValue(str(end_suffix))

class Calendar:
    def __init__(self):
        today = datetime.date.today()
        self.curr_date = today
        self.selected_date = None
        self.max_jobs = 25
        
        self.calendar = window.month_calendar
        self.calendar.setMonth(today.year, today.month)
        
        self.setCalendarTitle(today.year, today.month)
        
        self.__init__bindings()
    
    def colorCodeCalendar(self):
        jobs = {}
        for event in main.fetchEvents(main.curr_date):
            if event["start"].has_key("date"):
                gdate = event["start"].get("date")
            else:
                gdate = event["start"].get("dateTime")[0:10]
            dt = gcal.gDatetimeToDatetime(gdate)
            if jobs.has_key(dt):
                jobs[dt] += 1
            else:
                jobs[dt] = 1
                
        for job in jobs:
            if job.month == self.curr_date.month:
                if jobs[job] > self.max_jobs:
                    self.max_jobs = jobs[job]
                shade = 255 - ((float(jobs[job]) / float(self.max_jobs)) * 255)
                day = self.calendar.date_dict[job]
                day.setColour(255, shade, shade)
    
    def setCalendarTitle(self, year, month):
        title = "%s %s" % (calendar.month_name[month], year)
        window.calendar_title.SetLabel(title)
        
        self.curr_date = datetime.datetime(year, month, 1)
    
    def handleClick(self, evt):
        if self.selected_date:
            self.selected_date.setInactive()
        day = evt.GetEventObject()
        if type(day) != wxcalendar.Day:
            day = day.GetParent()
        day.setActive()
        self.selected_date = day
        joblist.getDaysEvents(day.date)
        jobdetails.clearJob()
    
    def __init__bindings(self):
        for date in self.calendar.date_dict:
            child = self.calendar.date_dict[date] 
            child.Bind(wx.EVT_LEFT_DOWN, self.handleClick)
            child.day_label.Bind(wx.EVT_LEFT_DOWN, self.handleClick)

class DayView:
    def __init__(self):
        self.day_view = window.day_list_view
        self.curr_date = datetime.date.today()
        
        self.day_view.addLists()
    
    def setWeekContainingDate(self, date):
        today = FIXED_WEEKDAYS[calendar.weekday(date.year, date.month, date.day)]
        sunday = date - datetime.timedelta(days=today)
        
        for i in range(7):
            curr_date = sunday + datetime.timedelta(days=i)
            self.day_view.setList(i, curr_date)
            day = self.day_view.days_list[i]
            job_list = JobList(day)
            job_list.getDaysEvents(curr_date)
            
            day.setTitle(curr_date, short=True)

class AddJobWindow():
    def __init__(self):
        self.gui = gui.AddJob(window)
        self.contact = None
        
        self.gui.choose_client_button.Bind(wx.EVT_BUTTON, self.getContact)
        self.gui.freq_choice.Bind(wx.EVT_CHOICE, self.updateFreq)
        self.gui.add_button.Bind(wx.EVT_BUTTON, self.addJob)
        
    def getContact(self, evt=None):
        c = ContactsWindow(choose=True)
        c.gui.ShowModal()
        atomid = c.contact
        if atomid:
            self.contact = atomid
            name = contacts.getFullName(atomid)
            self.gui.client_entry.SetValue(name)
        
    def updateFreq(self, evt=None):
        if self.gui.freq_choice.GetStringSelection() == "Weekly":
            self.gui.freq_label.SetLabel("week(s)")
        else:
            self.gui.freq_label.SetLabel("month(s)")
            
    def addJob(self, evt=None):
        client = self.gui.client_entry.GetValue()
        frequency = self.gui.freq_choice.GetValue()
        count = self.gui.count_combo.GetValue()

class ContactsWindow():
    def __init__(self, choose=False):
        self.gui = gui.ChooseContact(window)
        self.contacts = {}
        self.contact = None
        
        self.gui.contact_list.InsertColumn(0, "Name", width=100)
        self.gui.contact_list.InsertColumn(1, "Company", width=100)
        self.gui.contact_list.InsertColumn(2, "Phone", width=100)
        self.gui.contact_list.InsertColumn(3, "Address", width=300)
        
        self.gui.filter_entry.Bind(wx.EVT_TEXT, self.filter)
        
        if not choose:
            self.gui.title_label.SetLabel("Contacts")
            self.gui.cancel_button.Show(False)
            self.gui.Layout()
        
        self.fillContacts()
        
        self.gui.ok_button.Bind(wx.EVT_BUTTON, lambda evt: self.returnContact())
        self.gui.cancel_button.Bind(wx.EVT_BUTTON, lambda evt: self.returnContact(cancel=True))
        self.gui.ok_button.SetDefault()
        
    def returnContact(self, cancel=False):
        selection = self.gui.contact_list.GetFirstSelected()
        if not cancel and selection != -1:
            self.contact = self.contacts[selection]
            
        self.gui.Close()
        
    def fillContacts(self):
        contacts_dict = contacts.getAllContactsInGroup("Clients")
        
        i = 0
        for atomid in contacts_dict:
            name = contacts.getFullName(atomid)
            company = contacts.getCompany(atomid)
            phone = contacts.getPhoneNumber(atomid)
            address = contacts.getAddress(atomid)
            self.gui.contact_list.Append((name,
                                          company is None and " " or company,
                                          phone is None and " " or phone,
                                          address is None and " " or address))
            self.contacts[i] = atomid
            i += 1
            
    def filter(self, evt):
        contents = self.gui.filter_entry.GetValue()
        index = self.gui.contact_list.FindItem(0, contents, True)
        self.gui.contact_list.Select(self.gui.contact_list.GetFirstSelected(), False)
        if index != None:
            self.gui.contact_list.EnsureVisible(index)
            self.gui.contact_list.Select(index)

class MenuBar():
    def __init__(self):
        window.Bind(wx.EVT_MENU, self.showContacts, window.view_contacts_menuitem)
    
    def showContacts(self, evt=None):
        contacts_window = ContactsWindow(False)
        contacts_window.gui.ShowModal()

class Main:
    def __init__(self):
        self.curr_date = datetime.date.today()
        self.curr_view = "Month"
        
        window.change_view_button.Bind(wx.EVT_BUTTON, self.changeView)
        window.next_time_button.Bind(wx.EVT_BUTTON, lambda evt: self.changeDate("forward"))
        window.now_time_button.Bind(wx.EVT_BUTTON, lambda evt: self.changeDate("now"))
        window.prev_time_button.Bind(wx.EVT_BUTTON, lambda evt: self.changeDate("backward"))
        
        self.events = self.fetchEvents(self.curr_date)
        
        window.add_job_button.Bind(wx.EVT_BUTTON, self.addJob)
        
    def addJob(self, evt):
        addjob = AddJobWindow()
        addjob.gui.ShowModal()
    
    def fetchEvents(self, date):
        month = gcal.getEventsList(date)
        if not month:
            window.statusbar.SetStatusText("Updating...")
            month = gcal.getEventsList(date, True)
        window.statusbar.SetStatusText("")
        
        return month
    
    def changeDate(self, direction):
        year = self.curr_date.year
        month = self.curr_date.month
        if direction == "now":
            date = datetime.date.today()
        else:
            if self.curr_view == "Month":
                date = datetime.date(year, month, 1)
                if direction == "forward":
                    month_length = calendar.monthrange(year, month)[1]
                    date += datetime.timedelta(days=month_length)
                elif direction == "backward":
                    date -= datetime.timedelta(days=1)
                    month_length = calendar.monthrange(date.year, date.month)[1]
                    date -= datetime.timedelta(days=(month_length - 1))
            elif self.curr_view == "Week":
                day = self.curr_date.day
                days_to_sunday = FIXED_WEEKDAYS[calendar.weekday(year, month, day)]
                sunday = self.curr_date - datetime.timedelta(days=days_to_sunday)
                if direction == "forward":
                    date = sunday + datetime.timedelta(days=7)
                else:
                    date = sunday - datetime.timedelta(days=7)
                
        self.curr_date = date
        self.fetchEvents(self.curr_date)
        self.updateViews()
            
    def updateViews(self):
        self.curr_date = self.curr_date
        wxcal.setCalendarTitle(self.curr_date.year, self.curr_date.month)
        wxcal.calendar.setMonth(self.curr_date.year, self.curr_date.month)
        wxcal.colorCodeCalendar()
        
        dayview.setWeekContainingDate(self.curr_date)
    
    def changeView(self, evt):
        btn = window.change_view_button
        if self.curr_view == "Week":
            self.curr_view = "Month"
            btn.SetLabel("Week")
            self.showMonthView()
        else:
            self.curr_view = "Week"
            btn.SetLabel("Month")
            self.showWeekView()
            
    def showWeekView(self):
        window.month_view.Show(False)
        window.day_view.Show(False)
        window.day_list_view.Show(True)
        window.Layout()
        
    def showMonthView(self):
        window.day_list_view.Show(False)
        window.day_view.Show(True)
        window.month_view.Show(True)
        window.Layout()

if __name__ == '__main__':
    app = wx.App()
    
    window = gui.GUI(None)
    menubar = MenuBar()
    
    gapi = googleapi.API()
    gapi.authenticate()
    
    gcal = googleapi.Calendar(gapi)
    contacts = googleapi.Contacts(gapi)
    
    wxcal = Calendar()
    joblist = JobList(window.day_list)
    jobdetails = JobDetails()
    dayview = DayView()
    main = Main()
    
    wxcal.colorCodeCalendar()
    dayview.setWeekContainingDate(datetime.date.today())
    
    window.Show()
    app.MainLoop()