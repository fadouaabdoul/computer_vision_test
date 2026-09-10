import cv2
import pickle
from ultralytics import YOLO


class CarDetection:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_frames(self, frames, read_from_stub=False, stub_path=None):
        car_detections = []
        #to not run the processing all over again
        if read_from_stub and stub_path is not None:
            with open(stub_path, 'rb') as f:
                car_detections = pickle.load(f)
            return car_detections

        for frame in frames:
            car_list = self.detect_frame(frame)
            car_detections.append(car_list)
        #to not run the processing all over again
        if stub_path is not None:
            with open(stub_path, 'wb') as f:
               pickle.dump(car_detections, f)
        return car_detections

    def detect_frame(self, frame):
        #by lowering the conf metric the detection will be less accurate and will detect distant object, blurry ones too
        #the iou helps in crowded scenes, put it high means that the model can tolerate the overlapping boxxes

        results = self.model.track(
            frame,
            persist=True,
            tracker="configs/bytetrack_custom.yaml",
            conf=0.2,
            iou=0.7,
            verbose=False
        )[0]
        id_name_dict = results.names
        car_list = []
        #testing the dimensions of the bbox and printing the confidence metric
        for box in results.boxes:

            cls_id = int(box.cls[0])
            cls_name = id_name_dict[cls_id]

            if cls_name != "car":
                continue

            # Bounding box
            bbox = box.xyxy[0].tolist()

            # Detection confidence
            confidence = float(box.conf[0])

            # Track id
            if box.id is not None:
                track_id = int(box.id[0])
            else:
                track_id = None

            car_list.append({
                "bbox": bbox,
                "confidence": confidence,
                "track_id": track_id
            })


            print(
                f"Car | "
                f"ID={track_id} | "
                f"confidence={confidence:.3f} | "
                f"bbox={bbox}"
            )

        return car_list

    def draw_bounding_box(self, video_frames, car_detections):

        output_video_frames = []

        for frame, car_list in zip(video_frames, car_detections):

            for car in car_list:

                bbox = car["bbox"]
                confidence = car["confidence"]
                track_id = car["track_id"]

                # YOLO format: [x1, y1, x2, y2]
                x1, y1, x2, y2 = bbox

                # Convert to integers ONCE
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)

                # Calculate dimensions
                width = x2 - x1
                height = y2 - y1

                # Debug
                print(
                    f"ID={track_id} | "
                    f"x1={x1}, y1={y1}, "
                    f"x2={x2}, y2={y2} | "
                    f"W={width}, H={height}"
                )

                # Draw EXACTLY those coordinates
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 0, 255),
                    2
                )

                # Display dimensions
                cv2.putText(
                    frame,
                    f"confidence={confidence:.3f}",
                    (x1, max(y1 - 5, 15)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    1
                )

                # Display ID
                cv2.putText(
                    frame,
                    f"ID: {track_id}",
                    (x1, y2 + 15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    1
                )

            output_video_frames.append(frame)

        return output_video_frames