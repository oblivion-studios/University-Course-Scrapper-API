# Import Libraries 
from itertools import groupby
from itertools import zip_longest
import json
import os

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
# Built using JSON Libraries, and Python2 Language
# ----------------------------------------------------
# Total Time For Script To Run => >1 minute
# ----------------------------------------------------
# Author: Sirak Berhane
# Created On: 11/19/2018
# ----------------------------------------------------
# Used for creating JSON API for
# UNIVERSITY TIMETABLE GENERATOR API
# ----------------------------------------------------
#  Maps data from [course]temp.txt file to 
#  [course].json file then deletes any temp files.
# ----------------------------------------------------
# ----------------------------------------------------

# Course Code
static_course_code = ["ACCT", "AFRI", "ANTH", "ALDS", "ARCT", "ARCS",
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

# JSON data attributes 
data_attributes = ["Status", "CRN", "Course Number", "Section", 
                    "Title", "Credits", "Type", "Restrictions", "Prerequistes", "Instructor Name", "Meeting Date", "Also Register In", "Other"]

course = []

# Map data_attributes to [course]temp.txt file and store result to [course].json
for x in range(0, len(static_course_code)):
    with open("data/Graduate/Winter2020/JSON/"+static_course_code[x]+"temp.txt") as f, open("data/Graduate/Winter2020/JSON/"+static_course_code[x]+".json","w") as out:
        grouped = groupby(map(str.rstrip,f), key=lambda x: x.startswith("|-"))
        for k,v in grouped:
            if not k:
                course.append(dict(zip_longest(data_attributes,v, fillvalue='none')).copy())
        json.dump(course, out, indent=4)
        out.write("\n")
        course = []

# Clean up --> [DELETE] temp files and raw data
for y in range(0,len(static_course_code)):
    os.remove("data/Graduate/Winter2020/JSON/"+static_course_code[y]+"temp.txt")
    os.remove("data/Graduate/Winter2020/JSON/"+static_course_code[y]+".txt")