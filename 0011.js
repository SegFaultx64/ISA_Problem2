var INSTRUCTION_FORMAT = "A"

var ASM_NAME = "Compare1"

function zeroFill( number, width )
{
  width -= number.toString().length;
  if ( width > 0 )
  {
    return new Array( width + (/\./.test( number ) ? 2 : 1) ).join( '0' ) + number;
  }
  return number + ""; // always return a string
}

function commandExec(param) {
    var curOffset = emu.loadReg(3);
    var curWord = emu.loadWord(96 + curOffset);
    emu.storeReg(5, curWord)
    var reg4 = emu.loadReg(4);
    var reg5 = emu.loadReg(5);
    var binaryQuery = reg4.toString(2)
    binaryQuery = zeroFill(binaryQuery, 16)
    var binaryCurWord = reg5.toString(2)
    binaryCurWord = zeroFill(binaryCurWord, 16)
    emu.log("reg4: " + reg4);
    emu.log("reg5: " + reg5);
    emu.log("binaryQuery: " + binaryQuery);
    emu.log("binaryCurWord: " + binaryCurWord);
    if (emu.loadReg(4) === emu.loadReg(5)) {
    	emu.setProgramCounter(10);
    } else if (binaryQuery.slice(0, 8) === binaryCurWord.slice(8, 16)) {
    	emu.setProgramCounter(5);
    }
    emu.incrementProgramCounter(1);
}