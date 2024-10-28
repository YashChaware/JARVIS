import sys
from functions import *

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    greeting = greet_based_on_time()
    say(f"{greeting} sir. Jarvis is online.")
    
    now, date_str, time_str_24hr, time_str_12hr = get_current_date_time()
    say(f"Today's date is {date_str} and   the current time is   {time_str_12hr}")
    
    # Report battery percentage after greeting
    battery_status = get_battery_percentage()
    say(battery_status)

    say(f"How can i help you today")

    while True:
        fst = False
        query = takeCommand()
        print(query)
        if query.strip() == "":
                        continue
        elif "hey jarvis" in query.lower() or "jarvis" in query.lower():
            while True:
                if fst:
                    query = takeCommand()
                fst = True
                query = query.replace("hey jarvis", "").replace("jarvis", "").strip()
                sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
                for site in sites:
                    if f"open {site[0]}".lower() in query:
                        say(f"Opening {site[0]} sir...")
                        webbrowser.open(site[1])
    
                if "open music" in query:
                        say("Opening music app...")
                        open_music()
                    
                   # Play music
                elif "play music" in query or "play songs" in query:
                    say("Playing music...")
                    play_media()

                elif "pause music" in query or "pause song" in query or "stop music" in query or "stop song" in query:
                    say("Pausing music...")
                    pause_media()

                elif "stop music" in query or "stop songs" in query:
                    say("Stopping music...")
                    stop_media()

                elif "resume music" in query or "unpause music" in query or "unpause song" in query or "unpause music" in query:
                    say("Resuming music...")
                    resume_media()

                elif "next track" in query or "next song" in query:
                    say("Skipping to the next track...")
                    next_track()

                elif "previous track" in query or "previous song" in query:
                    say("Going back to the previous track...")
                    previous_track()

                elif"maximize the volume" in query or "max the volume" in query:
                        set_volume(100)  # Set system volume to 100%
                        say("Maximizing the volume.")

                elif "set volume" in query:
                        if "max" in query:
                             set_volume(100)  # Set system volume to 100%
                        else:
                            # Improve number extraction by finding digits in the query
                            level_str = ''.join(filter(str.isdigit, query))
                        
                            if level_str:  # Check if a number was found
                                level = int(level_str)
                                if 0 <= level <= 100:
                                    set_volume(level)
                                    say(f"Setting volume to {level} percent.")
                                else:
                                    say("Please specify a volume level between 0 and 100.")
                            else:
                                say("I couldn't understand the volume level. Please specify a number between 0 and 100.")

                elif "increase volume" in query:
                    volume_up()
                    say("Increasing volume.")

                elif "decrease volume" in query:
                    volume_down()
                    say("Decreasing volume.")

                elif "mute" in query:
                    mute_volume()
                    say("Muting volume.")

                elif "unmute" in query:
                    mute_volume()
                    say("Unmuting volume.")

                elif "take screenshot" in query:
                    say("Taking screenshot...")
                    take_screenshot()

                elif "open folder" in query:
                    folder_name = query.lower().split("open folder", 1)[1].strip()
                    if open_folder(folder_name):
                        say(f"Opening {folder_name} folder.")
                    else:
                        say(f"Sorry, I couldn't find the {folder_name} folder.")

                elif "open application" in query:
                    app_name = query.lower().split("open application", 1)[1].strip()
                    if open_application(app_name):
                        say(f"Opening {app_name} application.")
                    else:
                        say(f"Sorry, I couldn't find the {app_name} application.")

                elif "open file explorer" in query:
                    if open_file_explorer():
                        say("Opening File Explorer.")
                    else:
                        say("Sorry, I couldn't open File Explorer.")

                elif "this pc" in query:
                    if open_this_pc():
                        say("Opening This PC.")
                    else:
                        say("Sorry, I couldn't open This PC.")

                elif "the time" in query:
                    if "24 hour" in query or "24 hours format" in query:
                        
                        # Unpack all 4 values, ignore date and 12-hour format with '_'
                        now, _, time_str_24hr, _ = get_current_date_time()
                        say(f"Sir, the time is {time_str_24hr}")
                    else:
                        # Default to 12-hour format
                        now, _, _, time_str_12hr = get_current_date_time()
                        say(f"Sir, the time is {time_str_12hr}")  # Added this line


                elif "open facetime".lower() in query:
                    os.system(f"open /System/Applications/FaceTime.app")

                elif "open pass".lower() in query:
                    os.system(f"open /Applications/Passky.app")

                elif "using artificial intelligence".lower() in query:
                    ai(prompt=query)

                elif "google search" in query:
                    search_query = query.split("google search", 1)[1].strip()
                    say(f"Searching Google for {search_query}...")
                    for url in search(search_query, num_results=3):
                        webbrowser.open(url)

                elif "wait" in query or "stop"in query or "vate" in query or" sleep" in query:
                    say("Okay, I'll wait.")
                    break

                elif "quit" in query or "exit" in query or "go offline" in query or "bye jarvis" in query or "goodbye" in query or "jarvis bye" in query:
                    farewell = goodbye_based_on_time() 
                    say(f"{farewell} sir. JARVIS going offline.")
                    sys.exit()

                elif "reset chat" in query:
                    chatStr = ""

                elif query.strip() == "":
                        continue

                else:
                    print("Chatting...")
                    chat(query)

        elif "quit" in query or "exit" in query or "go offline" in query or "bye jarvis" in query or "goodbye" in query or "jarvis bye" in query:
            farewell = goodbye_based_on_time() 
            say(f"{farewell} sir. JARVIS going offline.")
            sys.exit()
        else :
            continue