import csv
import json
import pickle
import sys
from abc import ABC, abstractmethod

class FileHandler(ABC):
    def __init__(self, input_file_path, output_file_path, transformations):
        self.input_file = input_file_path
        self.output_file = output_file_path
        self.transformations = transformations
        self.data = None

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    def do_transformations(self):
        for transformation in self.transformations:
            x, y, value = transformation.split(",")
            x = int(x)
            y = int(y)
            self.data[y][x] = value

class CSVFileHandler(FileHandler):
    def load_data(self):
        with open(self.input_file, newline='') as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                data.append(row)
            return data

    def save_data(self):
        with open(self.output_file, "w", newline='') as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

class JSONFileHandler(FileHandler):
    def load_data(self):
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def save_data(self):
        with open(self.output_file, 'w') as file:
            json.dump(self.data, file, indent=4)

class TxtFileHandler(FileHandler):
    def load_data(self):
        with open(self.input_file, 'r') as file:
            data = []
            for line in file:
                data.append(line.strip().split(','))
            return data

    def save_data(self):
        with open(self.output_file, 'w') as file:
            for row in self.data:
                file.write(','.join(row) + '\n')

class PickleFileHandler(FileHandler):
    def load_data(self):
        with open(self.input_file, 'rb') as file:
            return pickle.load(file)

    def save_data(self):
        with open(self.output_file, 'wb') as file:
            pickle.dump(self.data, file)

arguments = sys.argv[1:]
input_file = arguments[0]
output_file = arguments[1]
transformations = arguments[2:]

if input_file.endswith(".csv"):
    input_file_handler = CSVFileHandler(input_file, output_file, transformations)
elif input_file.endswith(".json"):
    input_file_handler = JSONFileHandler(input_file, output_file, transformations)
elif input_file.endswith(".txt"):
    input_file_handler = TxtFileHandler(input_file, output_file, transformations)
elif input_file.endswith(".pkl"):
    input_file_handler = PickleFileHandler(input_file, output_file, transformations)
else:
    raise ValueError("Unsupported input file format")

if output_file.endswith(".csv"):
    output_file_handler = CSVFileHandler(input_file, output_file, transformations)
elif output_file.endswith(".json"):
    output_file_handler = JSONFileHandler(input_file, output_file, transformations)
elif output_file.endswith(".txt"):
    output_file_handler = TxtFileHandler(input_file, output_file, transformations)
elif output_file.endswith(".pkl"):
    output_file_handler = PickleFileHandler(input_file, output_file, transformations)
else:
    raise ValueError("Unsupported output file format")

input_file_handler.data = input_file_handler.load_data()
input_file_handler.do_transformations()

output_file_handler.data = input_file_handler.data
output_file_handler.save_data()

for row in output_file_handler.data:
    print(",".join(map(str, row)))
