from scipy.fftpack import ifftn
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

######################################################################
# Am example image is created
# Explain each line of the code using line comments
im = np.zeros((200, 200))       # defining 200x200 matrix with all values are 0 and they will seen black in gray color map
im[:, 100:200] = im[:, 100:200] + 255   # all values between 100,...,200 columns will be 255 which will seen white in gray color map
plt.figure()    # creating figure of our matrix
plt.imshow(im, plt.cm.gray)     # setting color map to gray
plt.title('Image')      # title is image
plt.show()      # showing the image
# dividing a 200x200 matrix into 2 parts by making 100,...,200. columns' values 255 left side of the image
# created by matrix will be black and right side of the matrix will become white then this image will shown

####################################################################
# Explain each line of the following code block separately
im_fft = np.fft.fft2(im)        # computing 2D fourier transform of im matrix which will be complex array
im_fft = np.fft.fftshift(im_fft)    # shifting zero frequency parts of the matrix to center row of the spectrum
plt.imshow(np.abs(im_fft), plt.cm.gray)  # displaying image with absolute value of shifted im matrix and setting color map to gray
plt.title('FT of the image')    # setting title of the plotted image
plt.show()      # displaying image

# Explain image of fourier transfom. Why did you get such an image?
"""
Result of the shifting fourier transform of im matrix, zero freq. components which are DC components will shifted to center of the spectrum thus,
output image's center which is in 100. row (half of the matrix), more brighter than the other parts and this will be magnitude spectrum of the matrix which shows low freq. parts more.
"""

################################################################
# Another example image is created
# Explain each line of the code using line comments
im = np.zeros((200, 200))       # creating 200x200 matrix with its values are 0 and they will seen black in gray color map
im[100:200, :] = im[100:200, :] + 255    # all values between 100,...,200 rows will be 255 which will seen white in gray color map
plt.figure()        # creating figure 
plt.imshow(im, plt.cm.gray) # displaying matrix image with gray color map
plt.title('Image')      # setting plot title to image 
plt.show()          # showing the image that we created


####################################################################
# Explain each line of the following code block separately
im_fft = np.fft.fft2(im)    # computing 2D fourier transform of im matrix which will be complex array
im_fft = np.fft.fftshift(im_fft)     # shifting zero frequency parts of the matrix to center column which is 100. column of the spectrum
plt.imshow(np.abs(im_fft), plt.cm.gray) # displaying image with absolute value of shifted im matrix and setting color map to gray
plt.title('FT of image')    # setting plot title to FT of image
plt.show()              # displaying the image

# Explain image of fourier transfom. Why did you get such an image?
# Why are there differences between this image and previous image of fft?
"""
Because of the shifting fourier transform of im matrix, zero freq. components which are DC components will shifted to center column (100. column) of the spectrum thus,
output image's center which is in 100.column (half of the matrix), more brighter than the other parts and this will be magnitude spectrum of the matrix

Previous image's matrix is traversed but this image's matrix is divided vertically so, with the fast fourier transform transformed each matrix to complex array
previous matrix's values which are DC components are in first row but this image matrix's DC component values are in first column. Because of this previous image's center row
is brighter than other parts and this image's center column is brighter which shows low freq. contents.
"""

###############################################################
# Explain each line of the following code block separately
im_fft = np.fft.ifftshift(im_fft)  # making an inverse shifting and zero freq. parts again come to the first column 
im = np.fft.ifft2(im_fft)        # finding inverse fast fourier transform of the im matrix
plt.figure()    # creating a figure of our matrix
plt.imshow(im.real, plt.cm.gray)    # displaying our matrix's real parts with the gray colormap
plt.title('IFT of FT of image')     # setting plot title to IFT of FT of image
plt.show()      # displaying figure that we created


###############################################################
# Explain each line of the following code block separately
im_fft = np.fft.fftshift(im_fft)   # again shifting DC components of the matrix to center column which is 100. column of the spectrum
im_fft[0:95, :] = 0         # setting all values from 0.row to 95.row(except 95.row) to 0
im_fft[105:199, :] = 0   # setting all values from 105.row to 199.row(except 199.row) to 0
im_fft = np.fft.ifftshift(im_fft)   # making an inverse shifting, only 4 zero freq. components' values are in starting matrix 
im = np.fft.ifft2(im_fft)       # finding inverse fft of the matrix and set their values to im matrix
plt.figure()        # creating figure for im matrix
plt.imshow(im.real, plt.cm.gray)    # taken im matrix's value's real parts into plot and setting color map to gray
plt.title('IFT of filtered FT of image')    # setting title to IFT of filtered FT of image
plt.show()      # displaying created image

