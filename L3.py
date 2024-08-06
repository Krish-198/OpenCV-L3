import cv2
img=cv2.imread("tomato.png")
cv2.imshow("Original Iamge",img)
cv2.waitKey(0)

grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",grey)
cv2.waitKey(0)

img2=cv2.imread("Image1.jpg")
(row,col) =img2.shape[0:2]
for i in range(row):
    for j in range(col):
        img2[i,j]=sum(img2[i,j])*0.33
cv2.imshow("Blah 1",img2)
cv2.waitKey(0)

b=cv2.getRotationMatrix2D((col/2,row/2),45,1)
r=cv2.warpAffine(img2,b,(col,row))

cv2.imwrite("Image.png",r)
cv2.waitKey(0)


#Edge Dectetion
h=cv2.Canny(img,100,200)
cv2.imwrite("Tomato(2).png",h)
cv2.waitKey(0)


#hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("Gray Image",hsv)
cv2.waitKey(0)


