# Import Libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from datetime import datetime
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
# TIMETABLE GENERATOR API
# ----------------------------------------------------
# Creates 1 empty .JSON and 1 .txt file containing
# raw html data from Carleton Central.
# ----------------------------------------------------
# ----------------------------------------------------

# Course Code for Undergraduate Level
static_course_code_fall = [ "AERO", "AFRI", "ASLA", "ANTH", "ALDS", "ARAB", "ARCY","ARCS",
                            "ARCC", "ARCN", "ARCH", "ARCU", "ARTH", "BIOC", "BIOL",
                            "BUSI", "CDNS", "CHEM", "CHST", "CHIN", "CIVE", "CLCV",
                            "COOP", "CGSC", "CCDP", "COMS", "COMP", "CRCJ", "DIGH",
                            "DBST", "ESPW", "ERTH", "ECON", "ELEC", "ECOR", "ENGL",
                            "ESLA", "ENVE", "ENSC", "ENST", "EURR", "FILM", "FYSM",
                            "FOOD", "FREN", "FINS", "GEOG", "GEOM", "GERM", "GPOL", "GINS",
                            "GREK", "HLTH", "HIST", "HUMR", "HUMS", "INDG", "IDES", "IRM",
                            "BIT", "ITEC", "IMD", "ISAP", "IPAF", "ISCI", "INAF", "ITAL",
                            "JAPA", "JOUR", "KORE", "LATN", "LACS", "LAWS", "LING",
                            "MATH", "MECH", "MAAE", "MPAD", "MEMS", "MGDS", "MUSI", "NSCI",
                            "NET", "NEUR", "OSS", "PHIL", "PHYS", "PSCI", "PORT", "PSYC",
                            "PADM", "PAPM", "RELI", "RUSS", "SXST", "SOWK", "SOCI","SPAN",
                            "STAT", "SREE", "SYSC", "TSES", "WGST"]     # "INSC", "PLT" , "SAST" - Removed 9/23/2020

static_course_code_winter = ["AERO", "AFRI", "ASLA", "ANTH", "ALDS", "ARAB", "ARCS",
                            "ARCC", "ARCN", "ARCH", "ARCU", "ARTH", "BIOC", "BIOL",
                            "BUSI", "CDNS", "CIED", "CHEM", "CHST", "CHIN", "CIVE", "CLCV",
                            "COOP", "CGSC", "CCDP", "COMS", "COMP", "CRCJ", "DIGH",
                            "DBST", "ESPW", "ERTH", "ECON", "ELEC", "ECOR", "ENGL",
                            "ESLA", "ENVE", "ENSC", "ENST", "EURR", "FILM", "FYSM",
                            "FOOD", "FREN", "FINS", "GEOG", "GEOM", "GERM", "GPOL", "GINS",
                            "GREK", "HLTH", "HIST", "HUMR", "HUMS", "INDG", "IDES", "IRM",
                            "BIT", "ITEC", "INSC", "IMD", "ISAP", "IPAF", "ISCI", "INAF", "ITAL",
                            "JAPA", "JOUR", "KORE", "LATN", "LACS", "LAWS", "LING",
                            "MATH", "MECH", "MAAE", "MPAD", "MEMS", "MUSI",
                            "NET", "NEUR", "PHIL", "PLT", "PHYS", "POLM", "PSCI", "PORT", "PSYC",
                            "PADM", "PAPM", "RELI", "RUSS", "SXST", "SOWK", "SOCI", "SPAN",
                            "STAT", "SREE", "SYSC", "TSES", "WGST"]                      

# Removed following courses due to empty result: "ARCN","GERM", "INDG", "IDES", "INSC", "ITIS", "ITEC", "IPIS"
static_course_code_summer = ["AFRI", "ASLA", "ANTH", "ALDS", "ARCC", "ARCH", "ARTH", "BIOC", "BIOL", "BUSI", "CDNS", "CHEM", "CHST", "CIVE", "CLCV", "CGSC", "CCDP", "COMS", "COMP", "CRCJ", "DIGH", "ERTH", "ECON", "ELEC", "ECOR", "ENGL", "ESLA", "ENVE", "ENSC", "ENST", "EURR", "FILM", "FOOD", "FREN",
                             "GEOG", "GEOM", "GPOL", "GINS", "HLTH", "HIST", "HUMR", "HUMS", "BIT", "IPAF", "ITAL", "JAPA", "KORE", "LANG", "LAWS", "LING", "MATH", "MAAE", "MUSI", "NET", "NEUR", "PHIL", "PLT", "PHYS", "PSCI", "PSYC", "PAPM", "RELI", "SOWK", "SOCI", "SPAN", "STAT", "SYSC", "TSES", "WGST"]

