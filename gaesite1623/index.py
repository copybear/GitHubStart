#!/usr/bin/env python
# encoding: utf-8
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from google.appengine.ext import db
from google.appengine.api import users
from myutility import htmlFactory
from mymodel import TableDefine
from mymodel import Urls
from mymodel import MyData
class MainHandler(webapp.RequestHandler):
	def get(self):
		user = users.get_current_user() 
		if user:
			greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
			(user.nickname(), users.create_logout_url("/index.pp")))
		else:
			greeting = ("Get the <a class='header'' href=\"%s\">login</a> on google account." % 
			users.create_login_url("/index.pp"))
		
		hf = htmlFactory()
		head = hf.getHtmlHeader("test page!")

        #tableデータの取得
		datas = MyData.all().order('-time').fetch(10, 0)		
		dfs = []
		dfs.append(TableDefine("time",0,"label"))
		dfs.append(TableDefine("message",0,"label"))
		dfs.append(TableDefine("name",0,"label"))
		table = hf.getDbTable(datas,dfs)

		#メッセージリンク
		if user: 
			strMsgLink="<a href='/home.pp'>Send Message!</a>"
		else:
			strMsgLink="<span class='warning'>You can not Send Message.</a>"

		fpath = os.path.join(os.path.dirname(__file__),'views','index.html')
		params = {'message':'Please Enter ','greeting':greeting,'head':head,'table':table,'send':strMsgLink}
		html = template.render(fpath,params)
		self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write(html)

def main():
	application=webapp.WSGIApplication([('/index.pp',MainHandler)],debug=True)
	util.run_wsgi_app(application)

if __name__ == '__main__':
    main()