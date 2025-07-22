# -*- coding: utf-8 -*-

#--------------------------------------------------------------------------
# Python code generated with wxFormBuilder (version 3.9.0 Jun 14 2020)
# http://www.wxformbuilder.org/
#
# PLEASE DO *NOT* EDIT THIS FILE!
#--------------------------------------------------------------------------

import wx
import wx.xrc

import gettext
_ = gettext.gettext

#--------------------------------------------------------------------------
#  Class MyFrame1
#---------------------------------------------------------------------------

class MyFrame2 ( wx.Frame ):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,460 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		self.SetBackgroundColour(wx.Colour( 239, 235, 235 ))

		main = wx.BoxSizer(wx.VERTICAL)

		shou = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, _(u"收"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText1.Wrap(-1)

		shou.Add(self.m_staticText1, 0, wx.ALL, 5)

		shouItemChoices = []
		self.shouItem = wx.ComboBox(self, wx.ID_ANY, _(u"绿宝石"), wx.DefaultPosition, wx.DefaultSize, shouItemChoices, 0)
		shou.Add(self.shouItem, 0, wx.ALL, 5)

		self.shouNam = wx.TextCtrl(self, wx.ID_ANY, _(u"1"), wx.DefaultPosition, wx.DefaultSize, 0)
		shou.Add(self.shouNam, 0, wx.ALL, 5)

		self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, _(u"个"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText2.Wrap(-1)

		shou.Add(self.m_staticText2, 0, wx.ALL, 5)


		main.Add(shou, 0, wx.EXPAND, 5)

		bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, _(u"换得"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText3.Wrap(-1)

		bSizer5.Add(self.m_staticText3, 0, wx.ALL, 5)

		sellItemChoices = []
		self.sellItem = wx.ComboBox(self, wx.ID_ANY, _(u"面包"), wx.DefaultPosition, wx.DefaultSize, sellItemChoices, 0)
		bSizer5.Add(self.sellItem, 0, wx.ALL, 5)

		self.sellNum = wx.TextCtrl(self, wx.ID_ANY, _(u"4"), wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer5.Add(self.sellNum, 0, wx.ALL, 5)

		self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, _(u"个"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText4.Wrap(-1)



		bSizer5.Add(self.m_staticText4, 0, wx.ALL, 5)


		main.Add(bSizer5, 0, wx.EXPAND, 5)

		self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
		main.Add(self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5)

		nbt = wx.BoxSizer(wx.HORIZONTAL)

		shou = wx.BoxSizer(wx.VERTICAL)

		self.shouNBT = wx.StaticText(self, wx.ID_ANY, _(u"收购物品NBT"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.shouNBT.Wrap(-1)

		shou.Add(self.shouNBT, 0, wx.ALL, 5)

		self.shouInput = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
		self.shouInput.SetFont(wx.Font( 11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ))
		self.shouInput.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ))

		shou.Add(self.shouInput, 1, wx.ALL|wx.EXPAND, 5)


		nbt.Add(shou, 1, wx.EXPAND, 5)

		sell = wx.BoxSizer(wx.VERTICAL)

		self.sellNBT = wx.StaticText(self, wx.ID_ANY, _(u"售卖物品NBT"), wx.DefaultPosition, wx.DefaultSize, 0)
		self.sellNBT.Wrap(-1)

		sell.Add(self.sellNBT, 0, wx.ALL, 5)

		self.sellInput = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
		self.sellInput.SetFont(wx.Font( 11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ))
		self.sellInput.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ))

		sell.Add(self.sellInput, 1, wx.ALL|wx.EXPAND, 5)


		nbt.Add(sell, 1, wx.EXPAND, 5)


		main.Add(nbt, 1, wx.EXPAND, 5)

		self.add = wx.Button(self, wx.ID_ANY, _(u"添加"), wx.DefaultPosition, wx.DefaultSize, 0)
		main.Add(self.add, 0, wx.EXPAND, 5)


		self.SetSizer( main )
		self.Layout()

		self.Centre(wx.BOTH)

		self.add.Bind(wx.EVT_BUTTON, self.OnAdd)
	def OnAdd(self, event):
		sellItem = self.sellItem.GetValue()
		sellNum = self.sellNum.GetValue()
		shouItem = self.shouItem.GetValue()
		shouNam = self.shouNam.GetValue()



		self.Destroy()

class MyFrame1 ( wx.Frame ):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,460 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)
		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		self.SetBackgroundColour(wx.Colour( 239, 235, 235 ))

		main = wx.BoxSizer(wx.HORIZONTAL)

		self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
		self.m_textCtrl8.SetFont(wx.Font( 11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas" ))
		self.m_textCtrl8.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ))

		main.Add(self.m_textCtrl8, 1, wx.ALL|wx.EXPAND, 5)

		bSizer2 = wx.BoxSizer(wx.VERTICAL)

		projectChoices = []
		self.project = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, projectChoices, 0)
		bSizer2.Add(self.project, 1, wx.ALL|wx.EXPAND, 5)

		self.add = wx.Button(self, wx.ID_ANY, _(u"添加项目"), wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer2.Add(self.add, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5)

		self.delete = wx.Button(self, wx.ID_ANY, _(u"删除项目"), wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer2.Add(self.delete, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT|wx.EXPAND, 5)

		self.invincibility = wx.CheckBox(self, wx.ID_ANY, _(u"村民无敌"), wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer2.Add(self.invincibility, 0, wx.ALL, 5)

		self.NoAI = wx.CheckBox(self, wx.ID_ANY, _(u"无AI"), wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer2.Add(self.NoAI, 0, wx.ALL, 5)


		main.Add(bSizer2, 1, wx.EXPAND, 5)


		self.SetSizer( main )
		self.Layout()

		self.Centre(wx.BOTH)


		self.add.Bind(wx.EVT_BUTTON, self.OnAdd)

		self.delete.Bind(wx.EVT_BUTTON, self.OnDelete)

		self.project.AppendItems(["项目1", "项目2", "项目3"])

	def OnAdd(self, event):
		app = wx.App()
		frame = MyFrame2(None)
		frame.Show()
		app.MainLoop()

	def OnDelete(self, event):
		try:
			self.project.Delete(self.project.GetSelection())
		except:
			wx.MessageBox(u"请选择一个项目", u"提示")



	def __del__( self ):
		pass



	def __del__( self ):
		pass




if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame1(None)
	frame.Show()
	app.MainLoop()