# Course Code for Graduate Level
static_course_code_grad_fall = ["ACCT", "AFRI", "ANTH", "ALDS", "ARCT", "ARCS",
                                "ARCC", "ARCN", "ARCH", "ARTH", "BIOL", "BIOM",
                                "BUSI", "CDNS", "CHEM", "CIVE", "CIVJ", "CGSC",
                                "COMS", "COMP", "CLMD", "CURA", "DIGH",
                                "ERTH", "ECON", "EACJ", "ELEC", "ENGL", "ENVJ",
                                "ENVE", "EPAF", "EURR", "FILM", "FINA",
                                "FOOD", "FREN", "GEOG", "HLTH", "HIST", "HCIN", "IDES", "ITIS",
                                "ITEC", "IPIS", "INAF", "IBUS", "IDMG", "JOUR", "LAWS", "MGMT",
                                "MATH", "MAAJ", "MECH", "MUSI", "NEUR", "NRTH", "PANL", "PHIL",
                                "PHYS", "PHYJ", "PECO", "POLM", "PSCI", "PSYC",
                                "PADM", "RELI", "SOWK", "SOCI", "STAT", "STGY",
                                "SERG", "SYSC", "TIMG", "TOMS", "WGST"]

static_course_code_grad_winter = ["ACCT", "AFRI", "ANTH", "ALDS", "ARCT", "ARCS",
                                "ARCC", "ARCN", "ARCH", "ARTH", "BIOL", "BIOM",
                                "BUSI", "CDNS", "CHEM", "CIVE", "CIVJ", "CGSC",
                                "COMS", "COMP", "CLMD", "CURA", "DATA", "DIGH",
                                "ERTH", "ECON", "EACJ", "ELEC", "ENGL", "ENVJ",
                                "ENVE", "EPAF", "EURR", "FILM", "FINA",
                                "FOOD", "FREN", "GEOG", "HLTH", "HIST", "HCIN", "IDES", "ITIS",
                                "ITEC", "IPIS", "INAF", "IBUS", "JOUR", "LAWS", "MGMT", "MKTG",
                                "MATH", "MAAJ", "MECH", "MUSI", "NEUR", "NRTH", "PANL", "PHIL",
                                "PHYS", "PHYJ", "PECO", "POLM", "PSCI", "PSYC",
                                "PADM", "RELI", "SOWK", "SOCI", "STAT", "STGY",
                                "SERG", "SYSC", "TIMG", "TOMS", "WGST"]

static_course_code_grad_summer = ["ACCT", "AFRI", "ANTH", "ALDS", "ARCT", "ARCS",
                                "ARCC", "ARCN", "ARCH", "ARTH", "BIOL", "BIOM",
                                "BUSI", "CDNS", "CHEM", "CIVE", "CIVJ", "CGSC",
                                "COMS", "COMP", "CLMD", "CURA", "DATA", "DIGH",
                                "ERTH", "ECON", "ELEC", "ENGL", "ENVJ",
                                "ENVE", "EPAF", "EURR", "FILM", "FINA",
                                "FOOD", "FREN", "GEOG", "HLTH", "HIST", "HCIN", "IDES", "ITIS",
                                "ITEC", "IPIS", "INAF", "IBUS", "JOUR", "LAWS", "MGMT",
                                "MATH", "MAAJ", "MECH", "MUSI", "NEUR", "NRTH", "PANL", "PHIL",
                                "PHYS", "PECO", "POLM", "PSCI", "PSYC",
                                "PADM", "RELI", "SOWK", "SOCI", "STAT", "STGY",
                                "SERG", "SYSC", "TIMG", "TOMS", "WGST"]

# Specify the URL and Set up the chromedriver settings
start_time = time.time()

dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print("\n ~ Started scraping at [ " + dt_string + " ] ~ \n")

course_search = "https://central.carleton.ca"

# Headless Run Mode
options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe', options=options)

# Non-Headless Run Mode
#browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')

