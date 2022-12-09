# parental-control

1. Add the on_shutdown script to Task Scheduler

    Open the Task Scheduler by searching for it in the Start menu.

    In the Task Scheduler window, click on the "Action" menu and select "Create Task".

    In the "Create Task" window, enter a name and description for the task, and select the user that the task should run as.

    Go to the "Triggers" tab, and click on the "New" button to create a new trigger for the task.

    In the "New Trigger" window, select the "At log on" option, and then select the specific user that the task should run for from the "Settings" section.

    Go to the "Actions" tab, and click on the "New" button to create a new action for the task.

    In the "New Action" window, select the "Start a program" option, and then specify the path to the script that you want to run.

    Click on the "OK" button to save the task.

2. Rename the main py to main.pyw, add it to Windows Startup

3. Create c:\temp\time.txt
