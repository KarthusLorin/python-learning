#coding:utf-8
#对http://www.something.com形式的URL进行分割

url = raw_input('Please enter the URL: ')
domain = url[11:-4]

print "Domain name: " + domain