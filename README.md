# obs-countdown-python
A Python plugin for OBS Studio that allows setting an on-screen countdown to a particular date and time.

**Note: Does not allow counting down for a specific amount of time (e.g., 5 minutes), only to a particular time (e.g., 5:00 pm)**.

![](https://i.imgur.com/pZ3Kf1B.png)

# How to Use
### Initial Setup
Download and install Python 3.6+ (for example, [3.6.8](https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe)). Be sure to choose the option that adds Python to the PATH environment variable.

Open a Command Prompt or PowerShell and type the following commands to install the required dependencies.

```
pip install python-dateutil
pip install pyperclip
```

In OBS Studio, open Tools > Scripts > Python Settings, and enter the path to the Python installation directory.

![](https://i.imgur.com/hcOl2hj.png)

### Plugin Setup
Download the latest version of [obs-countdown.py](https://github.com/micahmo/obs-countdown-python/blob/master/obs-countdown.py).

In OBS Studio, open Tools > Scripts, click the plus icon to add a script, and browse to the obs-countdown.py file.

Populate the fields with the desired text to be displayed on screen.
 - **Countdown Date/Time**: This field should contain the target time when the stream is intended to start. The value can be entered in any format with various elements omitted. For example, if the date is omitted, it is assumed to be today. If AM/PM is omitted, it is assumed to be the next instance of the time in the future.
 - **Text to display**: This field should contain the text that is shown on screen during the countdown. Use the `%s` marker to indicate where the remaining time should be placed within the string. If no other text is needed, the `%s` marker can be used on its own.
 - **Expired text**: This field should contain the text that is displayed on screen when the countdown timer has expired. Leave blank to show no text at the end of the contdown.

### Text Setup
In order to use the output of the plugin, you must create a text source whose input is a text file that is updated by the plugin. While still in the Scripts configuration screen, click the "Copy file path" button.

Now, add a new Text source to your scene.

![](https://i.imgur.com/xeOCiUX.png)

In the text source properties editor, choose the option to "Read from file". For the "Text File" field, Browse and paste the file path that was previously copied from the script configuration. Set any other properties as desired on the text (for example, it is recommended to set "Alignment" to "Center").

![](https://i.imgur.com/NtxaCtJ.png)

### Example
With the configuration specified at the beginning, the countdown text would display the following at 8:31:11 PM.

![](https://i.imgur.com/Zi7Dbn9.png)
