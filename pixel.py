import cv2

path = 'imagePATH/'
input = cv2.imread(path+'b2.jpg')

#print("Shape : ", input.shape[:2])
height, width = input.shape[:2]

w, h = (30, 30)

temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

cv2.imshow('Input', input)
cv2.imshow('Output', output)
cv2.waitKey(0)
