import re
from Decoder import HackAssemblerDecoder
from Parser import HackAssemblerParser
from SymbolTable import SymbolTable

class HackAssembler():
    def __init__(self, input_file):
        self.parser = HackAssemblerParser(input_file)
        self.symbol_table = SymbolTable()

    def run(self):
        self.parse_for_labels()
        self.parser.reset()
        self.translate()

    # 1st pass
    def parse_for_labels(self):
        num_instructions_so_far = 0

        while self.parser.has_more_lines_to_parse:
            self.parser.advance()

            if self.parser.current_command_type == 'not_instruction':
                continue
            elif self.parser.current_command_type == 'label':
                self.symbol_table.add_entry(symbol=self.parser.symbol(), address=num_instructions_so_far)
            else:
                num_instructions_so_far += 1

    # 2nd pass
    def translate(self):
        hack_file_name = self.parser.input_file.name.split('.')[0] + '.hack'
        hack_file = open(hack_file_name, 'w+')

        char_only_matcher = re.compile('[a-zA-Z]+')

        while self.parser.has_more_lines_to_parse:
            self.parser.advance()
            machine_code = ''

            if self.parser.current_command_type == 'address':
                symbol = self.parser.symbol()
                not_number = char_only_matcher.match(symbol)

                if not_number:
                    if self.symbol_table.contains(symbol):
                        register_number = self.symbol_table.get_address(symbol)
                    else:
                        register_number = self.symbol_table.add_entry(symbol)
                else:
                    register_number = int(symbol)

                machine_code = HackAssemblerDecoder.decimal_to_binary_string(register_number)
            elif self.parser.current_command_type == 'computation':
                init_bits = HackAssemblerDecoder.C_COMMAND_INIT_BITS
                comp_mnemonic = self.parser.comp_mnemonic()
                comp_bits = HackAssemblerDecoder.COMP_MNEMONIC_TO_BITS[comp_mnemonic]
                dest_mnemonic = self.parser.dest_mnemonic()
                dest_bits = HackAssemblerDecoder.DEST_MNEMONIC_TO_BITS[dest_mnemonic]
                jump_mnemonic = self.parser.jump_mnemonic()
                jump_bits = HackAssemblerDecoder.JUMP_MNEMONIC_TO_BITS[jump_mnemonic]

                machine_code = init_bits + comp_bits + dest_bits + jump_bits

            if len(machine_code) > 0:
                hack_file.write(machine_code + '\n')

        hack_file.close()
