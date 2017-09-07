import csv
from collections import OrderedDict
import json
import glob

days = ['mon','tue','wed','thu','fri']
output = []
final_output = []

class Parser(object):

    def read_csv(self, file_name):
        """
        Read csv file.
        """
        try:
            file_obj = open(file_name)
            reader = csv.DictReader(file_obj)
        except:
            raise IOError
        return file_obj, reader

    def find_operation(self, day_name):
        """
        Finding out whether to Square or Double the value
        based on day.
        for mon,tue,wed : square the value
        for thu, fri: double the value
        """
        if day_name == 'mon' or day_name == 'tue' or day_name == 'wed':
            operation = 'square'
        elif day_name == 'thu' or day_name == 'fri':
            operation = 'double'
        else:
            raise ValueError
        return operation

    def parse_single_day_data(self,desc_value,key,val):
        """
        Preparing an ordered dictionary of key:value pairs
        based on single day and value provided for the specific file.
        For eg: for Monday, if value is 3 and file is 2.csv:

        {"day": "mon", "description": "second_desc 9", "square": "9", "value": "3"}
        """
        sample_dict=OrderedDict()
        sample_dict['day'] = key
        operation = self.find_operation(key)
        if operation == 'square':
            value = int(val)**2
            sample_dict['description'] = desc_value+" "+str(value)
        if operation == 'double':
            value = int(val)*2
            sample_dict['description'] = desc_value+" "+str(value)
        sample_dict[operation] = str(value)
        sample_dict['value'] = val

        return sample_dict


    def parse_csv(self, csv_reader):
        """
        Parsing one complete file into desired format for all days (mon-fri).
        """
        for line in csv_reader:
            desc_value = line['description']
            for key,val in line.iteritems():
                split_key = key.split('-')
                if ((len(split_key) == 1) and (key in days)):
                    sample_dict = self.parse_single_day_data(desc_value,key,val)
                    output.append(sample_dict)
                elif (len(split_key) == 2):
                    start_index = days.index(split_key[0])
                    end_index = days.index(split_key[1])
                    number_of_days = range(start_index, end_index+1)
                    for day in number_of_days:
                        day_name = days[day]
                        sample_dict = self.parse_single_day_data(desc_value,day_name,val)
                        output.append(sample_dict)
                else:
                    pass
        return output

    def process_output(self, output):
        """
        Formatting output in the sequence of week days.
        """
        ordered_list = [None]*5
        for element in output:
            day_index = days.index(element['day'])
            ordered_list[day_index] = element
        return json.dumps(ordered_list)


if __name__ == "__main__":
    """
    Finding all files with csv extension and
    parsing data in the desired format and printing on console.
    """
    path_to_csv_files = "files/*.csv"
    files = glob.glob(path_to_csv_files)
    for file_name in files:
        print file_name.split("/")[-1]
        instance = Parser()
        file_object,reader = instance.read_csv(file_name)
        output = instance.parse_csv(reader)
        procesed_output = instance. process_output(output)
        file_object.close()
        print procesed_output
        print "\n"

