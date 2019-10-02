# Import Libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import json

# ----------------------------------------------------
# ----------------------------------------------------
# Automated Carleton University Timetable Web-Scrapper
# Saves Course information to text.
# ----------------------------------------------------
# Use AdvancedStringParser (Java) to remove newlines 
# and add "|-" in the next repeating string -->
# then Use TextToJSONParser (Python) to map the raw
# text data to a JSON file.
# ----------------------------------------------------
# Built using Selenium Webdriver Libraries,
# BeautifulSoup4 Libraries and Python2 Language
# ----------------------------------------------------
# Total Time For Script To Run => 20 ~ 30 minutes
# ----------------------------------------------------
# Author: Sirak Berhane
# Created On: 11/18/2018
# ----------------------------------------------------
# Used for creating JSON API for
# CARLETON UNIVERSITY TIMETABLE GENERATOR ANDROID APP
# ----------------------------------------------------
# Creates 1 empty .JSON and 1 .txt file containing 
# raw html data from Carleton Central.
# ----------------------------------------------------
# ----------------------------------------------------

# Course Code for Undergraduate Level
static_course_code = ['AERO', 'AFRI', 'ASLA', 'ANTH', 'ALDS', 'ARAB', 'ARCS', 
                      'ARCC', 'ARCN', 'ARCH', 'ARCU', 'ARTH', 'BIOC', 'BIOL',
                     'BUSI', 'CDNS', 'CHEM', 'CHST', 'CHIN', 'CIVE', 'CLCV',
                      'COOP', 'CGSC', 'CCDP', 'COMS', 'COMP', 'CRCJ', 'DIGH',
                        'DBST', 'ESPW', 'ERTH', 'ECON', 'ELEC', 'ECOR', 'ENGL',
                        'ESLA', 'ENVE', 'ENSC', 'ENST', 'EURR', 'FILM', 'FYSM',
                         'FOOD', 'FREN', 'FINS', 'GEOG', 'GEOM', 'GERM', 'GPOL', 'GINS',
                      'GREK', 'HLTH', 'HIST', 'HUMR', 'HUMS', 'INDG', 'IDES', 'IRM',
                       'BIT', 'ITEC', 'INSC', 'IMD', 'IPAF', 'ISCI', 'INAF', 'ITAL',
                        'JAPA', 'JOUR', 'KORE', 'LANG', 'LATN', 'LACS', 'LAWS', 'LING',
                         'MATH', 'MECH', 'MAAE', 'MPAD', 'MEMS', 'MGDS', 'MUSI', 'NSCI',
                          'NET', 'NEUR', 'PHIL', 'PLT', 'PHYS', 'PSCI', 'PORT', 'PSYC',
                           'PADM', 'PAPM', 'RELI', 'RUSS', 'SXST', 'SOWK', 'SOCI', 'SPAN',
                            'STAT', 'SREE', 'SYSC', 'TSES', 'WGST']

# Course Code for Gradute Level --> [WIP]

# Specify the URL and Set up the chromedriver settings
course_search = "https://central.carleton.ca"

# Headless Run Mode
options = Options()
options.headless = True
browser = webdriver.Chrome(
    executable_path='C:/chromedriver/chromedriver.exe', chrome_options=options)

# Non-Headless Run Mode
#browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')

# Get the URL
browser.get(course_search)
print ("\nGET URL: " + course_search)

# Select the Timetable URL
URL = "http://central.carleton.ca/prod/bwysched.p_select_term?wsea_code=EXT"
browser.get(URL)
print("GET URL: http://central.carleton.ca/prod/bwysched.p_select_term?wsea_code=EXT")

# Find the Fall 2018 course schedule
select_fall2018 = Select(browser.find_element_by_id('term_code'))
select_fall2018.select_by_value('201830')
print("\nSELECT FALL 2018")

# Wait for page to load
time.sleep(2)

# Click search for fall 2018
browser.find_element_by_xpath("//input[@value='Proceed to Search']").click()
print("CLICK Search")

# Wait for page to load
time.sleep(6)

# Database to Hold CRN, Course Code + Number + Section, Lab/Tutorial Section, Date, Building, Room
# WEBSITE -> {Database to JSON} -> ANDROID STUDIO PORT -> ANDROID DEVICE Timetable Application
# Return only CRN, Course Code + Number + Section, Lab/Tutorial Section, Date, Building, Room in for loop
for x in range(0, len(static_course_code)):
    # Choose Undergraduate Level
    browser.find_element_by_xpath("//option[@value='UG']").click()
    print("SELECT Undergraduate Course Level")
    time.sleep(2)

    # De-Select 'All Subjects'
    browser.find_element_by_xpath("//select[@id='subj_id']/option[1]").click()
    time.sleep(2)

    # Select the Course Code from 0 to 102
    browser.find_element_by_xpath(
        "//select[@id='subj_id']/option[@value='" + static_course_code[x] + "']").click()
    print("SELECT COURSE CODE: " + static_course_code[x] + "\n")

    # Click search with the above course parameters
    browser.find_element_by_xpath("//input[@value='Search']").click()
    print("CLICK Search\n")

    # GET the page information
    response = browser.page_source
    soup = BeautifulSoup(response, "lxml")

    # Important line in order to traverse all 
    # of the <tr> elements found in Carleton Central Course.
    containers = soup.findAll('tr')

    # JSON Parsed Data
    courseInfoData = []

    # Traverse each <tr> elements 
    # with only the following colour attributes
    for container in containers:
        try:
            # Output all rows of course data with the color of #C0C0C0
            # Each line is data to be converted into JSON
            if 'bgcolor' in container.attrs and container.attrs['bgcolor'] == '#C0C0C0':
                with open("./JSON/" + static_course_code[x] + ".txt", "a") as fileOutput:
                    fileOutput.write(container.text.encode('utf-8').strip())

            # Output all rows of course data with the color of #DCDCDC
             # Each line is data to be converted into JSON
            if 'bgcolor' in container.attrs and container.attrs['bgcolor'] == '#DCDCDC':
                with open("./JSON/" + static_course_code[x] + ".txt", "a") as fileOutput:
                    fileOutput.write(container.text.encode('utf-8').strip())
        except AttributeError:
            continue

    # Create empty JSON files --> Used later when converting the raw text files to JSON
    # Eventually the JSON files will be converted to be a SQLite database 
    # {DATA} --> (Fetch and Downloaded by Android Device) from AWS or Firebase Services.
    with open("./JSON/" + static_course_code[x] + ".json", "a") as writeJSON:
        json.dump(courseInfoData, writeJSON, ensure_ascii=False)

    # Notify console output
    print("DONE SAVING TO JSON FILE --> COURSE CODE [" + static_course_code[x] + "]")

    # Return to Course Select
    browser.find_element_by_xpath("//input[@name='search_selected']").click()

    # Wait for web to load (5 Seconds to be safe with Carleton web load time + internet speeds)
    time.sleep(5)

# Close Selenium Browser
browser.quit()