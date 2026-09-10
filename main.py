from utils import load_video, save_video


def main():
    input_video_path = "input_video/input_cars_video.mp4"
    video_frames = load_video(input_video_path)

    save_video(video_frames, output_video_path="output_video/output_video.avi")


if __name__ == "__main__":
    main()

