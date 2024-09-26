import argparse

class CommandLine():

    def __init__(self, inputs=None) -> None:
        self.parser = argparse.ArgumentParser(description='Command Line Usage')

        self.parser.add_argument('-f', '--file', type = str, help = '.pdb file')
        self.parser.add_argument('-d', '--directory', type = str, help = 'directory containing .pdb files')

        if inputs is None:
            self.args = self.parser.parse_args()
        else:
            self.args = self.parser.parse_args(inputs)
