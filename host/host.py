import tkinter as tk
from tkinter import ttk
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



win = tk.Tk()

win.title("Maximized Window")

# Maximize the window
win.attributes("-alpha", True)
win.title("Python GUI App")

ttk.Label(win, text="Selenium Automation").pack()

# Define the dropdown options
options = [
    "|   |___Programming",
    "|   |___Web Development"

]

# Create the combobox widget
combobox = ttk.Combobox(win, values=options)
combobox.pack()

def stop_app():
    win.destroy()

stop_duration = 5000


def open_website():
            #-------------------------------------------------------------------------------
            # Setup
            Username = 0
            Email = 1
            URL = 2

            with open('data.csv', 'r') as csv_file:

                csv_reader = csv.reader(csv_file)

            #-------------------------------------------------------------------------------
            # Web Automation

                for line in csv_reader:


                    driver = webdriver.Firefox()
                    driver.get('https://hostingtres.com/submit.php')
                    driver.maximize_window()
                    
                    #time.sleep(5)
                    element = driver.find_elements(By.NAME, 'CATEGORY_ID')
                    print('ok')
                    drp = Select(element[0])
                    selected_option = combobox.get()  # Get the selected option from the combobox
                    drp.select_by_visible_text(selected_option)
                    time.sleep(4)

                    goto = driver.find_elements(By.XPATH, '//*[@id="ok"]')
                    goto[0].click()

                    freelink = driver.find_element("xpath", '//*[@id="submitForm"]/table/tbody/tr/td/div/div[1]/table/tbody/tr[2]/td[1]/input')
                    freelink.click()
                    time.sleep(5)

                    goto = driver.find_elements(By.XPATH, '//*[@id="submitForm"]/table/tbody/tr/td/div/div[1]/table/tbody/tr[3]/td/center/input')
                    goto[0].click()

                    Title_field = driver.find_element("xpath", '//*[@id="TITLE"]')
                    Title_field.send_keys(line[3])
                    time.sleep(3)


                    Description_field = driver.find_element("xpath", '//*[@id="DESCRIPTION"]')
                    Description_field.send_keys(line[4])
                    time.sleep(3)

                    Ownername_field = driver.find_element("xpath", '//*[@id="OWNER_NAME"]')
                    Ownername_field.send_keys(line[0])
                    time.sleep(3)

                    Email_field = driver.find_element("xpath", '//*[@id="OWNER_EMAIL"]')
                    Email_field.send_keys(line[1])
                    time.sleep(40)

                    agree = driver.find_elements(By.NAME, 'AGREERULES')
                    agree[0].click()
                    time.sleep(10)

                    # submit = driver.find_elements(By.XPATH, '//*[@id="submitForm"]/table/tbody/tr[12]/td/input')
                    # submit[0].click()
                    print("completed")
                    win.after(stop_duration, stop_app)
                    

button = ttk.Button(win, text="Open Website", command=open_website)
button.pack()
win.mainloop()   
    