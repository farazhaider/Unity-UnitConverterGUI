# Title: Unit Converter
# Authors:
# Arnav Akhoury MIT CSE    Faraz Haider MIT CSE 
# converts distance, area, volume, weight, pressure, energy, time, power torque, velocity, force, currency.
# Imports modules to send HTTP requests and employ regular expressions.
import re
from urllib2 import Request, urlopen, URLError, HTTPError



# Flag Variable
flag=1

# Sending HTTP Requests
url="http://openexchangerates.org/api/latest.json?app_id=5599bfbf15da495ebd21e275525709af"
req = Request(url)

# Error catching process
try:
        response=urlopen(req)	
except URLError as e:
        print "Connection not found. Using default values instead."
        print "Reason", e.reason
        flag=0
        x={}
        y={}
        x[60]=54
        x[1]=3.65
        x[45]=0.65
        x[74]=0.28
        

if flag==1:
        # Employing Regular expressions to extract currency information
        results=response.read()
        x=re.findall("\d+.\d+",results)
        y=re.findall('"\w+."',results)
	print x
	print y



# Imports wx Python module
import wx

# Creating application frame
class MyNotebook(wx.Frame):
        # Initialise all the dictionary elements
    def __init__(self, parent, title, distance, area, volume,
            weight, pressure, energy, time, power, force, velocity, torque,currency):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title,
            size=(640, 480))
        # style=wx.NB_TOP is default
        # could use style=wx.NB_BOTTOM
        note_book = wx.Notebook(self, wx.ID_ANY)
        # MyPage(parent, conversion dictionary, preselected choice)
        self.page1 = MyPage(note_book, distance, 0)
        self.page2 = MyPage(note_book, area, 0)
        self.page3 = MyPage(note_book, volume, 0)
        self.page4 = MyPage(note_book, weight, 0)
        self.page5 = MyPage(note_book, pressure, 0)
        self.page6 = MyPage(note_book, energy, 0)
        self.page7 = MyPage(note_book, time, 0)
        self.page8 = MyPage(note_book, power, 0)
        self.page9= MyPage(note_book, torque, 0)
        self.page10= MyPage(note_book, force, 0)
        self.page11= MyPage(note_book, velocity, 0)
        self.page12= MyPage(note_book, currency, 0)
        # Add new tabs
        note_book.AddPage(self.page1, "Distance")
        note_book.AddPage(self.page2, "Area")
        note_book.AddPage(self.page3, "Volume")
        note_book.AddPage(self.page4, "Weight")
        note_book.AddPage(self.page5, "Pressure")
        note_book.AddPage(self.page6, "Energy")
        note_book.AddPage(self.page7, "Time")
        note_book.AddPage(self.page8, "Power")
        note_book.AddPage(self.page9,"Torque")
        note_book.AddPage(self.page10,"Velocity")
        note_book.AddPage(self.page11,"Force")
        note_book.AddPage(self.page12,"Currency")
        
        # start with page1 active
        self.page1.SetFocus()
