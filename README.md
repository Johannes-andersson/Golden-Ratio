# Golden-Ratio
Golden Ratio Tone Generator
This Python script generates and plays tones based on the golden ratio sequence using Pygame.

Requirements
Python 3.x
Pygame library (pip install pygame)
Usage
Ensure Python and Pygame are installed on your system.
Run the script golden_ratio_tones.py.
Functionality
Tone Generation: Generates sine wave tones based on frequencies derived from the golden ratio sequence.
Playback: Uses Pygame's sound capabilities to play generated tones.
Golden Ratio Sequence: Continuously generates numbers based on the golden ratio (1, 1, 2, 3, 5, 8, ...).
Mapping to Frequency: Maps generated numbers to audible frequencies within a specified range.
Loop: Infinite loop to continuously play tones until interrupted by the user (Ctrl + C).
File Structure
golden_ratio_tones.py: Main script file containing the tone generation and playback logic.
Usage Notes
Adjust the map_to_frequency function parameters (base_freq, max_freq, etc.) for different audible ranges or tones.
Press Ctrl + C in the terminal to stop the program and quit Pygame.
Authors
Johan 
