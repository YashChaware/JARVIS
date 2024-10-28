elif " the time" in query:
                    if "24 hour" in query:
                        now, _, time_str_24hr = get_current_date_time()
                        say(f"Sir, the time is {time_str_24hr}")
                    else:
                        now, _, time_str_12hr, _ = get_current_date_time()
                        say(f"Sir, the time is {time_str_12hr}")