class MyPage(wx.Panel):
    """
    each panel instance creates the notbook page content
    from the given conversion dictionary convert
    """
    def __init__(self, parent, convert, preselect):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        color = '#FCFFE1'
        self.SetBackgroundColour(color)
        self.convert = convert
        # create list of possible units
        self.options = convert.keys()
        self.radiobox1 = wx.RadioBox(self, wx.ID_ANY,
            "Select a unit to convert from",
            choices=self.options, style=wx.VERTICAL)
        # set radio button 1 as selected (first button is 0)
        self.radiobox1.SetSelection(preselect)
        # bind mouse click to an action
        self.radiobox1.Bind(wx.EVT_RADIOBOX, self.onAction)
        self.radiobox2 = wx.RadioBox(self, wx.ID_ANY,
            "Select a unit to convert to  ",
            choices=self.options, style=wx.VERTICAL)
        # set radio button 1 as selected (first button is 0)
        self.radiobox2.SetSelection(preselect)
        # bind mouse click to an action
        self.radiobox2.Bind(wx.EVT_RADIOBOX, self.onAction)
        # additional widgets
        self.label1 = wx.StaticText(self, wx.ID_ANY, "" )
        self.label2 = wx.StaticText(self, wx.ID_ANY, "" )
        self.edit1 = wx.TextCtrl(self, wx.ID_ANY, value="1.0",
            size=(150, 20))
        # respond to enter key when focus is on edit1
        self.edit1.Bind(wx.EVT_TEXT_ENTER, self.onAction)
        self.edit2 = wx.TextCtrl(self, wx.ID_ANY, value="",
            size=(150, 20))
        self.button = wx.Button(self, wx.ID_ANY, label='Convert')
        self.button.Bind(wx.EVT_BUTTON, self.onAction)
        # use box sizers to layout the widgets
        # nest the 3 vertical sizers in the horizontal sizer later
        sizer_v1 = wx.BoxSizer(wx.VERTICAL)
        sizer_v2 = wx.BoxSizer(wx.VERTICAL)
        sizer_v3 = wx.BoxSizer(wx.VERTICAL)
        sizer_h = wx.BoxSizer(wx.HORIZONTAL)
        # add the widgets to the corresponding vertical sizer
        sizer_v1.Add(self.radiobox1, 0, flag=wx.ALL, border=10)
        sizer_v1.Add(self.label1, 0, wx.LEFT|wx.RIGHT|wx.TOP, 10)
        sizer_v1.Add(self.edit1, 0, wx.LEFT|wx.RIGHT, 10)
        # add a spacer to position the button lower ...
        sizer_v2.Add((0, 225), 0, wx.ALL, 10)
        sizer_v2.Add(self.button, 0, wx.ALL, 10)
        sizer_v3.Add(self.radiobox2, 0, wx.ALL, 10)
        sizer_v3.Add(self.label2, 0, wx.LEFT|wx.RIGHT|wx.TOP, 10)
        sizer_v3.Add(self.edit2, 0, wx.LEFT|wx.RIGHT, 10)
        # put the 3 vertical sizers into the horizontal sizer
        sizer_h.Add(sizer_v1, 0)
        sizer_h.Add(sizer_v2, 0)
        sizer_h.Add(sizer_v3, 0)
        # it's the horizontal sizer you have to set
        self.SetSizer(sizer_h)
        # show present selection
        self.onAction(None)
    def onAction(self, event):
        """show the selected choice"""
        index1 = self.radiobox1.GetSelection()
        unit1 = self.options[index1]
        #print unit1  # test
        s = "Enter a value (%s):" % unit1
        self.label1.SetLabel(s)
        # dito for radio box #2
        index2 = self.radiobox2.GetSelection()
        unit2 = self.options[index2]
        #print unit2  # test
        s = "Result (%s):" % unit2
        self.label2.SetLabel(s)
        value = float(self.edit1.GetValue())
        factor1 = self.convert[unit1]
        factor2 = self.convert[unit2]
        result = factor2 * value/factor1
        self.edit2.ChangeValue(str(result))
