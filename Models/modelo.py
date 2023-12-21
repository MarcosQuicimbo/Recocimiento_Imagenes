import cv2
from matplotlib import pyplot as plt

# Read the image
image = cv2.imread('../Images/contorno.jpg')
grises = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Display the image 
cv2.imshow("Imagen original", image)
cv2.imshow("Imagen grises", grises)
cv2.waitKey(0)
cv2.destroyAllWindows()

# _, igora esa variable, ignora la primer variable
tipo_umbral,umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)


cv2.imshow("Imagen umbral", umbral)
