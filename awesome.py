from os import path, remove
from time import sleep
import os


from driver_builder import DriverBuilder

from selenium import webdriver  
from selenium.webdriver.chrome import webdriver as chrome_webdriver
from selenium.webdriver import Chrome

class RMPDownload:
    def __init__(self,path):
        self.path_root=path
        self.driver_builder = DriverBuilder()
        download_path = self.path_root
        print("download_path=",download_path)
        self.driver = self.driver_builder.get_driver(download_path, headless=True)

    def download(self,equipment):

        self.driver.get("https://arxiv.org/search/?query=Autonomous+Vehicle&searchtype=all&source=header&order=-announced_date_first&size=50&abstracts=show&start="+equipment) 

        try :
            js = ''' document.querySelectorAll("a")[16].click();

                
            '''
            self.driver.execute_script(js)
        except: 
            print("exception 1 ")

        sleep(10)  

        try :
            js = ''' document.querySelectorAll("a")[1].click();

                
            '''
            self.driver.execute_script(js)
        except:
            print("exception 2 ")

        self.wait_until_file_exists("1909.12288.pdf", 20)

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

    def download_by_quip(self,equipment):
        print("testing download")

        fileList=os.listdir(self.path_root)
        for file in fileList:
            print("file name=",file)
            if file.find(equipment) >=0 :
                os.remove(self.path_root+file)

        self.download(equipment)

if __name__ == "__main__":
 

    t=RMPDownload("C:\\Users\\shijonn\\Desktop\\cop\\automation"+"\\")
    t.download_by_quip("0")












