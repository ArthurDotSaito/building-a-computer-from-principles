import re

class HackAssemblerParser():
    DEST_DELIMITER = '='
    JUMP_DELIMITER = ';'

    def __init__(self, input_file):
        self.input_file = open(input_file, 'r')
        self.current_command = None
        self.next_line = None
        self.has_more_lines_to_parse = True

    def reset(self):
        self.input_file.seek(0)
        self.current_command = None
        self.next_line = None
        self.has_more_lines_to_parse = True

    def dest_mnemonic(self):
        if self.current_command.find(self.DEST_DELIMITER) != -1:
            return self.current_command.split(self.DEST_DELIMITER)[0]

    def comp_mnemonic(self):
        if self.current_command.find(self.DEST_DELIMITER) != -1:
            return self.current_command.split(self.DEST_DELIMITER)[1]
        elif self.current_command.find(self.JUMP_DELIMITER) != -1:
            return self.current_command.split(self.JUMP_DELIMITER)[0]

    def jump_mnemonic(self):
        if self.current_command.find(self.JUMP_DELIMITER) != -1:
            return self.current_command.split(self.JUMP_DELIMITER)[1]

    def symbol(self):
        return ''.join(c for c in self.current_command if c not in '()@/')

    def advance(self):
        if self.current_command is None:
            self.current_command = self.input_file.readline()
        else:
            self.current_command = self.next_line

        self.current_command = self._cleaned_line(self.current_command)

        self.next_line = self.input_file.readline()
        if self.next_line == '':
            self.has_more_lines_to_parse = False

        self._find_current_command_type()

    def _cleaned_line(self, line):
        line = line.strip()
        line = line.split('//')[0]
        line = line.strip(' ')
        return line

    def _find_current_command_type(self):
        if self.current_command == '':
            self.current_command_type = 'not_instruction'
        elif self.current_command[0] == '@':
            self.current_command_type = 'address'
        elif self.current_command[0] == '(':
            self.current_command_type = 'label'
        else:
            self.current_command_type = 'computation'
