~F2::
Suspend
return

string := "+laps seers"
min:= 27
sec:= 1

time := ((min * 60) + sec) * 1000
toogle := 0
Return

F2::
    toogle := !toogle
    if(toogle){
        Settimer, Label, %time%
    } else {
        Settimer, Label, Off
    }
Return

Label:
    Sendraw, %string%
    Send {enter}
Return