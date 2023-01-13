import wmi

name = 'PanGPA.exe'
f = wmi.WMI()

while True:
    try:
        for process in f.Win32_Process():
            if process.name == name:
                process.Terminate()
                print('Bloqueado')
    except:
        pass