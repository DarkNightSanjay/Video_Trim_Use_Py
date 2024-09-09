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

input_path = r"C:\Users\4a Freeboard\Videos\AnyDesk\demovedio.mp4"
output_path = r"C:\Users\4a Freeboard\Videos\AnyDesk\output_video.mp4"
start_time = 0   # Start time in seconds
end_time = 10    # End time in seconds

cut_video(input_path, output_path, start_time, end_time)



