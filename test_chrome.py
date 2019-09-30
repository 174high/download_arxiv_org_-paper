import pychrome
from bs4 import BeautifulSoup
import requests
from awesome import RMPDownload

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

class crawler():

    def __init__(self,*args,**kwargs):
        # create a browser instance
        self.browser = pychrome.Browser(url="http://127.0.0.1:9221")
        # create a tab
        self.tab = self.browser.new_tab()
        #self.tab.Network.requestWillBeSent = self.request_will_be_sent
        # start the tab
        self.tab.start()
        # call method
        self.tab.Network.enable()
        self.t=RMPDownload("C:\\Users\\shijonn\\Desktop\\cop\\automation"+"\\")


    # register callback if you want
    def request_will_be_sent(**kwargs):
        print("loading: %s" % kwargs.get('request').get('url'))

    def call_web(self): 

        # call method with timeout
        self.tab.call_method('Page.navigate',url="https://arxiv.org/search/?query="+"Autonomous+Vehicle"+"&searchtype=all&source=header&order=-announced_date_first&size=50&abstracts=show&start=0", _timeout=5)

        # wait for loading
        self.tab.wait(2)

        html = self.tab.Runtime.evaluate(expression="document.documentElement.outerHTML")

        #print(html)
        soup = BeautifulSoup(((html['result'])['value']),"html.parser")

        number_pdf=0
        control_1=0

        for link in soup.find_all("a"):
        #    print(link)
        #    print(type(str(link)))   
            if str(link).find("pdf") > 0 :
                print(link)
                #print(type(str(link)))
                a=str(link).find("pdf")
                pdf_name=str(link)[a+4:a+14]
                print(pdf_name)
                number_pdf=number_pdf+1
            
                cmd=CLICK_A_NUM % control_1

                print(cmd)
                self.tab.Runtime.evaluate(expression=cmd)

                # wait for loading
                self.tab.wait(20)

                html = self.tab.Runtime.evaluate(expression="document.documentElement.outerHTML")

                #print(html)

                soup = BeautifulSoup(((html['result'])['value']),"html.parser")

                control_2=0

                for link in soup.find_all("a"):
                    print(link)
                    if str(link).find("here") > 0 :
                        print(link)
                        print(type(str(link)))
                        self.t.download_by_quip("https://arxiv.org/search/?query="+"Autonomous+Vehicle"+"&searchtype=all&source=header&order=-announced_date_first&size=50&abstracts=show&start=0",pdf_name+".pdf",control_1,control_2)
                        break
                    control_2=control_2+1

            control_1=control_1+1

        print("the amount of pdf =",number_pdf)
'''
        number_title=0

        for link in soup.find_all("p"):
        #    print(link)
        #    print(type(str(link)))
            if str(link).find("title is-5 mathjax") > 0 :
        #        print(link)
        #        print(type(str(link)))
                print(link.text)
                number_title=number_title+1

        print("the amount of title=",number_title)

        number_abstract=0

        for link in soup.find_all("p"):
        #    print(link)
        #    print(type(str(link)))
            if str(link).find("abstract-full has-text-grey-dark mathjax") > 0 :
        #        print(link)
        #        print(link.text)
                a=link.text.find("More")+4                
                b=link.text.find("Less")-2
                c=link.text[a:b]
                print(c)       

                number_abstract=number_abstract+1

        print("the amount of abstract=",number_abstract)

        if number_pdf==number_title==number_abstract:
            print("everything goes well")
'''



if __name__ == "__main__" :
    c=crawler()
    c.call_web()














