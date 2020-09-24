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
static_course_code = ["AERO", "AFRI", "ASLA", "ANTH", "ALDS", "ARAB", "ARCS",
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
                            "NET", "NEUR", "PHIL", "PHYS", "PSCI", "PORT", "PSYC",
                            "PADM", "PAPM", "RELI", "RUSS", "SXST", "SOWK", "SOCI","SPAN",
                            "STAT", "SREE", "SYSC", "TSES", "WGST"]
semesterCode = "202030"

# JSON data attributes 
data_attributes = ["Status", "CRN", "Course Number", "Section", 
                    "Title", "Credits", "Type", "Restrictions", "Prerequistes", "Instructor Name", "Meeting Date", "Also Register In", "Other"]

course = []

# Map data_attributes to [course]temp.txt file and store result to [course].json
for x in range(0, len(static_course_code)):
    with open("data/Undergraduate/_" + semesterCode + "/JSON/" + static_course_code[x] + "temp.txt") as f, open("data/Undergraduate/_" + semesterCode + "/JSON/" + static_course_code[x] + ".json","w") as out:
        grouped = groupby(map(str.rstrip,f), key=lambda x: x.startswith("|-"))
        for k,v in grouped:
            if not k:
                course.append(dict(zip_longest(data_attributes,v, fillvalue='none')).copy())
        json.dump(course, out, indent=4)
        out.write("\n")
        course = []

# Clean up --> [DELETE] temp files and raw data
for y in range(0,len(static_course_code)):
    os.remove("data/Undergraduate/_" + semesterCode + "/JSON/" +  static_course_code[y] + "temp.txt")
    os.remove("data/Undergraduate/_" + semesterCode + "/JSON/" + static_course_code[y] + ".txt")
