import cv2

def load_video(video_path):
    capture = cv2.VideoCapture(video_path)
    fps = capture.get(cv2.CAP_PROP_FPS)
    frames = []

    while True:
        ret, frame = capture.read()
        if not ret:
            break
        frames.append(frame)
    capture.release()
    return frames, fps

def save_video(output_video_frames, output_video_path, fps):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    height, width = output_video_frames[0].shape[:2]
    output = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    for frame in output_video_frames:
        output.write(frame)
    output.release()
