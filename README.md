# Simple parental control
# A simple script to allow only 1h/day 

## Spending more than an hour a day in front of a computer can be harmful for kids
    Physical problems like eye strain, neck and back pain, and carpal tunnel syndrome
    Sleep problems
    Difficulty focusing
    Social isolation
    Negative effects on mental and emotional well-being

To prevent these harms, it's important to:

    Limit a child's computer usage to a reasonable amount of time each day
    Encourage them to engage in other activities that involve physical activity, 
    social interaction, and creativity.

###How to install
    Create c:\temp
    Run install.py
    A windows service called Ztime will be installed on your Windows machine


The script automatically shuts down the computer if the total usage time for a given day exceeds a specified maximum value (in seconds). This maximum time, known as "max_time", can be customized by editing the value in the script. If the cumulated usage time for a day exceeds this maximum, the script will shut down the computer to prevent further usage. This helps ensure that kids don't exceed a healthy amount of screen time each day.