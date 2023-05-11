from sklearn.model_selection import train_test_split
import pandas as pd
import PyIO
import PyPluMA

# Define plugin class
class DataSplitPlugin:

    # Define input function
    def input(self, filename):
        self.parameters = PyIO.readParameters(filename)
        # Read in input data as a pandas DataFrame
        self.data = pd.read_csv(PyPluMA.prefix()+"/"+self.parameters["csvfile"], index_col=0)
        self.train = PyPluMA.prefix()+"/"+self.parameters["train"]
        self.test = PyPluMA.prefix()+"/"+self.parameters["test"]
        self.trainsize = int(self.parameters["trainsize"])
        self.testsize = int(self.parameters["testsize"])

    # Define run function
    def run(self):
        # Split data into train and test sets
        self.train_data, self.test_data = train_test_split(self.data, train_size=self.trainsize, test_size=self.testsize, random_state=42)

    # Define output function for train data
    def output(self, filename):
        # Write train data to output file
        self.train_data.to_csv(filename)

    # Define output function for test data
    # Define output function
    def output(self, filename, data_type=None):
        if data_type == "train":
            self.train_data.to_csv(filename)
        elif data_type == "test":
            self.test_data.to_csv(filename)
        elif data_type is None:
            self.train_data.to_csv(self.train)
            self.test_data.to_csv(self.test)
        else:
            raise ValueError("Invalid data type. Must be either 'train' or 'test'.")


    

