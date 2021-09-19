; User variables
command := "+laps seers"
min := 0
sec := 1
; End user variables

; Internal timing variables
command_time := ((min * 60) + sec) * 1000
return

; Main - application
Main:
    Sendraw, %command%
    SendEvent, {tab}{enter}
return

; Start script
F2::
    script_active := !script_active
    if(script_active){
        Sendraw, %command%
        SendEvent, {tab}{enter}
        Settimer, Main, %command_time%
    } else {
        Settimer, Main, Off
    }
return

; Terminate the script
F3::ExitApp