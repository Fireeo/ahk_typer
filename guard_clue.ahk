guards_command := "+k 100 guards"
clue_command := "+m clue medium"
guard_kill_time_min := 27
clue_time_min := 27
time_buffer_after_clue_sec := 2




time_g := guard_kill_time_min * 3600000
time_c := clue_time_min * 36000000
time_buffer := time_buffer_after_clue_sec * 1000
toogle := 0

F2::
	toogle := !toogle
	if(toogle){
		Settimer, Label, %time%
	} else {
		Settimer, Label, Off
	}
Return

Label:		
	Sendraw, %guards_command%
	Send {tab}{Enter}
	Sleep time_g
	Sendraw, %clue_command%
	Sleep 500
	Send {tab}{Enter}
	Sleep %time_buffer%
	Sendraw, %guards_command%
	Send {tab}{Enter}
	Sleep time_c
	Sendraw, %guards_command%
	Send {tab}{Enter}
	Sleep time_g
return
		


