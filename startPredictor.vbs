Set WshShell = WScript.CreateObject("WScript.Shell")
Set objWshShell = CreateObject("Wscript.Shell")

objWshShell.run "start_conda_environment.bat", 1
WScript.Sleep 500
WshShell.SendKeys "python gradeModelPredictor.py"
WshShell.SendKeys "{ENTER}"