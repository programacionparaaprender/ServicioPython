import win32serviceutil, win32service
import win32event, win32api
import servicemanager
import time

import win32gui, win32gui_struct, win32con

class EventDemoService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PyServiceEventDemo"
    _svc_display_name_ = "Python Service Event Demo"
    _svc_description_ = "Demonstrates a Python service which takes advantage of the extra notifications"
    def __init__(self, args):
         win32serviceutil.ServiceFramework.__init__(self, args)
         self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
         self.running = True
    def SvcStop(self):
         self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
         win32event.SetEvent(self.hWaitStop)
         self.running = False
    def SvcDoRun(self):
         self.ReportServiceStatus(win32service.SERVICE_RUNNING)
         while self.running:
         servicemanager.LogInfoMsg("aservice - is alive and well")
         time.sleep(3)
def ctrlHandler(ctrlType):
    return True

if __name__=='__main__':
    win32api.SetConsoleCtrlHandler(ctrlHandler, True)
    win32serviceutil.HandleCommandLine(EventDemoService)