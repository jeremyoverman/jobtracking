# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import daylistview
import wxcalendar
import daylist

###########################################################################
## Class GUI
###########################################################################

class GUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Work Tracking", pos = wx.DefaultPosition, size = wx.Size( 1024,768 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 1024,768 ), wx.DefaultSize )
		
		self.menubar = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.menubar.Append( self.file_menu, u"&File" ) 
		
		self.job_menu = wx.Menu()
		self.menubar.Append( self.job_menu, u"&Job" ) 
		
		self.contacts_menu = wx.Menu()
		self.view_contacts_menuitem = wx.MenuItem( self.contacts_menu, wx.ID_ANY, u"View contacts...", wx.EmptyString, wx.ITEM_NORMAL )
		self.contacts_menu.AppendItem( self.view_contacts_menuitem )
		
		self.menubar.Append( self.contacts_menu, u"&Contacts" ) 
		
		self.help_menu = wx.Menu()
		self.menubar.Append( self.help_menu, u"&Help" ) 
		
		self.SetMenuBar( self.menubar )
		
		container_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.container_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		cal_title_container_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.cal_title_panel = wx.Panel( self.container_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		cal_title_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.prev_time_button = wx.BitmapButton( self.cal_title_panel, wx.ID_ANY, wx.Bitmap( u"icons/previous.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		cal_title_sizer.Add( self.prev_time_button, 0, 0, 0 )
		
		self.now_time_button = wx.BitmapButton( self.cal_title_panel, wx.ID_ANY, wx.Bitmap( u"icons/now.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		cal_title_sizer.Add( self.now_time_button, 0, 0, 0 )
		
		self.next_time_button = wx.BitmapButton( self.cal_title_panel, wx.ID_ANY, wx.Bitmap( u"icons/next.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		cal_title_sizer.Add( self.next_time_button, 0, wx.RIGHT, 10 )
		
		self.calendar_title = wx.StaticText( self.cal_title_panel, wx.ID_ANY, u"May 2015", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.calendar_title.Wrap( -1 )
		self.calendar_title.SetFont( wx.Font( 18, 74, 90, 92, False, "Arial" ) )
		
		cal_title_sizer.Add( self.calendar_title, 0, wx.BOTTOM, 10 )
		
		
		cal_title_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.change_view_button = wx.Button( self.cal_title_panel, wx.ID_ANY, u"Week", wx.DefaultPosition, wx.DefaultSize, 0 )
		cal_title_sizer.Add( self.change_view_button, 0, wx.ALL, 5 )
		
		
		self.cal_title_panel.SetSizer( cal_title_sizer )
		self.cal_title_panel.Layout()
		cal_title_sizer.Fit( self.cal_title_panel )
		cal_title_container_sizer.Add( self.cal_title_panel, 0, wx.EXPAND|wx.LEFT, 5 )
		
		self.body_container_panel = wx.Panel( self.container_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		main_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.left_panel = wx.Panel( self.body_container_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		left_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.day_list_view = daylistview.DayListView(self.left_panel)
		self.day_list_view.Hide()
		
		left_sizer.Add( self.day_list_view, 2, wx.EXPAND, 0 )
		
		self.month_view = wx.Panel( self.left_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		month_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.calendar_panel = wx.Panel( self.month_view, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		calendar_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.month_calendar = wxcalendar.Calendar(self.calendar_panel)
		calendar_sizer.Add( self.month_calendar, 1, wx.EXPAND, 0 )
		
		
		self.calendar_panel.SetSizer( calendar_sizer )
		self.calendar_panel.Layout()
		calendar_sizer.Fit( self.calendar_panel )
		month_sizer.Add( self.calendar_panel, 1, wx.EXPAND, 0 )
		
		
		self.month_view.SetSizer( month_sizer )
		self.month_view.Layout()
		month_sizer.Fit( self.month_view )
		left_sizer.Add( self.month_view, 2, wx.EXPAND, 0 )
		
		self.job_panel = wx.Panel( self.left_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		job_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.job_title_label = wx.StaticText( self.job_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.job_title_label.Wrap( -1 )
		self.job_title_label.SetFont( wx.Font( 18, 74, 90, 92, False, "Arial" ) )
		
		job_sizer.Add( self.job_title_label, 0, wx.BOTTOM, 10 )
		
		job_hor_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.job_details_panel = wx.Panel( self.job_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		job_details_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.job_services_panel = wx.Panel( self.job_details_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		job_services_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		job_services_listboxChoices = []
		self.job_services_listbox = wx.ListBox( self.job_services_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, job_services_listboxChoices, 0 )
		job_services_sizer.Add( self.job_services_listbox, 0, wx.EXPAND, 0 )
		
		job_services_butt_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.job_services_add_butt = wx.BitmapButton( self.job_services_panel, wx.ID_ANY, wx.Bitmap( u"icons/add.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		job_services_butt_sizer.Add( self.job_services_add_butt, 0, 0, 0 )
		
		self.job_services_rem_butt = wx.BitmapButton( self.job_services_panel, wx.ID_ANY, wx.Bitmap( u"icons/remove.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		job_services_butt_sizer.Add( self.job_services_rem_butt, 0, 0, 0 )
		
		
		job_services_sizer.Add( job_services_butt_sizer, 1, wx.EXPAND, 5 )
		
		
		self.job_services_panel.SetSizer( job_services_sizer )
		self.job_services_panel.Layout()
		job_services_sizer.Fit( self.job_services_panel )
		job_details_sizer.Add( self.job_services_panel, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.job_time_panel = wx.Panel( self.job_details_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		job_time_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.job_start_panel = wx.Panel( self.job_time_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		job_start_time_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.job_start_time_label = wx.StaticText( self.job_start_panel, wx.ID_ANY, u"Start Time", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.job_start_time_label.Wrap( -1 )
		self.job_start_time_label.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		job_start_time_sizer.Add( self.job_start_time_label, 0, wx.ALIGN_CENTER|wx.RIGHT, 5 )
		
		job_start_time_hour_comboChoices = [ u" ", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12" ]
		self.job_start_time_hour_combo = wx.ComboBox( self.job_start_panel, wx.ID_ANY, u"12", wx.DefaultPosition, wx.Size( -1,-1 ), job_start_time_hour_comboChoices, 0 )
		self.job_start_time_hour_combo.SetSelection( 0 )
		job_start_time_sizer.Add( self.job_start_time_hour_combo, 0, wx.ALIGN_CENTER, 0 )
		
		job_start_time_min_comboChoices = [ u" ", u"00", u"15", u"30", u"45" ]
		self.job_start_time_min_combo = wx.ComboBox( self.job_start_panel, wx.ID_ANY, u"30", wx.DefaultPosition, wx.DefaultSize, job_start_time_min_comboChoices, 0 )
		self.job_start_time_min_combo.SetSelection( 0 )
		job_start_time_sizer.Add( self.job_start_time_min_combo, 0, wx.ALIGN_CENTER, 0 )
		
		job_start_time_suffix_comboChoices = [ u" ", u"AM", u"PM" ]
		self.job_start_time_suffix_combo = wx.ComboBox( self.job_start_panel, wx.ID_ANY, u"PM", wx.DefaultPosition, wx.DefaultSize, job_start_time_suffix_comboChoices, 0 )
		self.job_start_time_suffix_combo.SetSelection( 0 )
		job_start_time_sizer.Add( self.job_start_time_suffix_combo, 0, wx.ALIGN_CENTER, 0 )
		
		self.job_start_time_butt = wx.Button( self.job_start_panel, wx.ID_ANY, u"Now", wx.DefaultPosition, wx.Size( 50,23 ), 0 )
		job_start_time_sizer.Add( self.job_start_time_butt, 0, wx.ALIGN_CENTER, 0 )
		
		
		self.job_start_panel.SetSizer( job_start_time_sizer )
		self.job_start_panel.Layout()
		job_start_time_sizer.Fit( self.job_start_panel )
		job_time_sizer.Add( self.job_start_panel, 0, wx.EXPAND|wx.LEFT, 5 )
		
		self.job_end_panel = wx.Panel( self.job_time_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		job_start_time_sizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.job_end_time_label = wx.StaticText( self.job_end_panel, wx.ID_ANY, u"End Time", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.job_end_time_label.Wrap( -1 )
		self.job_end_time_label.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		job_start_time_sizer1.Add( self.job_end_time_label, 0, wx.ALIGN_CENTER|wx.RIGHT, 5 )
		
		job_end_time_hour_comboChoices = [ u" ", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12" ]
		self.job_end_time_hour_combo = wx.ComboBox( self.job_end_panel, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size( -1,-1 ), job_end_time_hour_comboChoices, 0 )
		self.job_end_time_hour_combo.SetSelection( 0 )
		job_start_time_sizer1.Add( self.job_end_time_hour_combo, 0, wx.ALIGN_CENTER, 0 )
		
		job_end_time_min_comboChoices = [ u" ", u"00", u"15", u"30", u"45" ]
		self.job_end_time_min_combo = wx.ComboBox( self.job_end_panel, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, job_end_time_min_comboChoices, 0 )
		self.job_end_time_min_combo.SetSelection( 0 )
		job_start_time_sizer1.Add( self.job_end_time_min_combo, 0, wx.ALIGN_CENTER, 0 )
		
		job_end_time_suffix_comboChoices = [ u" ", u"AM", u"PM" ]
		self.job_end_time_suffix_combo = wx.ComboBox( self.job_end_panel, wx.ID_ANY, u"PM", wx.DefaultPosition, wx.DefaultSize, job_end_time_suffix_comboChoices, 0 )
		self.job_end_time_suffix_combo.SetSelection( 0 )
		job_start_time_sizer1.Add( self.job_end_time_suffix_combo, 0, wx.ALIGN_CENTER, 0 )
		
		self.job_end_time_butt = wx.Button( self.job_end_panel, wx.ID_ANY, u"Now", wx.DefaultPosition, wx.Size( 50,23 ), 0 )
		job_start_time_sizer1.Add( self.job_end_time_butt, 0, wx.ALIGN_CENTER, 0 )
		
		
		self.job_end_panel.SetSizer( job_start_time_sizer1 )
		self.job_end_panel.Layout()
		job_start_time_sizer1.Fit( self.job_end_panel )
		job_time_sizer.Add( self.job_end_panel, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.job_time_panel.SetSizer( job_time_sizer )
		self.job_time_panel.Layout()
		job_time_sizer.Fit( self.job_time_panel )
		job_details_sizer.Add( self.job_time_panel, 0, wx.EXPAND|wx.LEFT, 35 )
		
		
		self.job_details_panel.SetSizer( job_details_sizer )
		self.job_details_panel.Layout()
		job_details_sizer.Fit( self.job_details_panel )
		job_hor_sizer.Add( self.job_details_panel, 0, wx.EXPAND, 0 )
		
		self.job_contact_panel = wx.Panel( self.job_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		job_contact_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.job_contact_name_label = wx.StaticText( self.job_contact_panel, wx.ID_ANY, u"John Doe", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.job_contact_name_label.Wrap( -1 )
		self.job_contact_name_label.SetFont( wx.Font( 12, 74, 90, 92, False, "Arial" ) )
		
		job_contact_sizer.Add( self.job_contact_name_label, 0, 0, 0 )
		
		self.job_contact_phone_label = wx.StaticText( self.job_contact_panel, wx.ID_ANY, u"(555) 555 - 5555", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.job_contact_phone_label.Wrap( -1 )
		self.job_contact_phone_label.SetFont( wx.Font( 9, 70, 90, 92, False, "Arial" ) )
		
		job_contact_sizer.Add( self.job_contact_phone_label, 0, 0, 5 )
		
		self.job_contact_address_label = wx.StaticText( self.job_contact_panel, wx.ID_ANY, u"5555 Road Name\nTown Name, State\nAddition Info", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.job_contact_address_label.Wrap( -1 )
		self.job_contact_address_label.SetFont( wx.Font( 9, 74, 93, 92, False, "Arial" ) )
		
		job_contact_sizer.Add( self.job_contact_address_label, 0, wx.TOP, 10 )
		
		
		self.job_contact_panel.SetSizer( job_contact_sizer )
		self.job_contact_panel.Layout()
		job_contact_sizer.Fit( self.job_contact_panel )
		job_hor_sizer.Add( self.job_contact_panel, 0, wx.LEFT, 35 )
		
		
		job_sizer.Add( job_hor_sizer, 1, wx.EXPAND, 5 )
		
		
		self.job_panel.SetSizer( job_sizer )
		self.job_panel.Layout()
		job_sizer.Fit( self.job_panel )
		left_sizer.Add( self.job_panel, 1, wx.EXPAND|wx.TOP, 10 )
		
		
		self.left_panel.SetSizer( left_sizer )
		self.left_panel.Layout()
		left_sizer.Fit( self.left_panel )
		main_sizer.Add( self.left_panel, 3, wx.ALL|wx.EXPAND, 5 )
		
		self.day_view = wx.Panel( self.body_container_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		day_view_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.day_list = daylist.DayList(self.day_view)
		day_view_sizer.Add( self.day_list, 1, wx.ALL|wx.EXPAND, 0 )
		
		self.day_view_butt_panel = wx.Panel( self.day_view, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		day_view_butt_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.add_job_button = wx.Button( self.day_view_butt_panel, wx.ID_ANY, u"Add Job", wx.DefaultPosition, wx.DefaultSize, 0 )
		day_view_butt_sizer.Add( self.add_job_button, 0, 0, 0 )
		
		
		day_view_butt_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.remove_job_button = wx.Button( self.day_view_butt_panel, wx.ID_ANY, u"Remove Job", wx.DefaultPosition, wx.DefaultSize, 0 )
		day_view_butt_sizer.Add( self.remove_job_button, 0, 0, 0 )
		
		
		self.day_view_butt_panel.SetSizer( day_view_butt_sizer )
		self.day_view_butt_panel.Layout()
		day_view_butt_sizer.Fit( self.day_view_butt_panel )
		day_view_sizer.Add( self.day_view_butt_panel, 0, wx.EXPAND|wx.TOP, 5 )
		
		
		self.day_view.SetSizer( day_view_sizer )
		self.day_view.Layout()
		day_view_sizer.Fit( self.day_view )
		main_sizer.Add( self.day_view, 1, wx.BOTTOM|wx.EXPAND|wx.RIGHT|wx.TOP, 5 )
		
		
		self.body_container_panel.SetSizer( main_sizer )
		self.body_container_panel.Layout()
		main_sizer.Fit( self.body_container_panel )
		cal_title_container_sizer.Add( self.body_container_panel, 1, wx.EXPAND, 0 )
		
		
		self.container_panel.SetSizer( cal_title_container_sizer )
		self.container_panel.Layout()
		cal_title_container_sizer.Fit( self.container_panel )
		container_sizer.Add( self.container_panel, 1, wx.EXPAND, 0 )
		
		
		self.SetSizer( container_sizer )
		self.Layout()
		self.statusbar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class AddJob
###########################################################################

class AddJob ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Job", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		container_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.container_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		main_sizer = wx.BoxSizer( wx.VERTICAL )
		
		repeat_sizer = wx.GridBagSizer( 0, 0 )
		repeat_sizer.SetFlexibleDirection( wx.BOTH )
		repeat_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.add_job = wx.StaticText( self.container_panel, wx.ID_ANY, u"Add Job", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.add_job.Wrap( -1 )
		self.add_job.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		repeat_sizer.Add( self.add_job, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.repeat_label = wx.StaticText( self.container_panel, wx.ID_ANY, u"Repeat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.repeat_label.Wrap( -1 )
		repeat_sizer.Add( self.repeat_label, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.client_label = wx.StaticText( self.container_panel, wx.ID_ANY, u"Client", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.client_label.Wrap( -1 )
		repeat_sizer.Add( self.client_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		client_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.client_entry = wx.TextCtrl( self.container_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.client_entry.Enable( False )
		
		client_sizer.Add( self.client_entry, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.choose_client_button = wx.Button( self.container_panel, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		client_sizer.Add( self.choose_client_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		repeat_sizer.Add( client_sizer, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 4 ), wx.EXPAND, 5 )
		
		self.every_label = wx.StaticText( self.container_panel, wx.ID_ANY, u"every", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.every_label.Wrap( -1 )
		repeat_sizer.Add( self.every_label, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		freq_choiceChoices = [ u"Monthly", u"Weekly" ]
		self.freq_choice = wx.Choice( self.container_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, freq_choiceChoices, 0 )
		self.freq_choice.SetSelection( 0 )
		repeat_sizer.Add( self.freq_choice, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		count_comboChoices = [ u"1", u"2", u"3", u"4", u"5", u"6" ]
		self.count_combo = wx.ComboBox( self.container_panel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), count_comboChoices, 0 )
		repeat_sizer.Add( self.count_combo, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.freq_label = wx.StaticText( self.container_panel, wx.ID_ANY, u"month(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.freq_label.Wrap( -1 )
		repeat_sizer.Add( self.freq_label, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		main_sizer.Add( repeat_sizer, 1, wx.EXPAND, 5 )
		
		confim_buttons_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		
		confim_buttons_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.cancel_button = wx.Button( self.container_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		confim_buttons_sizer.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		self.add_button = wx.Button( self.container_panel, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		confim_buttons_sizer.Add( self.add_button, 0, wx.ALL, 5 )
		
		
		main_sizer.Add( confim_buttons_sizer, 0, wx.EXPAND|wx.TOP, 15 )
		
		
		self.container_panel.SetSizer( main_sizer )
		self.container_panel.Layout()
		main_sizer.Fit( self.container_panel )
		container_sizer.Add( self.container_panel, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( container_sizer )
		self.Layout()
		container_sizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChooseContact
###########################################################################

class ChooseContact ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Choose Contact", pos = wx.DefaultPosition, size = wx.Size( 640,480 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		conatiner_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.container_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		main_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title_label = wx.StaticText( self.container_panel, wx.ID_ANY, u"Choose Contact", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_label.Wrap( -1 )
		self.title_label.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		main_sizer.Add( self.title_label, 0, wx.ALL, 5 )
		
		content_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		contact_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.filter_entry = wx.TextCtrl( self.container_panel, wx.ID_ANY, u"Quick find...", wx.DefaultPosition, wx.DefaultSize, 0 )
		contact_sizer.Add( self.filter_entry, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.contact_list = wx.ListCtrl( self.container_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT )
		contact_sizer.Add( self.contact_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		content_sizer.Add( contact_sizer, 1, wx.EXPAND, 5 )
		
		
		main_sizer.Add( content_sizer, 1, wx.EXPAND, 5 )
		
		confirm_button_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		
		confirm_button_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.cancel_button = wx.Button( self.container_panel, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		confirm_button_sizer.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		self.ok_button = wx.Button( self.container_panel, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		confirm_button_sizer.Add( self.ok_button, 0, wx.ALL, 5 )
		
		
		main_sizer.Add( confirm_button_sizer, 0, wx.EXPAND, 5 )
		
		
		self.container_panel.SetSizer( main_sizer )
		self.container_panel.Layout()
		main_sizer.Fit( self.container_panel )
		conatiner_sizer.Add( self.container_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( conatiner_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

