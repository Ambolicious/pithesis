import csv
import datetime

class CSVLogger:

    def __init__(self, file_name='../pithesis_log.csv'):
        self.__file_name = file_name

    def write_to_csv(self, data):
        with open(self.__file_name, 'a') as f: 
            ct = datetime.datetime.now()
            ts = ct.timestamp()
            write = csv.writer(f) 
            write.writerow([ct, ts]+data)
