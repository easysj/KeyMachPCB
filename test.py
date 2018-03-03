#!/usr/bin/python
#-*- coding: utf-8 -*-

import web
import markdown

exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
html = '''
    <html lang="zh-cn">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link href="default.css" rel="stylesheet">
    <link href="github.css" rel="stylesheet">
    </head>
    <body>
    %s
    </body>
    </html>
    '''





class test:
    def GET(self,mdfile): 
        mdstr = open("static/"+mdfile,"rb").read().decode("utf8")
        ret = markdown.markdown(mdstr,extensions=exts)
        return html%ret
    
class StaticFile:
    def GET(self,file):
        web.seeother("/static/"+file)
app = web.application(mapping=(
    "/(.*\.md)",test
    ,"/(.*\.(?:css|jpg|pdf|PCB))",StaticFile  
    ))
app.run()
