
# Turing Complete Language (with IDE)
 - Can move pointer
 - Can add or substract value
 - can loop 
 - can do i/o
<br>

## Compile
`python3 main.py file`

## IDE
`python3 edit.py`

## Syntax:
- `inc` increment value at pointer
- `dec` decrment value at pointer
- `right` move pointer right
- `left` move pointer left
- `out` output value at pointer location
- `input` ask for input and store at location
- `goto` takes an input of a number and moves the pointer to that location
- `define` add variable
- `set` set var to something
- `push` print variable
- `loop` loop
- `if` if
<br>

### Loop Example:
```
loop // define loop
5 // how many times to run looop
... commands to run
endloop
```
<br>

### Variable Example
```
define vartest
set vartest 5
push vartest
```

### Goto Example
```
goto 4 // Moves the pointer to location 4
```

### If Examples:
```
define var1
define var2
set var1 3
set var2 4

if var1 == var2
// Output will be false

if var1 != var2
// Output will be True

if var1 >= var2
// Output will be false

if var1 <= var2
// Output will be true

if var1 > var2
// Output will be false

if var1 < var2
// Output will be true
```
