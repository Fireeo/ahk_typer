; User variables
; Guards
guards_command := "+k 100 guards"
guard_min := 0
guard_sec := 1

; Clue
clue_command := "+m clue medium"
clue_min := 8
clue_sec := 30
; End user variables

; Internal timing variables
time_g := ((guard_min * 60) + guard_sec) * 1000
time_c := ((clue_min * 60) + clue_sec) * 1000
return
; End Internal timing variables

; Main - application
Main:
    Sendraw, %guards_command%
    Send {tab}{Enter}
    Sleep time_g
    Sendraw, %clue_command%
    Send {tab}{Enter}
    Sleep 3000
    Sendraw, %guards_command%
    Send {tab}{Enter}
    Sleep time_c
    Sendraw, %guards_command%
    Send {tab}{Enter}
    Sleep time_g
return

; Start script
F2::
    script_active := !script_active
    if(script_active){
        Settimer, Main, %command_time%
    } else {
        Settimer, Main, Off
    }
return

; Terminate the script
F3::ExitApp