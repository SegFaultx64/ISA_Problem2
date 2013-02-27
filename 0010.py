INSTRUCTION_FORMAT = "A"

ASM_NAME = "LoadQuery"

def commandExec(param):
    emu.setRegister(4, emu.loadWord(9))
    emu.incrementProgramCounter(1)
