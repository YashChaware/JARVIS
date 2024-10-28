import openai
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime
import subprocess
import pyautogui
import time
import sys
from googlesearch import search
import psutil 
import ctypes
from api_key import apikey  # remove this 
openai.api_key = apikey  # replace apikey with your actuial api key 

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"User: {query}\nJarvis: "
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Jarvis, an AI assistant created by tony stark to help with various tasks."},
            {"role": "user", "content": query}
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = response.choices[0].message['content']
    say(response_text)
    chatStr += f"{response_text}\n"
    return response_text

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt}\n*************************\n\n"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Jarvis, an AI assistant created by tony stark to help with various tasks."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response.choices[0].message['content']
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()  # Return the query in lowercase for easier matching
        except sr.UnknownValueError:
            say("Sorry, I didn't catch that. Could you repeat?")
            return ""  # Return an empty string when speech is not recognized
        except sr.RequestError:
            say("Could not request results from Google Speech Recognition service.")
            return ""  # Return an empty string on API failure
        except Exception as e:
            print(f"Error: {e}")
            return ""  # Return an empty string for any other errors


def open_folder(folder_name):
    for root, dirs, files in os.walk("/"):
        for dir_name in dirs:
            if folder_name.lower() in dir_name.lower():
                folder_path = os.path.join(root, dir_name)
                os.startfile(folder_path)
                return True
    return False

def open_application(app_name):
    for root, dirs, files in os.walk("/Applications"):
        for file_name in files:
            if app_name.lower() in file_name.lower():
                app_path = os.path.join(root, file_name)
                os.startfile(app_path)
                return True

    app_executable = app_name.lower().replace(" ", "").replace(".", "") + ".exe"
    process = subprocess.Popen(["powershell", "Get-AppxPackage | Select Name, PackageFamilyName, InstallLocation"], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    package_lines = output.decode("utf-8").split("\n")

    for line in package_lines:
        if app_executable in line.lower():
            package_family_name = line.split(":")[-1].strip()
            os.system(f"start shell:AppsFolder\\{package_family_name}!{app_executable}")
            return True

    return False

def open_music():
    package_family_name = "Microsoft.ZuneMusic_8wekyb3d8bbwe"
    app_id = "!Microsoft.ZuneMusic"
    os.system(f"start shell:AppsFolder\\{package_family_name}{app_id}")

def play_media():
    package_family_name = "Microsoft.ZuneMusic_8wekyb3d8bbwe"
    app_id = "!Microsoft.ZuneMusic"
    os.system(f"start shell:AppsFolder\\{package_family_name}{app_id}")
    time.sleep(3)
    pyautogui.press('playpause')

def pause_media():
    pyautogui.press('playpause')

def resume_media():
    pyautogui.press('playpause')

def stop_media():
    pyautogui.press('stop')

def next_track():
    pyautogui.press('nexttrack')

def previous_track():
    pyautogui.press('prevtrack')

def volume_up():
    pyautogui.press('volumeup')

def volume_down():
    pyautogui.press('volumedown')

def mute_volume():
    pyautogui.press('volumemute')

def set_volume(level):
    """
    Sets the system volume to a specified level (0 to 100) directly on Windows.
    """
    if not 0 <= level <= 100:
        raise ValueError("Volume level must be between 0 and 100.")
    
    # Calculate the volume level in the range required by the API
    level = level / 100.0  # Convert to a fraction between 0.0 and 1.0
    
    # Use ctypes to interact with the Windows audio API
    ctypes.windll.winmm.waveOutSetVolume(0, int(level * 0xFFFF))  # 0xFFFF is the maximum volume level




def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

def get_current_date_time():
    now = datetime.datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")
    time_str_24hr = now.strftime("%H:%M")
    time_str_12hr = now.strftime("%I:%M %p")
    return now, date_str, time_str_24hr, time_str_12hr

def greet_based_on_time():
    now, _, _, _ = get_current_date_time()  # Only unpacking 'now'
    hour = now.hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"

def goodbye_based_on_time():
    now, _, _, _ = get_current_date_time()  # Only unpacking 'now'
    hour = now.hour
    if 5 <= hour < 12:
        return "Have a nice day"
    elif 12 <= hour < 17:
        return "Have a nice afternoon"
    elif 17 <= hour < 21:
        return "Have a nice evening"
    else:
        return "Good night, have a nice sleep"

def get_battery_percentage():
    battery = psutil.sensors_battery()
    if battery is not None:
        percent = battery.percent
        is_plugged = battery.power_plugged
        if is_plugged:
            return f"Your battery is at {percent} percent and is currently charging."
        else:
            return f"Your battery is at {percent} percent."
    else:
        return "Unable to determine battery status."

def open_file_explorer(path=None):
    try:
        if path:
            os.startfile(path)  # Open the specified path
        else:
            os.startfile(".")  # Open File Explorer at the current directory
        return True
    except Exception as e:
        print(f"Error opening File Explorer: {e}")
        return False

def open_this_pc():
    try:
        os.startfile("shell:MyComputerFolder")  # Opens "This PC"
        return True
    except Exception as e:
        print(f"Error opening 'This PC': {e}")
        return False