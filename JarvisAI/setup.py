import os
import subprocess
import webbrowser
import time

# Function to install required dependencies
def install_requirements():
    print("Installing required libraries...")
    try:
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("All dependencies installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing dependencies: {e}")
        exit(1)

# Function to create api_key.py with the user's API key
def create_api_key_file():
    print("If you don't have an OpenAI API key, please generate one here:")
    api_key_url = "https://platform.openai.com/account/api-keys"
    print(f"Ctrl+Click to open: {api_key_url}")
    
    # Automatically open the API key generation page in the browser
    webbrowser.open(api_key_url)
    
    # Delay to allow the user time to visit the webpage
    print("Waiting for you to generate your API key. Please paste it below when ready.")
    time.sleep(5)  # This gives the user a few seconds to focus on the web page
    
    # Ask the user to input their API key after they generate it
    print("Please enter your OpenAI API key:")
    api_key = input()  # Get the API key from the user
    
    # Create or overwrite the api_key.py file with the provided API key
    with open("api_key.py", "w") as f:
        f.write(f'apikey = "{api_key}"\n')
    print("API key saved in 'api_key.py'.")

# Main setup function
def setup():
    install_requirements()  # Install dependencies
    create_api_key_file()  # Create api_key.py with the user's API key

if __name__ == "__main__":
    setup()
