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

    print("Logging in ==> with username and password..\n")

    # Username and Keys
    user_id_box = driver.find_element_by_id('userid')
    user_id_box.send_keys('')

    # Find password box
    pass_box = driver.find_element_by_id('password')
    # Send password
    pass_box.send_keys('')

    # Find login button
    driver.find_element_by_id('Submit').click()

    print("Loading Village List....\n")

    driver.get('http://livestockcensus.gov.in/schedule/scheduleDetailsVillageWise.action')

    # Village number
    village = input("Input Village No:")
    print("Loading Village No. ==> " + str(village)+"\n")

    # Click on Respective link to that village
    driver.find_element_by_xpath('//*[@id="example"]/tbody/tr[' + str(village) + ']/td[4]').click()

    print("Loading Entries one by one...")

    running = True

    def alert_check():
        try:
            alert = driver.switch_to.alert.accept()
        except:
            time.sleep(1)
            alert_check()

    # This Function is to find first Draft Entry Link
    def find_the_link(i):
        try:
            a_link = driver.find_element_by_xpath('//*[@id="example"]/tbody/tr[' + str(i) + ']/td[8]/a').click()
        except Exception:
            find_the_link(i=i+1)

    def find_the_data_class(j):
        try:
            driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div/form/div[1]/div/a[' + str(j) + ']').click()
        except Exception:
            if j >= 0:
                find_the_data_class(j=j-1)

    # Infinite Loop That runs for Every entry
    while running:
        find_the_link(i=1)

        # inside tabareadata find the href text
        find_the_data_class(j=4)

        selected_link_text = driver.find_element_by_class_name('orange-d').text

        if selected_link_text == "Personal Details":
            print("No Data Found ==> Automatic Submitting entry\n")
            driver.find_element_by_id('_changeStatus6').click()

        # Only ask for t/f if entry finds livestock, poultry data
        if selected_link_text != "Personal Details":
            keyboard = input('Entry Values: Enter T for True / F for False  ')
            if keyboard == "T" or keyboard == "t":
                driver.find_element_by_id('_changeStatus6').click()
            elif keyboard == "F" or keyboard == "f":
                driver.find_element_by_id('_changeStatus2').click()
            else:
                keyboard = input('Entry Values: Enter T for True / F for False')
                if keyboard == "T" or keyboard == "t":
                    driver.find_element_by_id('_changeStatus6').click()
                elif keyboard == "F" or keyboard == "f":
                    driver.find_element_by_id('_changeStatus2').click()

        driver.find_element_by_id('submit').click()
        time.sleep(1.0)
        alert_check()
        loop_iter += 1
        print("successfully entered entry No. : " + str(loop_iter) + " \n")

except Exception as e:
    print(e)
    print("-"*40)
    print("Successfully entered entries:" + str(loop_iter) + "\n")
    print("Logging out from website")
    driver.get("http://livestockcensus.gov.in/logout.action")
    print("Closing Browser.....\n")
    driver.close()
    print("Thank you for using SelBot -- Developer Jeel \n For more Contact Dev.")
