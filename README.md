# DataSplit
# Language: Python
# Input: TXT
# Output: DIR
# Tested with: PluMA 1.1, Python 3.6
# Dependency: pandas==1.1.5

PluMA plugin that splits input data into a training and test set

The inputfile is a set of tab-delimited keyword value pairs:

csvfile: Input dataset
train: Training data filename
test: Test data filename
trainsize: Number of train samples
testsize: Number of test samples

Outputs train and test will be placed in the user-specified output directory

