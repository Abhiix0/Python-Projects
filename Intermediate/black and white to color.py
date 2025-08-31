import cv2

# Load the B&W image
img = cv2.imread('bw_image.jpg', 0)
colorized = cv2.applyColorMap(img, cv2.COLORMAP_JET)
cv2.imwrite('colorized_image.jpg', colorized)
