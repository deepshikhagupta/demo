This application parses the data provided in given csv files and print the result of formatted output on console.
It also contains test scenarios which test this application.
The directory structure is as follows:
# demo
 * app
    * \_\_init\_\_.py
   * [parser.py](./app/parser.py)
 
 * tests
   * \_\_init\_\_.py
   * test_data.py
 * files
   * 1.csv
   * 2.csv
   * 3.csv
 * README.md

**files** folder contains csv files which need to be parsed, **app** contains the python code for parsing the csv files and **tests** contains scenarios which are tested aginst the code

To run this application, please clone the following github-repository:
https://github.com/deepshikhagupta/demo

cd demo

Add the directory to your PYTHONPATH

* For application execution, run:
    * python app/tests.py
* For tests, run:
    * python tests/test_data.py
