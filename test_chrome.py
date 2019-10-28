import pychrome
from bs4 import BeautifulSoup
import requests
from awesome import RMPDownload

from openpyxl import load_workbook
from openpyxl import Workbook
import os,sys
import shutil 

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
                self.excel("./tamplate/","arxiv.xlsx","./files/","arxiv-total.xlsx",pdf_name,"test","test","test","test","test","test")
            

    def excel(self,path,name,output,name2,serial_num,titile,abstract,addr,existence,date,position):
    
        print(path)
        print(output)

        fileList=os.listdir(output)

        if(len(fileList)==0):
            shutil.copy(path+name,output)   

        fileList=os.listdir(output)

        wkbk = Workbook()

        for file in fileList:
            wb = load_workbook(output+file)
            print(wb.sheetnames[0])

            for sheet in wb:
                print("max row=",sheet.max_row,"max column=",sheet.max_column)
  
                file_num=2
                exist=False
                while(file_num<=sheet.max_row):
                    if(sheet.cell(row=file_num, column=1)==serial_num):
                        exist=True
                        break
                    file_num=file_num+1 

                next_row=sheet.max_row+1

                if(exist==False):
                    sheet.cell(row=next_row, column=1,value=serial_num)
                    sheet.cell(row=next_row, column=2,value=titile)
                    sheet.cell(row=next_row, column=3,value=abstract)
                    sheet.cell(row=next_row, column=4,value=addr)
                    sheet.cell(row=next_row, column=5,value=existence)
                    sheet.cell(row=next_row, column=6,value=date)
                    sheet.cell(row=next_row, column=7,value=position)

                wb.save(output+"tmp.xlsx")
                                
        shutil.copy(output+"tmp.xlsx",output+name2)             
        os.remove(output+"tmp.xlsx")
	
        try:
            os.remove(output+name) 
        except FileNotFoundError: 
            print("ignore it ")

if __name__ == "__main__" :
    c=crawler() 
    c.call_web()
#    c.excel("./files/","./files/","test","test","test","test","test","test","test")