# Note: When the website is created there should be course status updater
# Site: https://central.carleton.ca/prod/bwysched.p_display_course?wsea_code=EXT&term_code=202010&disp=11050565&crn=10012
# Note: CRN and the term_code changes
# YEAR: 2020 --> Followed by: (10) -> Winter, (20) -> Summer, (30) -> Fall
# COURSE STATUS SELECTOR: $('.contentareafull > table > tbody > tr:nth-child(11) > td:nth-child(2)').innerText

# Get the URL
browser.get(course_search)
print("\nGET URL: " + course_search)

# Select the Timetable URL
URL = "http://central.carleton.ca/prod/bwysched.p_select_term?wsea_code=EXT"
browser.get(URL)
print("GET URL: http://central.carleton.ca/prod/bwysched.p_select_term?wsea_code=EXT")

# Find course schedule
valueOfSemester = '202030' # CODE: 202110 for Winter 2021
selectable = Select(browser.find_element_by_id('term_code'))
selectable.select_by_value(valueOfSemester)
print("\nSELECTING")

# Wait for page to load
time.sleep(2)

# Click search
browser.find_element_by_xpath("//input[@value='Proceed to Search']").click()
print("CLICK Search")

# Wait for page to load
time.sleep(6)

# Database to Hold CRN, Course Code + Number + Section, Lab/Tutorial Section, Date, Building, Room
# WEBSITE -> {Database to JSON} -> ANDROID STUDIO PORT -> ANDROID DEVICE Timetable Application
# Return only CRN, Course Code + Number + Section, Lab/Tutorial Section, Date, Building, Room in for loop
for x in range(0, len(static_course_code_fall)):
    # Choose Undergraduate Level
    browser.find_element_by_xpath("//option[@value='UG']").click() # UG -> Undergraduate || GR -> Graduate
    print("SELECT Course Level")
    time.sleep(2)

    # De-Select 'All Subjects'
    browser.find_element_by_xpath("//select[@id='subj_id']/option[1]").click()
    time.sleep(2)

    # Select the Course Code from 0 to 102
    if x > 0:
        Select(browser.find_element_by_xpath("//select[@id='subj_id']")).deselect_all()
    
    Select(browser.find_element_by_xpath("//select[@id='subj_id']")).select_by_value(str(static_course_code_fall[x]))
    print("SELECT COURSE CODE: " + static_course_code_fall[x])

    # Click search with the above course parameters
    browser.find_element_by_xpath("//input[@value='Search']").click()
    print("Clicked Search")

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
                with open("data/Undergraduate/_" + valueOfSemester + "/JSON/" + static_course_code_fall[x] + ".txt", "a") as fileOutput:
                   fileOutput.write(str(container.text.encode("ascii", errors="ignore").decode()))

            # Output all rows of course data with the color of #DCDCDC
             # Each line is data to be converted into JSON
            if 'bgcolor' in container.attrs and container.attrs['bgcolor'] == '#DCDCDC':
                with open("data/Undergraduate/_" + valueOfSemester + "/JSON/" + static_course_code_fall[x] + ".txt", "a") as fileOutput:
                    fileOutput.write(str(container.text.encode("ascii", errors="ignore").decode()))
        except AttributeError:
            continue

    # Create empty JSON files --> Used later when converting the raw text files to JSON
    # Eventually the JSON files will be converted to be a SQLite database
    # {DATA} --> (Fetch and Downloaded by Android Device) from AWS or Firebase Services.
    with open("data/Undergraduate/_" + valueOfSemester +"/JSON/" + static_course_code_fall[x] + ".json", "a") as writeJSON:
        json.dump(courseInfoData, writeJSON, ensure_ascii=False)

    # Notify console output
    print("DONE SAVING TO JSON FILE --> COURSE CODE [" + static_course_code_fall[x] + "]\n")

    # Return to Course Select
    browser.find_element_by_xpath("//input[@name='search_selected']").click()

    # Wait for web to load (5 Seconds to be safe with Carleton web load time + internet speeds)
    time.sleep(5)

temp = (time.time() - start_time)
hours = temp//3600
temp = temp - 3600*hours
minutes = temp//60
seconds = temp - 60*minutes
print("\n--- Shutting down Selenium Browser. Completed in: %d:%d:%d ---\n" %(hours,minutes,seconds))

# Close Selenium Browser
browser.quit()
