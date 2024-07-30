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
































cv2.destroyAllWindows()