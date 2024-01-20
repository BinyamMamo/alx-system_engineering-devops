# Postmortem: How a Nginx server went down in flames 🔥

![Server on Fire](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzV0c2EyZmM2ZmR1Y2xzNG03OGRxd2toZHVneTZodmFjdGE0a2NzOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/P7JmDW7IkB7TW/giphy.gif)

## Issue Summary
- **Duration**: 75 minutes of chaos from 9:00 AM to 10:15 AM GMT.
- **Impact**: All users were greeted with a sassy 502 Bad Gateway error.
- **Root Cause**: The Nginx server process was leaking memory, causing resource depletion.

## Timeline
- **9:00 AM**: Monitoring system alerted us about unresponsive Nginx server, initially dismissed as glitch.
- **9:25 AM**: Engineer discovered bug in Nginx version causing memory leak, realized we hadn't updated.
- **9:30 AM**: Engineer upgraded Nginx to latest version, restarted server process.
- **10:00 AM**: Nginx server revived, users regained access to application without issues.


## Corrective and Preventive Measures
To prevent this issue from happening again,
- Upgrade all Nginx servers to latest version with memory leak bug fix.
- Implement regular software maintenance and updates.
- Improve incident response procedures for faster issue detection and resolution.


Remember, even in the midst of server flames, there's always a way to rise from the ashes! 🔥🔥🔥
