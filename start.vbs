Set WshShell = WScript.CreateObject("WScript.Shell")
Set objWshShell = CreateObject("Wscript.Shell")

objWshShell.run "createCondaEnvironment.bat", 1
WScript.Sleep 5000
WshShell.SendKeys "y"
WScript.Sleep 1000
WshShell.SendKeys "{ENTER}"
WScript.Sleep 15000
WshShell.SendKeys "exit"
WScript.Sleep 1000
WshShell.SendKeys "{ENTER}"
WScript.Sleep 15000
objWshShell.run "start_conda_environment.bat", 1
WScript.Sleep 5000
WshShell.SendKeys "pip install --ignore-installed --upgrade tensorflow==2.0.0"
WshShell.SendKeys "{ENTER}"
WScript.Sleep 30000
WshShell.SendKeys "pip install -r requirements.txt"
WshShell.SendKeys "{ENTER}"
WScript.Sleep 120000
objWshShell.run "finishSetUp.bat", 1
WScript.Sleep 5000
WshShell.SendKeys "exit"
WshShell.SendKeys "{ENTER}"
