# Pipelined CPU with Hazard Detection and Forwarding Unit

This multi-cycle/pipelined processor can perform basic arithmetic, logic and data operations. It is based on the ARM 64-bit architecture, with 32 registers each 64-bits wide with instruction lengths of 32-bits. 

**Basic assembly instructions:**
	1. LDUR
	2. STUR
	3. ADD
	4. SUB
	5. ORR
	6. AND
	7. CBZ
	8. B
	9. NOP
 are supported by the CPU, with `LDUR` and `STUR` supporting immediate values when performing certain operations to the registers module.

# Important to Note
The processor is pipelined allowing multiple instructions to run simultaneously. Buffers/caches are used in addition between each stage of the processor's operation to optimize the amount of time to run each instruction and protect against atomic reads in between register-base instructions. 

## Hazard Detection Unit and Forwarding Unit
Hazards are problems that could be found in the instruction pipeline of a processor that could lead to errors in the computation results. The **hazard detection unit** stalls the pipeline and inserts a "Non-Operation" until the next instruction is read. The hazard detection unit is often used when a LDUR instruction is immediately followed by an instruction that needs the use of the loaded register.

If the instruction in the EX stage needs a computed value from a previous instruction, the **forwarding unit** sends computed values from the MEM or WB stage of the pipeline to EX stage. There are multiplexers in the EX stage that pass values from the MEM and WB stage so the most current computed value can be used. 
 

	1. The instruction memory in this project is designed to have 64 8-bits for each index, since this CPU is little endian
	2. The Data Memory is made up of 31 64-bit values to show that the values could be accessed and stored via the CPU 

## ISA Explanations

### LDUR: Load RAM into Registers

Example: LDUR r2, [r10]

- Explanation: Retrieve the value in memory at location r10 and put that value into register r2

### STUR: Store Registers into RAM

Example: STUR r1, [r9]

- Explanation: Store the value of r1 into memory at the location r9

### ADD: Add Registers

Example: ADD r5, r3, r2

- Explanation: Add the values of r3 and r2 then put the result into r5

### SUB: Subtract Registers

Example: SUB r4, r3, r2

- Explanation: Subtract the values of r3 and r2 then put the result into r4

### ORR: Bit-wise OR Registers

Example: ORR r6, r2, r3

- Explanation: Bit-wise OR the values of r2 and r3 then put the result into r6

### AND: Bit-wise AND Registers

Example: AND r4, r3, r2

- Explanation: Bit-wise AND the values of r3 and r2 and put the result into r4

### CBZ: Conditional Jump (when the value in Register is zero)

Example: CBZ r1, #2

- Explanation: If the value of r1 is zero then jump to instruction 2, otherwise, continue executing PC++

### B: Unconditional (arbitrary) Jump

Example: B #2

- Explanation: Jump to instruction 2

### NOP: No Operation

Example: NOP

- Explanation: An instruction that makes the processor wait one clock cycle.

## Test Program (Instructions)

The thirteen instructions as shown in the table below is the test program used to test the functionality of the CPU.

|    ARM Assembly   |                Machine Code             | Hexadecimal|
|:------------------|:---------------------------------------:|:----------:|
| LDUR x0, [x2, #3] | 1111 1000 0100 0000 0011 0000 0100 0000 | 0xf8403040 |
| ADD x9, x0, x5    | 1000 1011 0000 0101 0000 0000 0000 1001 | 0x8b050009 |
| ORR x10, x1, x9   | 1010 1010 0000 1001 0000 0000 0010 1010 | 0xaa09002a |
| AND x11, x9, x0   | 1000 1010 0000 0000 0000 0001 0010 1011 | 0x8a00012b |
| SUB x12 x0 x11    | 1100 1011 0000 1011 0000 0000 0000 1100 | 0xcb0b000c |
| STUR x9, [x3, #6] | 1111 1000 0000 0000 0110 0000 0110 1001 | 0xf8006069 |
| STUR x10, [x4, #6]| 1111 1000 0000 0000 0110 0000 1000 1010 | 0xf800608a |
| STUR x11, [x5, #6]| 1111 1000 0000 0000 0110 0000 1010 1011 | 0xf80060ab |
| STUR x12, [x6, #6]| 1111 1000 0000 0000 0110 0000 1100 1100 | 0xf80060cc |
| B #10             | 0001 0100 0000 0000 0000 0000 0000 1010 | 0x1400000a |

## Test Program (Registers and Data Memory Setup)

The instructions were entered into the instruction memory itself to properly show its functionality while simulated. 

The Registers were initialized with values from 0-30 with register 31 defined set to 0 as stated in the reference sheet for LEGv8. 

The Data Memory was initialized with 5 times its index value.
