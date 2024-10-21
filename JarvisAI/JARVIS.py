import sys
from functions import *

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    greeting = greet_based_on_time()
    say(f"{greeting} sir. Jarvis is online.")
    
    now, date_str, time_str_24hr, time_str_12hr = get_current_date_time()
    say(f"Today's date is {date_str} and   the current time is   {time_str_24hr}")
    
    # Report battery percentage after greeting
    battery_status = get_battery_percentage()
    say(battery_status)

    say(f"How can i help you today")

    while True:
        fst = False
        query = takeCommand()
        if query.strip() == "":
                        continue
        elif "hey jarvis" in query.lower() or "jarvis" in query.lower():
            while True:
                if fst:
                    query = takeCommand()
                fst = True
                query = query.lower().replace("hey jarvis", "").replace("jarvis", "").strip()
                sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
                for site in sites:
                    if f"open {site[0]}".lower() in query.lower():
                        say(f"Opening {site[0]} sir...")
                        webbrowser.open(site[1])
    
                if "open music" in query.lower():
                        say("Opening music app...")
                        open_music()
                    
                   # Play music
                elif "play music" in query.lower() or "play songs" in query.lower():
                    say("Playing music...")
                    play_media()

                elif "pause music" in query.lower() or "pause song" in query.lower() or "stop music" in query.lower() or "stop song" in query.lower():
                    say("Pausing music...")
                    pause_media()

                elif "stop music" in query.lower() or "stop songs" in query.lower():
                    say("Stopping music...")
                    stop_media()

                elif "resume music" in query.lower() or "unpause music" in query.lower() or "unpause song" in query.lower() or "unpause music" in query.lower():
                    say("Resuming music...")
                    resume_media()

                elif "next track" in query.lower() or "next song" in query.lower():
                    say("Skipping to the next track...")
                    next_track()

                elif "previous track" in query.lower() or "previous song" in query.lower():
                    say("Going back to the previous track...")
                    previous_track()

                elif "set volume" in query.lower():
                    try:
                        level = int(query.lower().split("set volume to", 1)[1].strip())
                        set_volume(level)
                        say(f"Setting volume to {level} percent.")
                    except ValueError:
                        say("I couldn't understand the volume level. Please specify a number between 0 and 100.")

                elif "increase volume" in query.lower():
                    volume_up()
                    say("Increasing volume.")

                elif "decrease volume" in query.lower():
                    volume_down()
                    say("Decreasing volume.")

                elif "mute" in query.lower():
                    mute_volume()
                    say("Muting volume.")

                elif "unmute" in query.lower():
                    mute_volume()
                    say("Unmuting volume.")

                elif "take screenshot" in query.lower():
                    say("Taking screenshot...")
                    take_screenshot()

                elif "open folder" in query.lower():
                    folder_name = query.lower().split("open folder", 1)[1].strip()
                    if open_folder(folder_name):
                        say(f"Opening {folder_name} folder.")
                    else:
                        say(f"Sorry, I couldn't find the {folder_name} folder.")

                elif "open application" in query.lower():
                    app_name = query.lower().split("open application", 1)[1].strip()
                    if open_application(app_name):
                        say(f"Opening {app_name} application.")
                    else:
                        say(f"Sorry, I couldn't find the {app_name} application.")

                elif "open file explorer" in query.lower():
                    if open_file_explorer():
                        say("Opening File Explorer.")
                    else:
                        say("Sorry, I couldn't open File Explorer.")

                elif "this pc" in query.lower():
                    if open_this_pc():
                        say("Opening This PC.")
                    else:
                        say("Sorry, I couldn't open This PC.")

                elif "the time" in query and "12 hour" in query:
                    now, _, _, time_str_12hr = get_current_date_time()
                    say(f"Sir, the time is {time_str_12hr}")

                elif "the time" in query:
                    now, _, time_str_24hr, _ = get_current_date_time()
                    say(f"Sir, the time is {time_str_24hr}")

                elif "open facetime".lower() in query.lower():
                    os.system(f"open /System/Applications/FaceTime.app")

                elif "open pass".lower() in query.lower():
                    os.system(f"open /Applications/Passky.app")

                elif "using artificial intelligence".lower() in query.lower():
                    ai(prompt=query)

                elif "google search" in query.lower():
                    search_query = query.lower().split("google search", 1)[1].strip()
                    say(f"Searching Google for {search_query}...")
                    for url in search(search_query, num_results=3):
                        webbrowser.open(url)

                elif "wait" in query.lower() or "stop"in query.lower():
                    say("Okay, I'll wait.")
                    break

                elif "quit" in query.lower() or "exit" in query.lower() or "go offline" in query.lower() or "bye jarvis" in query.lower() or "goodbye" in query.lower() or "jarvis bye" in query.lower():
                    farewell = goodbye_based_on_time() 
                    say(f"{farewell} sir. JARVIS going offline.")
                    sys.exit()

                elif "reset chat" in query.lower():
                    chatStr = ""

                elif query.strip() == "":
                        continue

                # else:
                #     print("Chatting...")
                #     chat(query)

        elif "quit" in query.lower() or "exit" in query.lower() or "go offline" in query.lower() or "bye jarvis" in query.lower() or "goodbye" in query.lower() or "jarvis bye" in query.lower():
            farewell = goodbye_based_on_time() 
            say(f"{farewell} sir. JARVIS going offline.")
            sys.exit()
        else :
            continue