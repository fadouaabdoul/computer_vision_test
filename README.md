# Computer Vision  Detection and Tracking

## 1. Project Overview

This project creating a model to detect and track cars in a short video of roads.

The main objectives were: 

- Detect object in the video.
- Track the objects across frames.
- Management of the Region of Interest (ROI). 
- Maintain stable Track IDs.
- Analyze tracking behavior and failure cases:

        - ID switches. 
        - Lighting variation. 
        - Degraded video quality. 
        - Crossing or override detection between multiple objects. 
        - tracking loss and recovery. 

### Current pipeline
``` text
Input Video
    |
    v
OpenCV Video Loading
    |
    v
YOLO Vehicle Detection
    |
    v
ByteTrack Multi-Object Tracking
    |
    v
Car ID + Bounding Box + Confidence
    |
    v
Output Video
```
### Project Structure

Project structure is:

``` text
computer_vision_test/
├── configs/
│   └── bytetrack_custom.yaml
├── Detections/
│   ├── __init__.py
│   └── car_detection.py
├── input_video/
│   └── input_cars_video.mp4
├── notebooks/
│   └── ppt/
├── output_video/
│   ├── outputs_metrics/
│   └── output_video.avi
├── tracker_stubs/
│   └── __init__.py
├── utils/
│   ├── __init__.py
│   ├── track_analysis.py
│   └── video_utils.py
├── main.py
├── README.md
├── requirements.txt
```
# 2. Installation
## Clone the repository
``` bash
git clone https://github.com/fadouaabdoul/computer_vision_test.git
cd computer-vision-test
```
``` bash
pip install -r requirements.txt
```

The path is currently configured in `main.py`

The project currently uses:

``` text
yolo26n.pt
```

### Running the Project

From the project root:

``` bash
python main.py
```

## 3. Reproducibility

For reproducibility:

-   Python dependencies are pinned in `requirements.txt`.
-   ByteTrack parameters are stored in `configs/bytetrack_custom.yaml`.
-   The input video path is explicitly configured.
-   The YOLO model is explicitly specified.
-   The original video FPS is preserved when saving the output.
-   Detection/tracking data can be cached using the detection stub
    mechanism.
