# Simple Python Command-Line Music Player

A basic music player that runs in your terminal, built using Python, Pygame, and Mutagen. It allows you to play, pause, resume, stop music files, and view track information.

## Features

*   **Play Music:** Load and play audio files (supports formats like MP3, WAV, OGG handled by Pygame).
*   **Playback Control:** Pause, resume, and stop the currently playing track.
*   **Track Information:** Display the filename, duration (for MP3s), file path, and current playback status.
*   **Command-Line Interface:** Interact with the player using simple text commands.
*   **Help Menu:** Displays available commands.

## Prerequisites

*   Python 3.x
*   `pip` (Python package installer)

## Installation

1.  **Clone the repository (or download the script):**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    # or just download the .py file
    ```

2.  **Install required libraries:**
    It's recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```
    Then install the packages:
    ```bash
    pip install pygame mutagen
    ```

## Usage

1.  **Navigate to the directory** containing the script (`your_script_name.py` - replace with the actual filename).
2.  **Run the script** from your terminal:
    ```bash
    python your_script_name.py
    ```
3.  The player will start and display the help menu.
4.  **Enter commands** at the prompt:

    *   `play`: Prompts you to enter the full path to a music file. Loads and starts playing the file.
    *   `pause`: Pauses the currently playing track.
    *   `resume`: Resumes playback if the track was paused.
    *   `stop`: Stops the current track completely.
    *   `info`: Shows information about the currently loaded track (filename, duration, path, status).
    *   `help`: Displays the list of available commands again.
    *   `exit`: Quits the music player application.    

