
'''
Created on 2018/03/06

@author: WangLuming
'''
import urllib
import urllib2
values={}
values['username']=""
values['password']=""
data=urllib.urlencode(values)
url=""
request=urllib2.Request(url,data)   #post
#request = urllib2.Request("%s?%s"%(url,data))   #get
response=urllib2.urlopen(request)
print response.read()

