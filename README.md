# Carleton University Public Course Scrapper
Scraps all of the public courses into a text files and then converts it to JSON file.

### How to use the scrapper?
* Must have python-3 installed with beautifulsooup4 and selenium webdriver (Chrome Browser) installed as dependencies.
* Let the requestsOutputScrapper.py run first (takes the longest to run). UI is disabled for the selenium driver and only runs as headless (no need to see bunch of ui clicking and selecting dropboxes ii all runs in the background).
* Run the AdvancedStringParser.java file to remove any white spaces and weird symbols that it might have scrapped.
* Finally to convert the text file to JSON you need to run the TextToJSONConversion.py which will map line by line to a JSON param.

### License

```
  Copyright 2019 sirakberhane

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
