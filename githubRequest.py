# -*- coding: utf-8 -*-
#github follower 

from selenium import webdriver
import time

class Github(object):
    #constructor
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
        self.followersName=[]
        self.followersUsername=[]
    def signIn(self):
        self.browser.get("https://github.com/login")
        self.browser.fullscreen_window()
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
        
        time.sleep(1)
        
        self.browser.find_element_by_xpath("//*[@id='login']/form/div[3]/input[8]").click()
        
        time.sleep(1)
        self.browser.get("https://github.com/{}").format(self.username)
        time.sleep(1)
        
        self.browser.get("https://github.com/{}?tab=followers").format(self.username)
        time.sleep(1)
    
    def loadFollowers(self):
        items=self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        #to take followers and username
        for i in items:
            self.followersName.append(i.find_element_by_css_selector(".f4.link-gray-dark").text)
            self.followersUsername.append(i.find_element_by_css_selector(".link-gray.pl-1").text)                        

    def getFollowers(self):
        self.browser.get("https://github.com/{}?tab=followers".format(self.username))
        time.sleep(1)
        self.loadFollowers()
        #this loop to take all followers because f you have more than 50 followers they are next page
        #Github show us every page just 50 followers that's why we should change page check all followers
        while True: 
            links=self.browser.find_element_by_class_name("BtnGroup").find_elements_by_tag_name("a")
            if(len(links)==1):
                if(links[0].text=="Next"):
                    links[0].click()
                    time.sleep(1)
                    #to take followers and username
                    self.loadFollowers()
                else:
                    break            else:
                for link in links:
                    if(link.text=="Next"):
                        link.click()
                        time.sleep(1)
                        #to take followers and username
                        self.loadFollowers()
                    else:
                        continue
        self.browser.close()            
git=Github("yourUsername","yourPassword")
#git.signIn()
git.getFollowers()
print(git.followersName)
print(git.followersUsername)

