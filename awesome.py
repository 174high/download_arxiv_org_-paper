from os import path, remove
from time import sleep
import os


from driver_builder import DriverBuilder

from selenium import webdriver  
from selenium.webdriver.chrome import webdriver as chrome_webdriver
from selenium.webdriver import Chrome

CLICK_A_NUM = '''
document.querySelectorAll("a")[%s].click();
'''

class RMPDownload:
    def __init__(self,path):
        self.path_root=path
        self.driver_builder = DriverBuilder()
        download_path = self.path_root
        print("download_path=",download_path)
        self.driver = self.driver_builder.get_driver(download_path, headless=True)

    def download(self,addr,name,num1,num2):

        self.driver.get(addr) 

        try :
            js=CLICK_A_NUM % num1
            self.driver.execute_script(js)
        except: 
            print("exception 1 ")

        sleep(10)  

        try :
            js=CLICK_A_NUM % num2
            self.driver.execute_script(js)
        except:
            print("exception 2 ")

        self.wait_until_file_exists(name, 20)

        self.driver.close()

        print("done")

    def wait_until_file_exists(self, actual_file, wait_time_in_seconds=5):
        waits = 0
                      
        while waits < wait_time_in_seconds:
            fileList=os.listdir(self.path_root)
            for file in fileList:
               print("file name=",file)
               if file == actual_file :
                    return 

            print("sleeping...." + str(waits))
            sleep(.5)  # make sure file completes downloading
            waits += .5

    def download_by_quip(self,addr,name,num1,num2):
        print("testing download")

        fileList=os.listdir(self.path_root)
        for file in fileList:
            print("file name=",file)
            if file.find(name) >=0 :
                os.remove(self.path_root+file)

        self.download(addr,name,num1,num2)

if __name__ == "__main__":
 

    t=RMPDownload("C:\\Users\\shijonn\\Desktop\\cop\\automation"+"\\")


    t.download_by_quip("https://arxiv.org/search/?query="+"Autonomous+Vehicle"+"&searchtype=all&source=header&order=-announced_date_first&size=50&abstracts=show&start=0","1909.12288.pdf",16,1)

    t1=RMPDownload("C:\\Users\\shijonn\\Desktop\\cop\\automation"+"\\")

    t1.download_by_quip("https://arxiv.org/search/?query="+"Autonomous+Vehicle"+"&searchtype=all&source=header&order=-announced_date_first&size=50&abstracts=show&start=0","1909.12288.pdf",31,1)



#    t.download("https://arxiv.org/search/?query="+"Autonomous+Vehicle"+"&searchtype=all&source=header&order=-announced_date_first&size=50&abstracts=show&start=0","1909.12288.pdf",31,1)












