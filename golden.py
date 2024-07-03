import numpy as np
import pygame
import time


pygame.init()

# Function to generate a sine wave tone based on frequency (Hz) and duration (seconds)
def generate_tone(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)  # Reduce volume by multiplying by 0.5
    return tone

# Function to play a tone using pygame
def play_tone(tone, sample_rate=44100):
    
    audio = (tone * 32767).astype(np.int16)
    audio = np.repeat(audio[:, np.newaxis], 2, axis=1) 
    sound = pygame.sndarray.make_sound(audio)
    sound.play()
    time.sleep(len(audio) / sample_rate)    

# Function to generate numbers based on the golden ratio indefinitely
def golden_ratio_sequence():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

# Create a generator for the golden ratio sequence
golden_generator = golden_ratio_sequence()

# Function to map a number to a frequency within a specified range
def map_to_frequency(number, base_freq=220, max_freq=880):
    return base_freq + (number % 100) * ((max_freq - base_freq) / 100)

# Infinite loop to continuously play tones based on the golden ratio
try:
    i = 0
    while True:
        # Get the next number in the golden ratio sequence
        number = next(golden_generator)
        
        # Calculate frequency based on the number, mapped to an audible range
        frequency = map_to_frequency(number)
        duration = 0.5  
        
     
        print(f"Iteration: {i}, Number: {number}, Frequency: {frequency} Hz")
        
        
        tone = generate_tone(frequency, duration)
        play_tone(tone)
        
        
        time.sleep(0.1)
        
        i += 1

except KeyboardInterrupt:
    print("Program stopped by user")
    pygame.quit()  
