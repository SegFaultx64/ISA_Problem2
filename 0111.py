INSTRUCTION_FORMAT = "B"

ASM_NAME = "IncrementProgramCounter"

def commandExec(param):
    emu.incrementProgramCounter(0 - param[1])
