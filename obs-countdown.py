import obspython as obs
from datetime import datetime
from dateutil import parser # pip install python-dateutil 
import os
import pyperclip            # pip install pyperclip

# Properties
datetime = datetime.now()
text = "%s"
expiredtext = ""
debug = False

# Property names
datetime_property = "datetime"
text_propery = "text"
expired_text_property = "expiredtext"
debug_value_property = "debug-obs-countdown"

def script_description():
	return "Creates a dynamic countdown timer to a specified date/time.\r\n\r\n" \
"Specify the target time in the \"Countdown Date/Time\" field. The value can be input in any format, and the date can be omitted.\r\n\r\n" \
"Use the \"Text to display\" property to determine what string will be displayed containing the countdown timer. " \
"Use %s in the string to represent where the countdown timer should be placed.\r\n\r\n" \
"Use the \"Expired text\" property to determine what text to display after the countdown has expired. " \
"Leave blank to show no text after expiration."

def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_text(props, datetime_property, "Countdown Date/Time", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, text_propery, "Text to display", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, expired_text_property, "Expired text", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_button(props, "copypath", "Copy file path", copy_path)
    obs.obs_properties_add_bool(props, debug_value_property, "Debug")

    return props

def get_file_path():
    path = os.path.join(os.getenv('APPDATA'), "obs-countdown")    
    if not os.path.exists(path):
        os.makedirs(path)
    return os.path.join(path, "obs-countdown.txt")

def copy_path(props, prop):
    pyperclip.copy(get_file_path())

def script_update(settings):
    global datetime
    global text
    global expiredtext
    global debug

    obs.timer_remove(update)

    try:
        datetime = parser.parse(obs.obs_data_get_string(settings, datetime_property))
    except:
        # Don't let parsing kill us (which would annoyingly show the output dialog)
        pass

    text = obs.obs_data_get_string(settings, text_propery)
    expiredtext = obs.obs_data_get_string(settings, expired_text_property)
    debug = obs.obs_data_get_bool(settings, debug_value_property)

    debug_write(f"Retrieved settings: datetime is {datetime}, text is {text}, expiredtext is {expiredtext}")
    
    obs.timer_add(update, 500)

def update():
    file = open(get_file_path(), "w+")

    # Write a bunch of spaces to the file so that it is wide text
    # then it can fill the whole width of the screen, and we can use the center alignment
    # to ensure that the rest of the text is centered
    file.write("                                                                           \r\n")

    difference = (datetime - datetime.now())    
    
    if (difference.total_seconds() > 0):
        timeStr = create_time_string(difference)
        toWrite = text.replace("%s", timeStr)
        
        file.write(toWrite)
        debug_write(f"Wrote '{toWrite}' to file")
    else:
        toWrite = expiredtext
        file.write(toWrite)
        debug_write(f"Wrote '{toWrite}' to file")
        obs.timer_remove(update)
    
    file.close()

def create_time_string(difference):
    differenceHours = difference.seconds // 3600
    differenceMinutes = (difference.seconds // 60) % 60
    differenceSeconds = difference.seconds % 60
    timeStr = ""
    
    if (difference.days > 0):
        timeStr = f"{difference.days}.{differenceHours:02d}:{differenceMinutes:02d}:{differenceSeconds:02d}"
    elif (differenceHours > 0):
        timeStr = f"{differenceHours}:{differenceMinutes:02d}:{differenceSeconds:02d}"
    else:
        timeStr = f"{differenceMinutes}:{differenceSeconds:02d}"
    
    return timeStr

def debug_write(message):
    if (debug):
        print(message)