Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Program Files (x86)\QA Help\copyConfigure.bat" & Chr(34), 0
Set WshShell = Nothing