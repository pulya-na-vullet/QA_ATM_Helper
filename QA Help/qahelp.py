import customtkinter
import json
import subprocess

#Объявление параметров приложения.
app = customtkinter.CTk()
app.title("QA help")
app.geometry("550x340")
filePath = "C:\\Program Files (x86)\\QA Help\\appConfig.json"

def openConfigureJson(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)
        keyConfigDevOmniVideo = data["configDevOmniVideo"]
        keyConfigAppSettingsSupervisor = data["configAppSettingsSupervisor"]
        keyConfigTerminalOmnivideo = data["configTerminalOmnivideo"]
        keyConfigScreenRecorder = data["configScreenRecorder"]
        keyScript = data["copyAndClose"]
    file.close()
    return keyConfigDevOmniVideo, keyConfigAppSettingsSupervisor, keyConfigTerminalOmnivideo, keyConfigScreenRecorder, keyScript
def changeDEV():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        data['baseApi'] = 'https://gateway.omnivideo.dev.bfs-it.ru'
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
    with open(configAppSettingsSupervisor, 'r+') as file:
        data = json.load(file)
        data['Metrics']['BackendUrl'] = 'terminal.dev.bfs-it.ru'
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
    with open(configTerminalOmnivideo, 'r+') as file:
        data = json.load(file)
        data['Url'] = 'https://terminal.dev.bfs-it.ru/'
        file.seek(0)
        json.dump(data,file, indent=4)
        file.truncate()
    file.close()
    with open(configScreenRecorder, 'r+') as file:
        data = json.load(file)
        data['RecordingConfiguration']['ServerUrl'] = 'https://omnivideo.dev.bfs-it.ru/'
        file.seek(0)
        json.dump(data,file, indent=4)
        file.truncate()
    file.close()
def changeSTAGING():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        data['baseApi'] = 'https://gateway.omnivideo.staging.bfs-it.ru'
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
    with open(configAppSettingsSupervisor, 'r+') as file:
        data = json.load(file)
        data['Metrics']['BackendUrl'] = 'terminal.staging.bfs-it.ru'
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
    with open(configTerminalOmnivideo, 'r+') as file:
        data = json.load(file)
        data['Url'] = 'https://terminal.staging.bfs-it.ru/'
        file.seek(0)
        json.dump(data,file, indent=4)
        file.truncate()
    file.close()
    with open(configScreenRecorder, 'r+') as file:
        data = json.load(file)
        data['RecordingConfiguration']['ServerUrl'] = 'https://omnivideo.staging.bfs-it.ru/'
        file.seek(0)
        json.dump(data,file, indent=4)
        file.truncate()
    file.close()
def changeDEMO():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        data['baseApi'] = 'https://gateway.omnivideo.demo.bfs-it.ru'
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
    with open(configAppSettingsSupervisor, 'r+') as file:
        data = json.load(file)
        data['Metrics']['BackendUrl'] = 'terminal.demo.bfs-it.ru'
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
    with open(configTerminalOmnivideo, 'r+') as file:
        data = json.load(file)
        data['Url'] = 'https://terminal.demo.bfs-it.ru/'
        file.seek(0)
        json.dump(data,file, indent=4)
        file.truncate()
    file.close()
    with open(configScreenRecorder, 'r+') as file:
        data = json.load(file)
        data['RecordingConfiguration']['ServerUrl'] = 'https://omnivideo.demo.bfs-it.ru/'
        file.seek(0)
        json.dump(data,file, indent=4)
        file.truncate()
    file.close()
def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())
def oldControlScreen():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        data['controlScreen']['width'] = 340
        data['controlScreen']['height'] = 1080
        data['controlScreen']['x'] = 0
        data['controlScreen']['y'] = 0
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
def verticalControlScreen():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        data['controlScreen']['width'] = 1080
        data['controlScreen']['height'] = 1920
        data['controlScreen']['x'] = 0
        data['controlScreen']['y'] = 0
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
def comfortControlScreen():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        data['controlScreen']['width'] = 960
        data['controlScreen']['height'] = 800
        data['controlScreen']['x'] = 0
        data['controlScreen']['y'] = 0
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
def controlScreenCheckBox():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        if fullScreenCheckVar.get() == "on":
            data['controlScreen']['fullScreen'] = True
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        if fullScreenCheckVar.get() == "off":
            data['controlScreen']['fullScreen'] = False
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    file.close()
def resizableCPCheckBox():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        if resizableCP.get() == "on":
            data['controlScreen']['resizable'] = True
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        if resizableCP.get() == "off":
            data['controlScreen']['resizable'] = False
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    file.close()
def videoScreenCheckBox():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        if videoScreenCheckVar.get() == "on":
            data['videoScreen']['fullScreen'] = True
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        if videoScreenCheckVar.get() == "off":
            data['videoScreen']['fullScreen'] = False
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    file.close()
def resizableVPCheckBox():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        if resizableVP.get() == "on":
            data['videoScreen']['resizable'] = True
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        if resizableVP.get() == "off":
            data['videoScreen']['resizable'] = False
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    file.close()
def hideMenuBarCheckBox():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        if hideMenuBar.get() == "on":
            data['hideMenuBar'] = True
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        if hideMenuBar.get() == "off":
            data['hideMenuBar'] = False
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    file.close()
def oldVideoScreen():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        data['videoScreen']['width'] = 960
        data['videoScreen']['height'] = 1080
        data['videoScreen']['x'] = 340
        data['videoScreen']['y'] = 0
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
def verticalVideoScreen():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        data['videoScreen']['width'] = 1080
        data['videoScreen']['height'] = 1920
        data['videoScreen']['x'] = 1080
        data['videoScreen']['y'] = 0
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
def comfortVideoScreen():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        data['videoScreen']['width'] = 960
        data['videoScreen']['height'] = 800
        data['videoScreen']['x'] = 960
        data['videoScreen']['y'] = 0
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()
def run_script():
    subprocess.call(["cscript", keyScript, ])

