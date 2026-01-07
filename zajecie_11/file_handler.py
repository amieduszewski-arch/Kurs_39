import csv

class FileHandler:
    def __init__(self, input_file_patch, output_file_patch, transformations):
        self.input_file_patch = input_file_patch
        self.output_file_patch = output_file_patch
        self.transformations = transformations
        self.data = self.load_data()

    def load_data(self):
        with open(self.input_file_patch) as file:
            reader = csv.reader(file, delimiter=',')
            temp_matrix = []
            for row in reader:
                temp_matrix.append(list(row))
        return temp_matrix

    def save_data(self):
        with open(self.output_file_patch, mode='w') as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

    def do_transformations(self):
        for transformation in self.transformations:
            transformation_list = transformation.split(',')

            x = int(transformation_list[0])
            y = int(transformation_list[1])
            value = transformation_list[2]

            self.data[y][x] = value