from selenium import webdriver
import pyautogui as pyg
import time

print("Welcome to the SelBot program... You will be redirected to website soon.")

# Using Chrome to access web | Specify the download path from chrome driver
# Check your chrome browser version - https://www.whatismybrowser.com/
# download Chrome Driver extension for your chrome version - http://chromedriver.chromium.org/downloads
driver = webdriver.Chrome('C:\driver\chromedriver.exe')

loop_iter = 0

try:
    # Open the website
    driver.get('http://livestockcensus.gov.in/')

    print("Logging in with username and password..\n")

    user_id_box = driver.find_element_by_id('userid')
    user_id_box.send_keys('')

    # Find password box
    pass_box = driver.find_element_by_id('password')
    # Send password
    pass_box.send_keys('')
    # Find login button
    login_button = driver.find_element_by_id('Submit')
    # Click login
    login_button.click()

    print("Loding Village List....\n")

    driver.get('http://livestockcensus.gov.in/schedule/scheduleDetailsVillageWise.action')

    #Village number
    village = input("Input Village No:")
    #save = driver.find_element_by_tag_name('tr')[village+1].find_element_by_tag_name('td')[3].find_element_by_tag_name('a')

    print("Loding Village No.:" + str(village)+"\n")

    driver.find_element_by_xpath('//*[@id="example"]/tbody/tr[' + str(village) + ']/td[4]').click()

    print("Loding Entries one by one...")

    running = True

    def find_the_link(i):
        try:
            a_link = driver.find_element_by_xpath('//*[@id="example"]/tbody/tr['+ str(i) +']/td[8]/a').click()
        except:
            find_the_link(i=i+1)

    while running:
        #print(driver.find_element_by_xpath('//*[@id="example"]/tbody/tr[1]/td[8]/a'))
        #'//*[@id="example"]/tbody/tr[6]/td[8]'
        #all_links = driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/form/div[1]/div')
        #for link in all_links:
            #link.get_attribute('href').click()
            #time.sleep(25)
        find_the_link(i=1)

        keyboard = input('Entry Values: Enter T for True / F for False')

        if(keyboard == "T" or keyboard == "t"):
            driver.find_element_by_id('_changeStatus6').click()
        elif(keyboard == "F" or keyboard == "f"):
            driver.find_element_by_id('_changeStatus2').click()
        else:
            keyboard = input('Entry Values: Enter T for True / F for False')
            if (keyboard == "T" or keyboard == "t"):
                driver.find_element_by_id('_changeStatus6').click()
            elif (keyboard == "F" or keyboard == "f"):
                driver.find_element_by_id('_changeStatus2').click()

        driver.find_element_by_id('submit').click()
        time.sleep(2)
        alert = driver.switch_to.alert.accept()

        loop_iter += 1
        print("successfully entered entry No. : " + str(loop_iter) + " \n")

except:
    print("Successfully entered entries:" + str(loop_iter) + "\n")
    print("Logging out from website")
    driver.get("http://livestockcensus.gov.in/logout.action")
    print("Closing Browser.....\n")
    driver.close()
    print("Thank you for using SelBot -- Dev.Jeel \n For more Contact Dev.")
