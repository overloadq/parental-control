import win32service
import win32serviceutil
import win32event
import subprocess


class ParentalControl(win32serviceutil.ServiceFramework):
    _svc_name_ = "Ztime"
    _svc_display_name_ = "Ztime Service"
    _svc_description_ = "Ztime custom service."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        import servicemanager
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        # Run your main.pyw script
        subprocess.call(["python", "main.pyw"])


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(ParentalControl)
