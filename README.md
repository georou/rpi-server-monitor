# rpi-server-monitor

Using the lxml HTML scraper and requests library, this checks the gametracker website to see if there is any active online users in a server and then turns on an LED.

Checking is done a little more than every __5 minutes__ to line up with how often gametracker's page refreshes.

## How To Use:
1. Replace the IP-ADDRESS in the page variable to the server you want to monitor
2. Copy the service file to /etc/systemd/system
3. Copy the .py file to desired location and edit the service file to match
4. ```sudo systemct daemon-reload```
5. ```sudo systemctl enable rpi-server-monitor.service && systemctl start rpi-server-monitor```

__Optional:__
Copy and add another function to monitor multiple servers. Remember to output them to different GPIO pins!

## Notes:
* Raspberry PI - All models with a working internet connection and Python
* Tested on a RPI Zero W
* Written for python 2.7 aiming to be portable as 2.7 is the default on Raspbian OS