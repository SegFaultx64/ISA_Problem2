INSTRUCTION_FORMAT = "B"

ASM_NAME = "IncrementProgramCounter"

def commandExec(param):
    emu.incrementProgramCounter(-param[0])