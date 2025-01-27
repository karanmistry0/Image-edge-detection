# Edge Detection Script

This Python script is designed for performing edge detection on an image using OpenCV. It applies the Canny edge detection algorithm, followed by dilation and erosion, to process the image and visualize the results.

## Features
- Reads an input image and resizes it to a predefined size.
- Applies the Canny edge detection algorithm.
- Processes the detected edges with dilation and erosion.
- Displays the original, edge-detected, dilated, and eroded images using OpenCV's GUI.

## Requirements
To run this script, you need the following dependencies:
- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Setup Instructions
1. Install Python if it's not already installed on your system. You can download it from [python.org](https://www.python.org/).
2. Install the required Python libraries using pip:
   ```bash
   pip install opencv-python numpy
   ```
3. Place your input image in a directory named `imgs` in the same folder as this script. Rename the image to `happy.jpg`, or modify the `image_path` in the script to match your image file's path and name.

## Usage
1. Run the script by executing the following command in your terminal or command prompt:
   ```bash
   python edge_detection.py
   ```
2. The script will:
   - Load and resize the input image to `747x498`.
   - Detect edges using the Canny edge detection algorithm with thresholds `90` and `150`.
   - Apply dilation with a `5x5` kernel.
   - Apply erosion with a `3x3` kernel.
   - Display the following images in separate windows:
     - Original Image
     - Edge-detected Image (Canny)
     - Dilated Image
     - Eroded Image

## Customization
- **Canny Edge Detection**: Adjust the thresholds for edge detection by modifying:
  ```python
  img_edge = cv2.Canny(img, 90, 150)
  ```
  Replace `90` and `150` with your desired lower and upper thresholds.

- **Kernel Sizes**: Modify the kernel sizes for dilation and erosion by changing:
  ```python
  np.ones((5, 5), dtype=np.uint8)  # For dilation
  np.ones((3, 3), dtype=np.uint8)  # For erosion
  ```
  Replace `(5, 5)` or `(3, 3)` with your desired kernel dimensions.

- **Image Path**: Update the `image_path` variable to use a different image file:
  ```python
  image_path = os.path.join('.', 'imgs', 'your-image.jpg')
  ```

## Notes
- Ensure the input image exists in the specified path and has sufficient resolution for the processing.
- The script uses `cv2.imshow` to display images, which requires a GUI environment. It may not work in a headless setup like some remote servers.