# these are the conversion dictionaries ...
# (note that units won't appear in that order)
distance ={}
# all scale factors are relative to the first unit below
distance['meter'] = 1.0
distance['micron'] = 1000000.0
distance['millimeter'] = 1000.0
distance['centimeter'] = 100.0
distance['kilometer'] = 0.001
distance['inch'] = 100.0/2.54
distance['foot'] = 100.0/30.48
distance['yard'] = 100.0/91.44
distance['mile'] = 0.001/1.609344
distance['rod'] = 1.0/5.029
area = {}
# all scale factors are relative to the first unit below
area['sq meter'] = 1.0
area['sq millimeter'] = 1000000.0
area['sq centimeter'] = 10000.0
area['sq kilometer']  = 0.000001
area['hectare'] = 0.0001
area['sq inch'] = 1550.003
area['sq foot'] = 10.76391
area['sq yard'] = 1.19599
area['acre'] = 0.0002471054
area['sq mile'] = 0.0000003861022
volume = {}
# all scale factors are relative to the first unit below
volume['cubic meter'] = 1.0
volume['microliter'] = 1000000000.0
volume['milliliter'] = 1000000.0
volume['liter'] = 1000.0
volume['pint(US)'] = 2113.376
volume['quart(US)'] = 1056.688
volume['gallon(US)'] = 264.172
volume['cubic inch'] = 61023.74
volume['cubic foot'] = 35.31467
volume['cubic yard'] = 1.307951
weight = {}
# all scale factors are relative to the first unit below
weight['kilogram'] = 1.0
weight['microgram'] = 1000000000.0
weight['milligram'] = 1000000.0
weight['gram'] = 1000.0
weight['tonne (metric)'] = 0.001
weight['dram (avd)'] = 564.38339
weight['grain'] = 15432.358
weight['ounce (avd)'] = 35.273962
weight['pound (avd)'] = 2.2046226
weight['ton (short)'] = 0.0011023113
pressure = {}
# all scale factors are relative to the first unit below
pressure['atm'] = 1.0
pressure['bar'] = 1.01325
pressure['kilopascal'] = 101.325
pressure['torr'] = 760
pressure['kg/sqcm'] = 1.033227
pressure['kg/sqm'] = 10332.27
pressure['lb/sqinch'] = 14.69595
pressure['ton(sh)/sqfoot'] = 1.058108
pressure['inch of Hg'] = 29.92126
pressure['foot of water'] = 33.89854
energy = {}
# all scale factors are relative to the first unit below
energy['calorie'] = 1.0
energy['kilocalorie'] = 0.001
energy['joule or watt-second'] = 4.1868
energy['watt-hour'] = 0.001163
energy['kilowatt-hour'] = 0.000001163
energy['liter-atmosphere'] = 0.0413205
energy['horsepower-hour metric'] = 0.00000158124
energy['erg'] = 4186800
energy['btu'] = 0.00396832
# all scale factors are relative to the first unit below
time = {}
time['seconds']= 1.0
time['minutes']= 1.0/60
time['hours']=1.0/3600
time['day']=1.0/86400
time['week']=1.0/604800
time['month']=1.0/2592000
time['year']=1.0/31556952
time['decade']=1.0/(10*31556952)
time['century']=1.0/(100*31556952)
time['millenium']=1.0/(1000*31556952)
# all scale factors are relative to the first unit below
force={}
force['newton']= 1.0
force['kgf']= 9.80665
force['dyne']= .00001
force['atomic unit of force']= 0.00000008238722
force['pound force']= 4.4482216152
# all scale factors are relative to the first unit below
velocity={}
velocity['m/s']= 1.0
velocity['km/hr']= 18.0/5.0
velocity['knots']=0.514444
velocity['ml/hr']=0.44704
velocity['furlong']=1.663095*0.0001
velocity['f/s']=3.048*0.1
# all scale factors are relative to the first unit below
power={}
power['watt']=1.0
power['horsepower']=9810.657
power['BTU']=0.293071
# all scale factors are relative to the first unit below
torque={}
torque['N-m']=1.0
torque['m-kg']=0.101971
# all scale factors are relative to the first unit below
currency={}
currency['USD']= 1.0
currency['INR']=float(x[60])
currency['Arab Emirates Dinar']=float(x[1])
currency['Brtish Pound Sterling']=float(x[45])
currency['Kuwaiti Dinar']=float(x[74])
app = wx.App(1)
# Notebook widget
mynotebook = MyNotebook(None, "Unity", distance, area,
    volume, weight, pressure, energy, time, force, velocity, power, torque, currency)
mynotebook.Show()
app.MainLoop()
