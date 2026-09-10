from collections import defaultdict


def analyze_tracks(car_detections):

    track_frames = defaultdict(list)

    for frame_idx, frame_detections in enumerate(car_detections):

        for car in frame_detections:

            track_id = car["track_id"]

            if track_id is not None:
                track_frames[track_id].append(frame_idx)

    print(f"Total unique track IDs: {len(track_frames)}")

    track_lengths = []

    for track_id, frames in track_frames.items():

        length = len(frames)
        track_lengths.append(length)

    if track_lengths:

        print(f"Longest track: {max(track_lengths)} frames")
        print(f"Shortest track: {min(track_lengths)} frames")
        print(
            f"Average track length: "
            f"{sum(track_lengths) / len(track_lengths):.2f} frames"
        )

    return track_frames