#!/usr/bin/env python
# encoding: utf-8
from google.appengine.ext import db

class TableDefine(object):
	def __init__(self,_nm,_ln,_tp):
		self.colName=_nm
		self.colLength=_ln
		self.colType=_tp
	
	def getColContent(self,_val):
		if self.colType=="text":
			return """<input class="text" name=""" + self.colName + """ type="text" value=""" + _val  + """ maxlength=""" + self.colLength + """ /> """
		elif self.colType=="number":
			return """<input class="numtext" name=""" + self.colName + """ type="text" value=""" + _val + """ maxlength=""" + self.colLength + """ /> """
		elif self.colType=="date":
			return """<input class="datetext" name=""" + self.colName + """ type="text" value=""" + _val + """ maxlength=""" + self.colLength + """ />  """
		elif self.colType=="label":
			return """<div name=""" + self.colName + """ class="label" >""" + _val + """ </span>"""
		elif self.colType=="numlabel":
			return """<div name=""" + self.colName + """ class="numlabel" >""" + _val + """ </span>"""

class Urls(db.Model):
	name = db.StringProperty(required=True,multiline=False)
	url = db.StringProperty(multiline=False)
	target = db.StringProperty(multiline=False)
	time = db.DateTimeProperty(auto_now_add=True)