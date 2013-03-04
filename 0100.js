var INSTRUCTION_FORMAT = "B"

var ASM_NAME = "jumpBackOrInit"

function commandExec(param) {
    if (param[0] == 0) {
        emu.storeReg(3, 95);
        emu.incrementProgramCounter(1);
    } else if (param[0] == 1) {
        emu.setProgramCounter(22);
    } else if (param[0] == 2) {
        emu.setProgramCounter(emu.loadReg(0));
    }
}
        