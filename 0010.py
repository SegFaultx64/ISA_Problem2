INSTRUCTION_FORMAT = "B"

ASM_NAME = "init"

def commandExec(param):
    emu.storeReg(4, emu.loadWord(9))
    emu.incrementProgramCounter(1)
