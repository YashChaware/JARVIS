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
    print("Please enter your OpenAI API key, or press Enter if you don't have one:")

    api_key = input().strip()  # Get the API key from the user or empty string if they press Enter
    
    if not api_key:
        print("You don't have an API key. Please generate one at the following link:")
        api_key_url = "https://platform.openai.com/account/api-keys"
        print(f"Ctrl+Click to open: {api_key_url}")
        
        # Automatically open the API key generation page in the browser
        webbrowser.open(api_key_url)
        
        # Wait for the user to generate the API key
        input("Press Enter after you generate your API key and are ready to paste it here.")
        
        # Prompt the user to input the newly generated API key
        print("Please enter your OpenAI API key:")
        api_key = input().strip()

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