# Why do you obtained such an image after previous operation?
"""
Because of making shifted fft of im matrix's 0.row to 95.row and 105.row to 199.row values to 0,
it can be understood that output image's between 95.row and 105.row there is a transition through black to white and also by setting values to 0
in im matrix, matrix's values which are under the 100.row are near 255 but not 255 so in image these values seen as not white but close to white and also for
black values which are on 100.row seen as not black but near the black because its values are near 0.
"""

##########################################################################
# Explain each line of the followinf code block separately
N = 100     # setting N to 100
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')  # creating a 2x3 plot matrix to show plots
xf = np.zeros((N,N))    # defining a xf matrix NxN and setting its values to 0
xf[0, 5] = 1    # xf[0][5] = 1
Z = ifftn(xf)   # 2D inverse discrete FT of xf          
ax1.imshow(xf, cmap=cm.gray)        # for ax1 displaying image of xf matrix
ax4.imshow(np.real(Z), cmap=cm.gray)    # for ax4 displaying image of real values of Z
xf = np.zeros((N, N))       # defining a xf matrix NxN and setting its values to 0
xf[5, 0] = 1        # xf[5][0] = 1
Z = ifftn(xf)       # 2D inverse discrete FT of xf
ax2.imshow(xf, cmap=cm.gray)    # for ax2 displaying image of xf matrix
ax5.imshow(np.real(Z), cmap=cm.gray)     # for ax5 displaying image of real values of Z
xf = np.zeros((N, N))    # defining a xf matrix NxN and setting its values to 0
xf[5, 10] = 1         # xf[5][10] = 1
Z = ifftn(xf)           # 2D inverse discrete FT of xf
ax3.imshow(xf, cmap=cm.gray)      # for ax3 displaying image of xf matrix
ax6.imshow(np.real(Z), cmap=cm.gray)    # for ax6 displaying image of real values of Z
figManager = plt.get_current_fig_manager()  # to maximize plotting window
figManager.full_screen_toggle()     # for full screen window
plt.show()      # displaying images

# Comment about obtained images
"""
Here are three different types of images. 3 images on the top are images that applied inverse fourier transform without phase information 
and 3 images below are phase images. For first image making [0][5]=1 provides for each 10 columns values in matrix,colors on image will changed
and each 10 columns' values will become symmetrical according to first 5 columns' values.
For second image making [5][0]=1 provides for each 10 columns values in matrix,colors on image will changed and each 10 rows' values are symmetrical according to first 5 rows' values.
For third image making [5][10]=1 provides creating a matrix with band limited frequency content. This image is consisted of curves which are white and black and it is the phase shifted version of 
other images.
"""

#######################################################################################
# Explain each line of the following code block separately
N = 100         # setting N to 100
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')  # creating a 2x3 plot matrix to show plots
xf = np.zeros((N,N))       # defining a xf matrix NxN and setting its values to 0
xf[0, 20] = 1    # xf[0][20] = 1
Z = ifftn(xf)       # 2D inverse discrete FT of xf    
ax1.imshow(xf, cmap=cm.gray)          # for ax1 displaying image of xf matrix
ax4.imshow(np.real(Z), cmap=cm.gray)     # for ax4 displaying image of real values of Z
xf = np.zeros((N, N))         # defining a xf matrix NxN and setting its values to 0
xf[20, 0] = 1         # xf[20][0] = 1
Z = ifftn(xf)       # 2D inverse discrete FT of xf
ax2.imshow(xf, cmap=cm.gray)    # for ax2 displaying image of xf matrix
ax5.imshow(np.real(Z), cmap=cm.gray)     # for ax5 displaying image of real values of Z
xf = np.zeros((N, N))   # defining a xf matrix NxN and setting its values to 0
xf[10, 20] = 1        # xf[10][20] = 1
Z = ifftn(xf)       # 2D inverse discrete FT of xf
ax3.imshow(xf, cmap=cm.gray)     # for ax3 displaying image of xf matrix
ax6.imshow(np.real(Z), cmap=cm.gray)     # for ax6 displaying image of real values of Z
figManager = plt.get_current_fig_manager()   # to maximize plotting window
figManager.full_screen_toggle() # for full screen window
plt.show()  # displaying images

# Comment about difference between this image and previous image 

"""
This images are consisted of values that returned inverse discrete fourier transform of arbitrary type sequence 20 but previous images are
consisted of inverse discrete FT of arbitrary type sequence 5 because of that view of these images are different, also because of the sequence 
previous image's value change is rare but in this image value change for each matrix quickly and this image's colors are looking brighter due to sequence and density.
It is understood that this images spatial frequencies are larger and its period is smaller than the previous image by looking both of them.
"""



