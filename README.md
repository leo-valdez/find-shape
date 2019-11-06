Image Recognition is used in many fields now a days like, Face unlock in phone, Number plate number detection for drivers breaking rules(using picture of number plate captured by speed camera, etc.), etc.

Developing my knowledge in this field I came across:
https://pythonprogramming.net/image-recognition-python/

This repository conatains prediction of image using pillow.The images used are digits and some shapes.
What I learned from understanding and implementing this code is:

1) First we collect the data.

2)Understand how the image data would look if ploted.

3) Convert the image into pixel array form.

4)Thresholding of the image in data collected, i.e converting image to greyscale based on:
    
    Initial threshold value, typically the mean 8-bit value of the original image
    
    Divide image into 2 parts:
    
    Pixel values that are less than or equal to the threshold; background
    
    Pixel values greater than the threshold; foreground
   
5)Find the average mean values of the two new images.Calculate the new threshold by averaging the two means.
                                                                  
    If the difference between the previous threshold value and the new threshold value are below a specified limit, you are finished.  
    Otherwise apply the new threshold to the original image keep trying.
6) Training of data
 
7) Testing of data.

8) Ploting predction graph of the output.


  
