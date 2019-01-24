[ThingSee One](https://thingsee.com) is a "smart developer device for IoT". This rugged and compact device comes with a ton of sensors. It can connect via Wi-Fi, Bluetooth, or cellular network (using a SIM card). Sending the data to ThingSee's cloud server is very easy, as it should be.

But there's a slight problem, because for my application, the requirement was to send the collected data to my own cloud provider (DropBox) using HTTPS protocol. The slight problem was that ThingSee doesn't support HTTPS yet for custom clouds (apparently this feature was requested many years ago but is still unimplemented til now). So this is why I created this solution, to be able to ultimately send the data from ThingSee One device to Dropbox using secure connection.

# Thingsee One

Recording the environment (e.g., temperature, pressure, humidity, etc.) and uploading it to a custom cloud.



