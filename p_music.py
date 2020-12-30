import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from decouple import config 

email=config('EMAIL')
password=config('PASSWORD')

def play():

    PATH = "/Users/abraraltaflone/code/python/web_scrap/chromedriver" 
    driver = webdriver.Chrome(PATH) 
    song = search.get()
    driver.get('https://open.spotify.com/search/'+'%20'.join(song.split(" ")[:]))
    # try:
    #     run = driver.find_element_by_class_name("_38168f0d5f20e658506cd3e6204c1f9a-scss _34cfa3028b29d1f7b0c7794ad6a9c77a-scss")
    #     run.click()

    # except:
    #     print('something went wrong... \n Please try again later. Thanks for using our service ')
    #     driver.quit()

    run = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="searchPage"]/div/div/section[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/img'))
    )
    run.click()

    signIn = False

    while( signIn == False):
        login =WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'_3f37264be67c8f40fa9f76449afdb4bd-scss e6ed3359ee250e2ecc13253d4db86076-scss')))
        login.click()
    #email 
    #password 
    #login 
        # user_email=driver.find_element_by_id('login-username')
        # element = driver.find_element_by_name('username')
        # # user_email =WebDriverWait(driver,10).until(
        # # EC.presence_of_element_located((By.XPATH,''))
        # # )
        # print(user_email)
        # user_email.send_keys(email) 
        user_password =WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div/form/div[2]/div/input')))
        user_password.send_keys(password)
        user_login =WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="login-button"]'))
        )
        user_login.click()
        signIn =True

root =tk.Tk()

root.title('Play Music ')
root.resizable(False,False)
root.geometry('200x200')

tk.Label(root,text="One Search Can Make\n You Play Your Fav ").pack()

search = tk.Entry(root, width=40)
search.pack(pady=25,padx=10)

button = tk.Button(root,text='Play',command=play,height=2,width=10)
button.pack(pady=20)



tk.mainloop()