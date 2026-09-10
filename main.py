from utils import load_video, save_video, analyze_tracks
from Detections import CarDetection

def main():
    input_video_path = "input_video/input_cars_video.mp4"
    video_frames, fps = load_video(input_video_path)

    car_detector = CarDetection(model_path="yolo26n.pt")
    car_detections = car_detector.detect_frames(video_frames, read_from_stub=False, stub_path="tracker_stubs/car_detection.pkl")

    track_frames = analyze_tracks(car_detections)

    output_video_frames = car_detector.draw_bounding_box(video_frames, car_detections)

    save_video(output_video_frames, output_video_path="output_video/output_video.avi", fps=fps)


if __name__ == "__main__":
    main()

