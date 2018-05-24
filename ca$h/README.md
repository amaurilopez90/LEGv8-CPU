# ca$h

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/amaurilopez90/Computer-Architecture/master/LICENSE)

# Purpose 
The purpose of this project is to study, via simulation, the performance of memory management policies and memory
configurations for cache memory systems. For the simulations, the trace files can be described below.

# Trace Files
The trace files have been generated on a PC. The two programs traced have been stripped by removing cache hits
observed by a cache with 32 sets, 1-way associative, with 8 contiguous addresses per line.

**Format:**
  - Each memory reference is recorded as a three-byte word. All references are stored successively without any delimiters
  - Both trace files are 180,000-bytes long, and contain 60,000 3-byte memory references. The stripping algorithm eliminated 90% of the original references from original traces approximately 600,000 references long
  - The first byte of a three-byte word is the least-significant byte, the third one is the most-significant byte
  - The lower three-bits of the least-significant byte are always cleared, since only the base address of the line containing the memory words referenced is recorded

**Example:** The first threee references of TRACE1.dat are 038FE8, 038FF8, and 039000, in hexadecimal form.
DEBUG prints this information as follows:
  - 5651:0100 E8 8F 03 F8 8F 03 00 90-03 80 75 0C 08 90 03 E8 .........u....
  - 5651:0110 FF 07 F0 FF 07 78 96 03-E8 8D 03 F0 8D 03 F0 FF ....x.........

# Project Goal
 To prepare a program to simulate a cache memory system. The cache memory system will be evaluated under two replacement policies: FIFO and LRU, given the criteria below
  1. L - number of bytes per line of cache memory
  2. K - number of lines per set
  3. N - number of sets
  
  The total number of bytes of cache memory is given by the product LKN and L=8 will be used throughout the simulations.
  The miss rate should then be recorded for each simulation using MISS RATE = (TOTAL # OF MISSES/TOTAL # OF REFERENCES x 10)                      