configDevOmniVideo, configAppSettingsSupervisor, configTerminalOmnivideo, configScreenRecorder, keyScript = openConfigureJson(filePath)

#интерфейс
radio_var = customtkinter.IntVar(value=0)
radiobuttonDEV = customtkinter.CTkRadioButton(app, text="DEV",command=changeDEV, variable= radio_var,value=1)
radiobuttonDEV.grid(row=1, column=0, padx=20, pady=10)
radiobuttonSTAGING = customtkinter.CTkRadioButton(app, text="STAGING",command=changeSTAGING, variable= radio_var,value=2)
radiobuttonSTAGING.grid(row=1, column=1, padx=20, pady=10)
radiobuttonDEMO = customtkinter.CTkRadioButton(app, text="DEMO",command=changeDEMO, variable= radio_var,value=3)
radiobuttonDEMO.grid(row=1, column=2, padx=20, pady=10)

oldControlScreenButton = customtkinter.CTkButton(app, fg_color=("#d68a59"), hover_color=("#fbceb1") , text="CP:340*1024", command=oldControlScreen)
oldControlScreenButton.grid(row=2, column=0, padx=20, pady=10)
verticalControlScreenButton = customtkinter.CTkButton(app, text="CP:1080*1920", command=verticalControlScreen)
verticalControlScreenButton.grid(row=2, column=1, padx=20, pady=10)
comfortControlScreenButton = customtkinter.CTkButton(app, fg_color=("#DB3E39"), hover_color=("#660011"), text="CP:Comfort*Test", command=comfortControlScreen)
comfortControlScreenButton.grid(row=2, column=2, padx=20, pady=10)

fullScreenCheckVar = customtkinter.StringVar(value="off")
fullScreenControlScreen = customtkinter.CTkCheckBox(app, text="Full Scr CP", command=controlScreenCheckBox, variable=fullScreenCheckVar, onvalue="on", offvalue="off")
fullScreenControlScreen.grid(row=3,column=0, padx=20, pady=10)

resizableCP = customtkinter.StringVar(value="off")
resizableControlScreen = customtkinter.CTkCheckBox(app, text="Resize CP", command=resizableCPCheckBox, variable=resizableCP, onvalue="on", offvalue="off")
resizableControlScreen.grid(row=3,column=1, padx=20, pady=10)

hideMenuBar = customtkinter.StringVar(value="off")
hideMenuBarConfig = customtkinter.CTkCheckBox(app, text="Hide Menu Bar", command=hideMenuBarCheckBox, variable=hideMenuBar, onvalue="on", offvalue="off")
hideMenuBarConfig.grid(row=3,column=2, padx=20, pady=10)

oldVideoScreenButton = customtkinter.CTkButton(app, fg_color=("#d68a59"), hover_color=("#fbceb1") , text="VP:960*1024", command=oldVideoScreen)
oldVideoScreenButton.grid(row=4, column=0, padx=20, pady=10)
verticalVideoScreenButton = customtkinter.CTkButton(app, text="VP:1080*1920", command=verticalVideoScreen)
verticalVideoScreenButton.grid(row=4, column=1, padx=20, pady=10)
comfortVideoScreenButton = customtkinter.CTkButton(app, fg_color=("#DB3E39"), hover_color=("#660011"), text="VP:Comfort*Test", command=comfortVideoScreen)
comfortVideoScreenButton.grid(row=4, column=2, padx=20, pady=10)

videoScreenCheckVar = customtkinter.StringVar(value="off")
fullScreenVideoScreen = customtkinter.CTkCheckBox(app, text="Full Scr VP", command=videoScreenCheckBox, variable=videoScreenCheckVar, onvalue="on", offvalue="off")
fullScreenVideoScreen.grid(row=5,column=0, padx=20, pady=10)

resizableVP = customtkinter.StringVar(value="off")
resizableControlScreen = customtkinter.CTkCheckBox(app, text="Resize VP", command=resizableVPCheckBox, variable=resizableVP, onvalue="on", offvalue="off")
resizableControlScreen.grid(row=5,column=1, padx=20, pady=10)

entry = customtkinter.CTkEntry(app, placeholder_text="Set ATM number")
entry.grid(row=5,column=2, padx=20, pady=10)

def entryTerminalCode():
    with open(configDevOmniVideo, 'r+') as file:
        data = json.load(file)
        TerminalCode = entry.get()
        data['terminal']['code'] = TerminalCode
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    file.close()

SaveATMNumberBatton  = customtkinter.CTkButton(app, text="Change ATM Code", fg_color=("#686868"), hover_color=("#8D8D8D"), command=entryTerminalCode)
SaveATMNumberBatton.grid(row=6, column=2, padx=20, pady=10)

SaveAprooveBatton  = customtkinter.CTkButton(app, text="Save & Aproove", fg_color=("#009B00"), hover_color=("#008000"), command=run_script)
SaveAprooveBatton.grid(row=7, column=2, padx=20, pady=10)
app.mainloop()