# f08-for
Write a Python program called `conversions.py` that prints-out a table with a column for decimal integers, binary bits, and hexidecimal (base 16) and 32 rows, that range from 0 to 31.  You should use the functions `bin()` and `hex()`.  The `bin()` function takes an integer as an input and returns a `str` with the binary representation of the integer. In other words, it converts decimal to binary bits.  Similarly, `hex()` takes an integer as input and returns a `str` with the hexadecimal representation of the integer.

The output of `conversions.py` should look like the following:

| decimal |  binary   |   hex  |
|:--------|:----------|:-------|
|    0    |    0b0    |    0x0 |
|    1    |    0b1    |    0x1 |
|    2    |    0b10    |    0x2 |
|    3    |    0b11    |    0x3 |
|    4    |    0b100    |    0x4 |
|    5    |    0b101    |    0x5 |
|    6    |    0b110    |    0x6 |
|    7    |    0b111    |    0x7 |
|    8    |    0b1000    |    0x8 |
|    9    |    0b1001    |    0x9 |
|    10    |    0b1010    |    0xa |
|    11    |    0b1011    |    0xb |
|    12    |    0b1100    |    0xc |
|    13    |    0b1101    |    0xd |
|    14    |    0b1110    |    0xe |
|    15    |    0b1111    |    0xf |
|    16    |    0b10000    |    0x10 |
|    17    |    0b10001    |    0x11 |
|    18    |    0b10010    |    0x12 |
|    19    |    0b10011    |    0x13 |
|    20    |    0b10100    |    0x14 |
|    21    |    0b10101    |    0x15 |
|    22    |    0b10110    |    0x16 |
|    23    |    0b10111    |    0x17 |
|    24    |    0b11000    |    0x18 |
|    25    |    0b11001    |    0x19 |
|    26    |    0b11010    |    0x1a |
|    27    |    0b11011    |    0x1b |
|    28    |    0b11100    |    0x1c |
|    29    |    0b11101    |    0x1d |
|    30    |    0b11110    |    0x1e |
|    31    |    0b11111    |    0x1f |

You should use the following line to write the header row:
```
print('\tdecimal\tbinary\t\thex')
```

Notice that the pair of characters `\t` together represent the `TAB` or tabulation character.

You will notice that when you first try to print the table, it will be misaligned:

| decimal |  binary |  |   hex  |
|:--------|:--------|:-|:------|
|    0    |    0b0  |    0x0 | |
|    1    |    0b1  |    0x1 | |
|    2    |    0b10 |    0x2 | |
|    3    |    0b11 |    0x3 | |
|    4    |    0b100 |   0x4 | |
|    5    |    0b101  |  0x5 | |
|    6    |    0b110  |  0x6 | |
|    7    |    0b111  |  0x7 | |
|    8    |    0b1000    | |   0x8 |
|    9    |    0b1001    | |   0x9 |
|    10    |    0b1010   | |   0xa |

You will need to find a way to enter an extra tab, `\t`, to the first several rows.

HINT: After the first header row, `print('\tdecimal\tbinary\t\thex')`, all of the other rows have the same basic structure, so you will need to figure-out how to use some of the techniques we studied in Chapter 3 of GICP to repeatedly print-out similar rows.

## Rubric

|  Criteria                    | Possible | Actual  | Notes |
|:-----------------------------|:--------:|:-------:|:------|
| Iteration 0 - 31             |     2    |         |    |
| Showing decimal              |     2    |         |    |
| Showing binary               |     2    |         |    |
| Showing hexadecimal          |     2    |         |    |
| DOCSTRING                    |     1    |         |    |
| Comments                     |     1    |         |    |
| TOTAL                        |    10    |         |    |
