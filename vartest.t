define newvar
set newvar 4
set currentpoint newvar
out
goto newvar
set currentpoint 3
out
loop
5
set newvar currentpoint 
set currentpoint newvar
out
goto newvar
endloop