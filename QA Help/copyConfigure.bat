Copy-Item -Path "C:\Program Files (x86)\QA Help\Supervisor\appsettings.json" -Destination "C:\Program Files\BFS Supervisor\publish\" -Force
Copy-Item -Path "C:\Program Files (x86)\QA Help\Hardware\appsettings.json" -Destination "C:\Program Files\BFS Terminal Hardware" -Force
Copy-Item -Path "C:\Program Files (x86)\QA Help\ScreenRecorder\appsettings.json" -Destination "C:\Program Files\BFS OmniVideo ScreenRecorder\" -Force
taskkill /f /T /IM "BFS OmniVideo Terminal.exe"
