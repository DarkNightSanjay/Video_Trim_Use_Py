# Video Trim

This project provides a Python script to cut a segment from a video using OpenCV. The user can specify the input video, start time, end time, and the output path for the cut video.

## Features

- Cuts a video from a specified start time to an end time.
- Supports `.mp4` format (or any other format supported by OpenCV).
- Output video is saved in the XVID format.

## Requirements

Ensure you have the following installed:

- Python 3.x
- OpenCV library (`cv2`)

To install OpenCV, run the following command:


    pip install opencv-python
  
## Usage
1. Script Overview
The script contains a function cut_video(input_path, output_path, start_time, end_time) that cuts a video file from the specified start time to the end time.

- input_path: Path to the input video file.
- output_path: Path where the output video will be saved.
- start_time: Start time of the segment to cut (in seconds).
- end_time: End time of the segment to cut (in seconds).
  
## Example 
    input_path = r"C:\Users\4a Freeboard\Videos\AnyDesk\demovedio.mp4"
    output_path = r"C:\Users\4a Freeboard\Videos\AnyDesk\output_video.mp4"
    start_time = 0   # Start time in seconds
    end_time = 10    # End time in seconds
    cut_video(input_path, output_path, start_time, end_time)

  After running the script, you will see the following output in the console:

    Cut video saved at C:\Users\4a Freeboard\Videos\AnyDesk\output_video.mp4
    Total frames written: [Number of frames]

## How It Works
- Open the video: The script uses OpenCV’s VideoCapture to open and read the input video.
- Get frame rate and dimensions: The script extracts the frames per second (FPS) and video dimensions for writing the output file.
- Frame calculation: Based on the start and end times (in seconds), it calculates the respective frame numbers to cut.
- Write output: A VideoWriter object is used to write the frames within the specified time range into a new video file.

## Notes
- The script currently uses the XVID codec for video compression. You can modify this by changing the codec in the VideoWriter object if needed.
- Make sure that the output_path is different from the input_path to avoid overwriting the original video.
