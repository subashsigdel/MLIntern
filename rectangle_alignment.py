import cv2
import numpy as np

def align_rectangles(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to create a binary image
    _, thresholded = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    # Iterate through the detected contours (rectangles)
    for contour in contours:
        # Skip small contours
        if cv2.contourArea(contour) < 1000:
            continue
        print(contour)
        # Fit a rotated bounding box around the contour
        rect = cv2.minAreaRect(contour)
        print(rect)
        box = cv2.boxPoints(rect)
        box = np.intp(box)  # Use np.intp instead of np.int0
        
        # Calculate the rotation matrix to straighten the rectangle
        angle = rect[-1]
        rotation_matrix = cv2.getRotationMatrix2D(tuple(rect[0]), angle, 0.3)
        
        # Warp the rotated image to align the rectangle
        aligned_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        
        # Display or save the aligned image
    cv2.imwrite("straightimage.jpg",aligned_image)
    
    cv2.destroyAllWindows()

# Replace 'image_path' with the actual path to your image
image_path = 'blob.jpeg'
align_rectangles(image_path)
