import cv2

img = cv2.imread('C:/Users/Ahmad Karim/OneDrive/Desktop/python code/pic1.jpeg')
print("Total number of rows and columns:",img.shape)
print("total number of pixels",img.size)

cv2.imshow('image name',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# /////////////////////


from matplotlib import pyplot as py  

py.imshow(img)
py.show()












# import cv2

# Load an image using 'imread'
# image_path = r"C:\Users\Ahmad Karim\OneDrive\Desktop\python code\pic1.jpg"  # Use raw string literal to handle backslashes
# pic1 = cv2.imread(image_path)

# # Check if the image was successfully loaded
# if pic1 is None:
#     print("Error: Could not open or find the image.")
# else:
#     # Print the total number of columns and rows (shape)
#     print("Total number of columns and rows:", pic1.shape)

#     # Print the total number of pixels
#     print("Total number of Pixels:", pic1.size)
#     print()

#     # Display the image (Optional, requires a GUI)
#     cv2.imshow('Image', pic1)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     cv2.destroyAllWindows()

# ############################################################################

# import cv2
# import numpy as np

# # Correct path using raw string literal or double backslashes
# image_path = r"C:\Users\Ahmad Karim\OneDrive\Desktop\python code\pic1.jpg"

# # Load the image
# pic1 = cv2.imread(image_path)

# # Check if the image was successfully loaded
# if pic1 is None:
#     print("Error: Could not open or find the image.")
# else:
#     # Print the total number of columns and rows (shape)
#     print("Total number of columns and rows:", pic1.shape)

#     # Print the total number of pixels
#     print("Total number of Pixels:", pic1.size)

#     # Convert to grayscale
#     gray_image = cv2.cvtColor(pic1, cv2.COLOR_BGR2GRAY)

#     # Save the grayscale image
#     gray_image_path = r"C:\Users\Ahmad Karim\OneDrive\Desktop\python code\pic1_gray.jpg"
#     cv2.imwrite(gray_image_path, gray_image)

#     # Print pixel values of a specific region (e.g., top-left 10x10 region)
#     region = gray_image[0:10, 0:10]
#     print("Pixel values of top-left 10x10 region:\n", region)

#     # Display the original image
#     cv2.imshow('Original Image', pic1)

#     # Display the grayscale image
#     cv2.imshow('Grayscale Image', gray_image)

#     # Wait for a key press and close the image windows
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()





    

