from hack_assembler import HackAssembler

def main():
    asm_input_file = 'seu_programa.asm'  
    assembler = HackAssembler(asm_input_file)
    assembler.run()

if __name__ == "__main__":
    main()
