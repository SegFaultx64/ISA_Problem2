INSTRUCTION_FORMAT = "B"

ASM_NAME = "loadQuery"

def commandExec(param):
    emu.storeReg(4, emu.loadWord(param[0]))
    emu.incrementProgramCounter(1)
