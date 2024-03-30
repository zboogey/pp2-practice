import pygame
import os

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 1200
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set fonts
font = pygame.font.Font(None, 36)

# Specify music directory dynamically based on the script's location
script_dir = os.path.dirname(os.path.realpath("music/music.mp3"))
music_directory = script_dir

# Get list of music files
music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]
current_track_index = 0

# Load and play the first track
pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))

# Function to play music
def play_music():
    pygame.mixer.music.play()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Function to play next track
def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))
    pygame.mixer.music.play()

# Function to play previous track
def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track_index]))
    pygame.mixer.music.play()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                previous_track()

    # Fill the background
    screen.fill(WHITE)

    # Draw text
    text = font.render("Press SPACE to Play/Pause, N for Next Track, P for Previous Track", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
