import cv2
import numpy as np

# Load the image
image = cv2.imread('/home/subash/Downloads/MLIntern/blob.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform edge detection
edges = cv2.Canny(gray, threshold1=50, threshold2=150)

# Perform Hough Line Transform
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=10, maxLineGap=5)

# Create a dictionary to store line lengths
line_lengths = {}

# Calculate and store lengths of lines
for idx, line in enumerate(lines):
    x1, y1, x2, y2 = line[0]
    length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    line_lengths[idx] = length


# Assign line numbers based on length
numbering = {}
for idx, length in line_lengths.items():
    number = min(4, int(length / 50) + 1)  # Assign numbers 1 to 4 based on length
    numbering[idx] = number

# Draw line numbers on the image for visualization
for idx, line in enumerate(lines):
    x1, y1, x2, y2 = line[0]
    cv2.putText(image, str(numbering[idx]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)




cv2.imwrite("numberedd3.jpg",image)