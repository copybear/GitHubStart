#!/usr/bin/env python
# encoding: utf-8

class htmlFactory():
	def getHtmlHeader(self,_title):
		return """
		<html xmlns="http://www.w3.org/1999/xhtml">
		<head>
			<title>""" + _title + """</title>
			<link rel="stylesheet" href="css/style.css">
			<script type="text/javascript" src="js/common.js"></script>
			<link href='http://fonts.googleapis.com/css?family=Gochi+Hand' rel='stylesheet' type='text/css'>
			<link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono:700' rel='stylesheet' type='text/css'>
			<link href='http://fonts.googleapis.com/css?family=Butcherman+Caps' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Aubrey' rel='stylesheet' type='text/css'>
		</head>
		"""
	def getDbTable(self,_db,_dfs):
		self.str="<table>"
		# 列ヘッダの設定
		self.str= self.str + """<tr>"""
		for col in _dfs:
			self.str=self.str + """
			          <th>""" + col.colName + """</th>
		"""
		self.str=self.str + """</tr>"""		
		# データの設定
		for db in _db:
			self.str= self.str + """<tr>"""
			for col in _dfs:
				self.str=self.str + """
				          <td>""" + col.getColContent(db[col.colName]) + """</td>
			"""
			self.str=self.str + """</tr>"""
		self.str=self.str + """</table>"""
		return self.str
			