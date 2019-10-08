# University Course Scheduler
Top Level View (Scrapper --> REST API --> REACT Website)

## University Course Scrapper (Python)
Scraps all of the public courses into a text files and then converts it into a JSON file.

## University Course Scheduler (Node JS, REST API)
University Course Scheduler (REST API) used by the react website to build timetable.

### API Build Version
```API Version 1.0.0```

### How to use University Course Scheduler API?
* Must have python-3 installed with beautifulsooup4 and selenium webdriver (Chrome Browser) installed as dependencies.
* Let the requestsOutputScrapper.py run first (takes the longest to run). UI is disabled for the selenium driver and only runs as headless browser.
* Run the AdvancedStringParser.java file to remove any white spaces and weird symbols that it might have been scrapped. This is in java which will later be converted into python.
* Finally to convert the text file to JSON you need to run the TextToJSONConversion.py which will map line by line to a JSON param.

### What is this API use this for?
* This going to be used for a website that will show public schedule for various canadian universities in an organzied way instead of visting the particular university course website each time. Users will be able to make timetable schedules easily, provide recomended time to start classes, view and compare schedules with other users, and integrate Google Calendar/Outlook for an easy sync.

### What is newer versions going to look like?
* The end goal for this scrapper is to be deployed as a micro-service, that is able to have cron jobs each semester, and convert public courses into JSON data automatically without any manual input.

#### Express Routes Definitions
The following defines all of the current routes avaliable with this API:

1) ``` \undergraduate ```  --> Gets the undergraduate courses.

2) ``` \graduate ```       --> Gets the graduate courses.

3) ``` \search ```         --> Uses Fuse.js to search through JSON object with given 'keyword search'

#### Request Queries 
1) {undergraduate} ``` semester, year, and course ``` --> semester = 'Fall, Winter, or Summer' || Year = Current or Next School Year || course = Course Code

2) {graduate} ``` semester, year, and course ``` --> semester = 'Fall, Winter, or Summer' || Year = Current or Next School Year || course = Course Code

3) {search} ``` keyword, semester, year, and course ``` -> keyword = Search keyword by Title, Course Number, or CRN || semester = 'Fall, Winter, or Summer' || Year = Current or Next School Year || course = Course Code

## University Course Website (Node JS, REACT)
REACT website that fetches data from the API endpoint and displays an interface to build and share timetables. 

# License

```

Copyright 2019 Oblivion Studios (DevTOS)

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
  
```
