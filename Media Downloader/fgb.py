from pytube import YouTube

# Create YouTube object
yt = YouTube("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Get highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download to current folder
stream.download()

print("✅ Download complete.")
