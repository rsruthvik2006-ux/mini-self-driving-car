*Purpose: Handles traditional computer vision preprocessing and lane boundary extraction using OpenCV.*

```python
import cv2
import numpy as np

class LaneDetector:
    def __init__(self):
        pass

    def process_frame(self, frame):
        # 1. Convert to grayscale and blur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # 2. Canny Edge Detection
        edges = cv2.Canny(blur, 50, 150)
        
        # 3. Region of Interest (ROI) Masking
        height, width = edges.shape
        mask = np.zeros_like(edges)
        polygon = np.array([
            [(0, height), (width, height), (width, int(height * 0.6)), (0, int(height * 0.6))]
        ], np.int32)
        cv2.fillPoly(mask, polygon, 255)
        masked_edges = cv2.bitwise_and(edges, mask)
        
        return masked_edges
