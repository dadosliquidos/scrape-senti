from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

        
class Scrape:
    def __init__(self):
        pass

    @classmethod    
    def Scraping(cls, objeto_navegador):
        siteHtml = BeautifulSoup(objeto_navegador.page_source,'html.parser')

        
        
        objeto_navegador.quit()

        return siteHtml

    @classmethod
    def get_comments(cls, html):
        '''
            retorna uma lista com os comentários do post do instagram
        '''
        comments = html.find_all('div','html-div xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x9f619 xjbqb8w x78zum5 x15mokao x1ga7v0g x16uus16 xbiv7yw x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1')
        list_comments = []
        for comment in comments:
            #print(comment.text.strip()) 
            list_comments.append(comment.text.strip())

        return list_comments



    
    @classmethod
    def scroll_comments(cls,driver):
        script = '''
            // Pega o primeiro elemento iframe na página
            var iframe = document.getElementsByClassName("x5yr21d xw2csxc x1odjw0f x1n2onr6")[0];
            var y = iframe.scrollHeight;
            iframe.scrollTo(0,y)
                '''
        height_script = '''
            iframe = document.getElementsByClassName("x5yr21d xw2csxc x1odjw0f x1n2onr6")[0];
            return iframe.scrollHeight;
                        
                        '''
        

        height = driver.execute_script(height_script)
        while True:
            #time.sleep(3)
            height = driver.execute_script(height_script)
            driver.execute_script(script)
           # time.sleep(30)
           
            max_wait_time = 600
            height_changed = False
            start_time = time.time()
            while (time.time() - start_time) < max_wait_time:
                height_new = '''
                iframe = document.getElementsByClassName("x5yr21d xw2csxc x1odjw0f x1n2onr6")[0];
                return iframe.scrollHeight;     
                '''
                if driver.execute_script(height_new) > height:
                    height = driver.execute_script(height_new)
                    height_changed = True
                    break
            
            if not height_changed:
                print('Scrollado com sucesso!')
                break
           # if height == driver.execute_script(height_new):
            #    print('Scrollado com sucesso!')
             #   break
            
       
       
       
       


 