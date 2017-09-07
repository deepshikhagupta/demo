import unittest
from collections import OrderedDict
from app.parser import Parser
import csv
import json
import os

class CSVParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_find_operation_for_sqaure_field(self):
    	days = ['mon','tue','wed']
    	for day in days:
    		result = self.parser.find_operation(day)
        	self.assertEqual('square', result)

    def test_find_operation_for_double_field(self):
    	days = ['thu','fri']
    	for day in days:
    		result = self.parser.find_operation(day)
        	self.assertEqual('double', result)

    def test_find_operation_for_day_name_misspelled(self):
        self.assertRaises(ValueError, self.parser.find_operation,'abcd1234')

    def test_parse_single_day_data(self):
    	result = self.parser.parse_single_day_data('fifth_desc','thu','4')
    	expected_output = OrderedDict([('day', 'thu'), ('description', 'fifth_desc 8'), ('double', '8'), ('value', '4')])
    	self.assertEqual(expected_output,result)

    def test_csv_reader_for_existing_file_name(self):
    	file_name = "files/1.csv"
    	self.assertIsInstance(self.parser.read_csv(file_name),object)

    def test_csv_reader_for_non_existing_file_name(self):
    	file_name = "files/abc.csv"
    	self.assertRaises(IOError, self.parser.read_csv,'../files/abc.csv')

    def test_parse_csv_for_multiple_days_with_processed_output(self):
	    test_file = open('test.csv', 'w')
	    test_file.write('description,tue-wed,thu-fri,mon,some_columnnth\n')
	    test_file.write('nth_desc,12,1,2,data\n')
	    test_file.close()
	    file_obj,reader = self.parser.read_csv('test.csv')
	    parsed_data = self.parser.parse_csv(reader)
	    result = self.parser.process_output(parsed_data)
	    expected_output = [OrderedDict([('day', 'mon'), ('description', 'nth_desc 4'), ('square', '4'), ('value', '2')]),\
	                       OrderedDict([('day', 'tue'), ('description', 'nth_desc 144'), ('square', '144'), ('value', '12')]), \
	                       OrderedDict([('day', 'wed'), ('description', 'nth_desc 144'), ('square', '144'), ('value', '12')]),\
	                       OrderedDict([('day', 'thu'), ('description', 'nth_desc 2'), ('double', '2'), ('value', '1')]),\
	                       OrderedDict([('day', 'fri'), ('description', 'nth_desc 2'), ('double', '2'), ('value', '1')])]
	    os.remove('test.csv')
	    self.assertEqual(result,json.dumps(expected_output))

if __name__ == '__main__':
    unittest.main()
