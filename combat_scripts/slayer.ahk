; User variables
command := "+slayertask chaeldar"
command2 := "+autoslay"
min := 0
sec := 5
sec_between_commands = 3
; End user variables

; Internal timing variables
command_time := ((min * 60) + sec) * 1000
first_write := True
return


; Main - application
Main:
    Sendraw, %command%
    SendEvent, {tab}{enter}
return

; Main - application
Main2:
    Sendraw, %command2%
    SendEvent, {tab}{enter}
return

; Start script
F2::
    script_active := !script_active
    if(script_active){
        if (first_write) {
            Sendraw, %command%
            SendEvent, {tab}{enter}
            Sleep, sec_between_commands * 1000

            Sendraw, %command2%
            SendEvent, {tab}{enter}
            first_write = False;
        }
        Settimer, Main, %command_time%
        Sleep, sec_between_commands * 1000
        Settimer, Main2, %command_time%
    } else {
        Settimer, Main, Off
        Settimer, Main2, Off
    }
return

; Terminate the script
F3::ExitApp