import cv2 as cv


inputImage = cv.imread('/Users/meltemballan/Documents/Image_Processing/images/checkershadow_illusion4med.jpg', 1)
retina = cv.bioinspired_Retina.create((inputImage.shape[1], inputImage.shape[0]))
# the retina object is created with default parameters. If you want to read
# the parameters from an external XML file, uncomment the next line
#retina.setup('MyRetinaParameters.xml')
# feed the retina with several frames, in order to reach 'steady' state
for i in range(20):
    retina.run(inputImage)
# get our processed image :)
retinaOut_parvo = retina.getParvo()
# Convert the processed image to grayscale
retinaOut_parvo_gray = cv.cvtColor(retinaOut_parvo, cv.COLOR_BGR2GRAY)

# show the original image 
cv.imshow('image', inputImage)
cv.waitKey(0)
cv.destroyAllWindows()
# show the processed one
cv.imshow('retina parvo out', retinaOut_parvo_gray)
# wait for a key to be pressed and exit
cv.waitKey(0)
cv.destroyAllWindows()
# write the output image on a file
cv.imwrite('/Users/meltemballan/Documents/Image_Processing/images/checker_wc_parvo_gray.png', retinaOut_parvo_gray)