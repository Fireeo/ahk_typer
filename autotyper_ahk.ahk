string := "+laps seers"
min:= 0
sec:= 3

time := ((min * 60) + sec) * 1000
toogle := 0
return

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