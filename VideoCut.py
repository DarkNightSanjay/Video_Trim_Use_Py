import cv2

def cut_video(input_path, output_path, start_time, end_time):
    # Open the video file
    video = cv2.VideoCapture(input_path)
    if not video.isOpened():
        print(f"Error: Could not open video file {input_path}")
        return
    
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)
    
    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*'XVID'),
        fps,
        (frame_width, frame_height)
    )
    
    current_frame = 0
    frames_written = 0
    while True:
        ret, frame = video.read()
        if not ret:
            print("End of video or error reading frame")
            break

        if start_frame <= current_frame <= end_frame:
            out.write(frame)
            frames_written += 1
        
        current_frame += 1
        if current_frame > end_frame:
            break
    
    video.release()
    out.release()
    print(f"Cut video saved at {output_path}")
    print(f"Total frames written: {frames_written}")

# Example usage:
input_path = r"C:\Users\4a Freeboard\Videos\AnyDesk\demovedio.mp4"
output_path = "C:\Users\4a Freeboard\Videos\AnyDesk\demovedio.mp4"
start_time = 0
end_time = 10

cut_video(input_path, output_path, start_time, end_time)