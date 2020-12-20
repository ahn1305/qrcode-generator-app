# qr-generator-app

This app was made for generating qrcode.

# What is qrcode?

What is a QR Code?
A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. The code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind of data (e.g., binary, alphanumeric, or Kanji symbols)

---------------------------------------------------------------------------------------------

Before using the app, you need to install the following packages

---------------------------------------------------------------------------------------------

1; Tkinter

2; qrcode

-----------------------------------------------------------------------------------------------

Installation: 

For a standard install (run this if you dont have pillow package), run: pip install qrcode[pil] 

or (if you have pillow installed)

pip install qrcode


for more details, visit this site: https://pypi.org/project/qrcode/

-----------------------------------------------------------------------------------------------

Lets see what are the things inside the **gen_qrcode** function:



The version parameter is an integer from 1 to 40 that controls the size of the QR Code 
(the smallest, version 1, is a 21x21 matrix).

Set to None and use the fit parameter when making the code to determine this automatically.

The box_size parameter controls how many pixels each “box” of the QR code is.

The border parameter controls how many boxes thick the border should be 
(the default is 4, which is the minimum according to the specs).

fill_color and back_color can change the background and the painting color of the QR, 
when using the default image factory.

img.save is for saving the qrcode made inside a png.



----------------------------------------------------------------------------------------------------------------

In case if you get any error, you can contact me

Mail: ahnashwin1305@gmail.com

Dont hesitate to mail me in case if you get any error
