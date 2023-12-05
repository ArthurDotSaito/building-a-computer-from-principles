from hack_assembler import HackAssembler

def main():
    asm_input_file = '../pong/Pong.asm'  #Change here the file to be assembled
    assembler = HackAssembler(asm_input_file)
    assembler.run()

if __name__ == "__main__":
    main()
