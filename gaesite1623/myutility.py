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
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
			<link href='http://fonts.googleapis.com/css?family=Ubuntu+Mono:700' rel='stylesheet' type='text/css'>
			<link href='http://fonts.googleapis.com/css?family=Butcherman+Caps' rel='stylesheet' type='text/css'>
			<link href='http://fonts.googleapis.com/css?family=Aubrey' rel='stylesheet' type='text/css'>
			<link href='http://fonts.googleapis.com/css?family=Gloria+Hallelujah' rel='stylesheet' type='text/css'>
			<link href='http://fonts.googleapis.com/css?family=Aclonica' rel='stylesheet' type='text/css'>
			<link href='http://fonts.googleapis.com/css?family=Unkempt' rel='stylesheet' type='text/css'>
		</head>
		"""
	def getDbTable(self,_db,_dfs):
		self.str="<table class='display'>"
		# 列ヘッダの設定
		self.str= self.str + """<tr class='display'>"""
		for col in _dfs:
			self.str=self.str + """
			          <th class='display'>""" + col.colName + """</th>
		"""
		self.str=self.str + """</tr>"""		
		# データの設定
		for db in _db:
			self.str= self.str + """<tr class='display'>"""
			for col in _dfs:
				self.str=self.str + """
				          <td class='display'>""" + col.getColContent(db[col.colName]) + """</td>
			"""
			self.str=self.str + """</tr>"""
		self.str=self.str + """</table>"""
		return self.str
			