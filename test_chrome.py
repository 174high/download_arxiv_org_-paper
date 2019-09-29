import pychrome
from bs4 import BeautifulSoup
import requests

FILL_VALUE_IN_FORM = 'document.getElementById("%s").setAttribute("value", "%s");'
CLICK_BY_ID = 'document.getElementById("%s").click()'
#CLICK_ONE_BY_CLASS = 'document.getElementsByClassName("%s").click()'
CLICK_ONE_BY_CLASS = 'document.getElementsByClassName("target")%s.click()'
CLICK_ALL_BY_CLASS = '''
var nodes = document.getElementsByClassName("%s");
for (var i=0;i<nodes.length;i++){
    nodes[i].click();
}
'''
CLICK_ALL_BY_HREF = '''
var nodes = document.querySelectorAll("a[href]");
for (var i=0;i<nodes.length;i++){
    console.log("hello world"); 
    nodes[i].click();
}
'''

CLICK_A_NUM = '''
document.querySelectorAll("a")[%s].click();
'''

# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9221")

# create a tab
tab = browser.new_tab()


# register callback if you want
def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))

tab.Network.requestWillBeSent = request_will_be_sent

# start the tab 
tab.start()

# call method
tab.Network.enable()

# call method with timeout
tab.call_method('Page.navigate',url="https://arxiv.org/search/?query=Autonomous+Vehicle&searchtype=all&source=header&order=-announced_date_first&size=50&abstracts=show&start=0", _timeout=5)

# wait for loading
tab.wait(2)

html = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")

#print(html)

soup = BeautifulSoup(((html['result'])['value']),"html.parser")

number=0

for link in soup.find_all("a"):
#    print(link)
#    print(type(str(link)))   
   if str(link).find("pdf") > 0 :
    	print(link)
    	print(type(str(link))) 
    	break 
   number=number+1 

print("______________",len(soup.find_all("a")))

cmd=CLICK_A_NUM % number

print(cmd)
tab.Runtime.evaluate(expression=cmd)

# wait for loading
tab.wait(20)

html = tab.Runtime.evaluate(expression="document.documentElement.outerHTML")

print(html)

soup = BeautifulSoup(((html['result'])['value']),"html.parser")

number=0 

for link in soup.find_all("a"):
    print(link)
    if str(link).find("here") > 0 :
    	print(link)
    	print(type(str(link))) 
    	break 
    number=number+1 

print("______________",len(soup.find_all("b")))

cmd=CLICK_A_NUM % number

print(cmd)
tab.Runtime.evaluate(expression=cmd)

# wait for loading
tab.wait(20)


# stop the tab (stop handle events and stop recv message from chrome)
tab.stop()

# close tab
browser.close_tab(tab)

















