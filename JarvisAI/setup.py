import os
import subprocess

# Function to install required dependencies
def install_requirements():
    print("Installing required libraries...")
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("All dependencies installed.")

# Function to create api_key.py with the user's API key
def create_api_key_file():
    print("Please enter your OpenAI API key:")

    # Ask if the user has an API key
    api_key = input("If you don't have an API key, you can get one here: https://beta.openai.com/signup/\nEnter your API key (or press Enter to visit the link): ")
    
    if not api_key:  # If the user doesn't have an API key, guide them to the link
        print("Please visit the following link to generate your API key:")
        print("https://beta.openai.com/signup/")
        return  # Return and exit the function if no API key is provided
    
    # If the user provided the API key, save it to the file
    with open("api_key.py", "w") as f:
        f.write(f'apikey = "{api_key}"\n')
    print("API key saved in 'api_key.py'.")

# Main setup function
def setup():
    install_requirements()  # Install dependencies
    create_api_key_file()  # Create api_key.py with the user's API key

if __name__ == "__main__":
    setup()
