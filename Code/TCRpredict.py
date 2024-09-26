# from data_validation import Validate
import TCR_utils as uts
from TCR_commandLine import CommandLine
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

class SVMClassifier:
    def __init__(self, test_size=0.2, random_state=None, kernel='linear'):
        """
        Initialize the SVMClassifier with test size, random state, and kernel type.
        """
        self.test_size = test_size
        self.random_state = random_state
        self.kernel = kernel
        self.model = SVC(kernel=self.kernel, random_state=self.random_state)

    def load_data(self, dataframe):
        """
        Load data from a pandas DataFrame and separate features and target.
        """
        self.X = dataframe.drop('label', axis=1)
        self.y = dataframe['label']

    def split_data(self):
        """
        Split the data into training and testing sets.
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=self.test_size, random_state=self.random_state
        )

    def train(self):
        """
        Train the SVM model using the training data.
        """
        self.model.fit(self.X_train, self.y_train)

    def evaluate(self):
        """
        Evaluate the model on the testing set and print accuracy and classification report.
        """
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        report = classification_report(self.y_test, y_pred)
        print(f"Accuracy: {accuracy}")
        print("Classification Report:")
        print(report)

def main():
    cmd = CommandLine()
    
    if cmd.args.file:
        pass
        # parse the file to get selection 

        # run prodigy on file 

        # classify the output of prodigy and print to the console

    
    if cmd.args.directory:
        pass
        # parse each file in directory for selection

        # run prodigy on each file 

        # classify each maybe store in a cmd.args.filename



    


if __name__ == "__main__":
    main()
