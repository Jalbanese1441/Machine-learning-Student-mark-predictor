Set WshShell = WScript.CreateObject("WScript.Shell")
Set objWshShell = CreateObject("Wscript.Shell")


WshShell.SendKeys "exit(0)"
WshShell.SendKeys "{ENTER}"
WScript.Sleep 500
WshShell.SendKeys "exit"
WshShell.SendKeys "{ENTER}"