
. Image Pre-processing	5
Figure 4.1.1. Most common steps used in image processing.	6
4.2 Thresholding	6
Listing 4.2.1. Basic Thresholding Logic	6
4.2.1 Global Thresholding: A Fundamental Image Segmentation Technique	7
Listing 4.2.1.1. Background and Foreground Separation with a threshold	8
Figure 4.2.1.1 Original image is downloaded from https://unsplash.com/ by bunting wild photography (bunting-wild-photography-6CRREj0PZL0-unsplash.jpg). Two different thresholding methods, mean and median , are compared.	9
Listing 4.2.1.2  Image thresholding using the mean and median pixel values	9
4.2.2 Local Thresholding: Adaptive Segmentation for Varied Illumination	10
Listing 4.2.2.1 Testing the sigma value for the bird image that is used for global thresholding	12
Figure 4.2.2.1 Original image is downloaded from https://unsplash.com/ by bunting wild photography (bunting-wild-photography-6CRREj0PZL0-unsplash.jpg). Different sigma values tested.	12
Listing 4.2.2.2 Simple implementation of Gaussian Filter on a picture downloaded from https://unsplash.com/@libraryofcongress	12
Figure 4.2.2.2 Original image is downloaded from https://unsplash.com/ by library of congress archive, named library-of-congress-t5fqtwIn9HQ-unsplash.jpg.	13
Listing 4.2.2.3  Gaussian, block-based, and window-based adaptive thresholding techniques to a grayscale image for segmentation, reducing noise with a Gaussian blur, and displaying the original and thresholded images for comparison.	14
4.2.3 Histograms: Image Intensity Distributions	16
Listing 4.2.3.1 Image Density Distributions (histograms) on original image and thresholded images.	17
Figure 4.2.3.1. Histogram values for original image and thresholded images. The red line in the histogram represents the threshold value used in the simple global thresholding (T=127).	19
Figure 4.2.3.2. Logarithmic histogram for an image with a high dynamic range, where a significant portion of pixels might have low intensity values from https://unsplash.com/ and named as shubham-dhage-qn6LgQnxXAI-unsplash.jpg.	19
4.2.4  Otsu Thresholding: An Automated Approach to Image Segmentation	20
Listing 4.2.4.1. Implementation of adaptive Otsu thresholding.	21
Figure 4.2.4.1. Adaptive Otsu Threshold to separate high and low intensity pixel values to highlight edges.	22
4.2.5 Gradient-Based Adaptive Thresholding: A Robust Approach for Image Segmentation	22
Listing 4.2.5.1. Gradient-based Thresholding with 5x5 Sobel and Prewitt kernels [2].	24
Figure 4.2.5.1. Output of Listing 4.2.5.1 comparing the effects of Sobel and Prewitt operations on Gradient-based Thresholding.	26
4.2.6 Clipping: Effective and Simple Approach Thresholding for Contrast Enhancement	27
Figure 4.2.6.1 Different window sizes for clipping. Listing 4.1.1.6.1 is used to show the effects of clipping algorithms. In this algorithm mean value is used for thresholding.	28
Listing 4.2.6.1. Sample Clipping python code	28
4.2.7 Choosing the Right Thresholding Algorithm	29
4.3 Image Enhancement	30
4.3.1 Contrast Enhancement	30
Listing 4.3.1.1. Comparison of Histogram Equalizer and Contrast Stretching for Contrast Enhancement	31
Listing 4.3.1.2 Contrast Limited Adaptive Histogram Equalization (CLAHE)	32
Listing 4.3.1.3.Contrast stretching by using Percentile Method	32
4.3.2 Noise Reduction	33
Listing 4.3.2.1.. An example for Noise Reduction algorithms on a complex layer image	34
Figure 4.3.2.1. Noise Reduction Examples	35
4.3.3 Sharpening	36
Listing 4.3.3.1 An example for Laplacian Filter with image blurring	36
Figure 4.3.3.1. Laplacian Sharpening after blurring to extract edges.	37
Listing 4.3.3.2 High boost filtering python snippet	37
4.3.4 Color Balancing	38
Figure 4.3.4.1. Color balancing with CLAHE technique	39
Listing 4.3.4.1. Color Balancing code	39
Listing 4.3.4.2 Gray World Assumption Code Snippet	40
4.4 Image Smoothing	40
Table 4.4.1. Comparison between image enhancement and smoothing	41
Figure 4.4.1. Different blurring techniques applied on a color image.	42
Listing 4.4.1 Implementation of different smoothing, blurring, algorithms	42
Figure 4.4.2. Fast Fourier Transformation for Blurring with low-pass and high-pass filters, respectively.	44
Listing 4.4.2. Low-pass filter and High-pass filter code snippet to show effects of Fourier Transformation on a layered image	44
Listing 4.4.3 Homomorphic filtering using Fourier transform	45
Figure 4.4.3. Focused edges are smoothed with homomorphic filter using Fourier Transform	46
Listing 4.4.4. Homomorphic filtering with Gaussian Filter	47
Figure 4.4.4. Improved result for Homomorphic Filtering using a Gaussian filters	48
4.5 Edge Detection	48
4.5.1 Canny Edge Detector	49
Figure 4.5.1.1. Canny Edge detection after homomorphic smoothing using Sobel Operator	50
Listing 4.5.1.1. Canny Edge detection	50
4.5.2 Laplacian of Gaussian (LoG) Operator	51
Listing 4.5.2.1 LoG operation OpenCv example with bilateral filter to reduce the noise	52
Figure 4.5.2.1. LoG operator Edge detection of the cameraman picture	53
4.5.3 Zero-Crossing Approach	54
Listing 4.5.3.1. Zero Crossings overlaid on LoG	54
Figure 4.5.3.1. Zero Crossings Overlayed on LoG	55
4.5.4 Choosing the Edge Detection Algorithm	55
4.6 Morphology	56
4.6.1 Dilation	57
Listing 4.6.1.1 Dilation of a plant and removing the bug	57
Figure 4.6.1.1 Dilation and removing the details	59
4.6.2 Erosion	59
Listing 4.6.1.1 Erosion in comparison to Dilation	59
Figure 4.6.2.1 Erosion to separate bug from the plant	60
4.6.3 Opening	60
Listing 4.6.3.1 Comparison of erosion, dilation and opening for a different image	61
Figure 4.6.3.1 Opening Examples. First examples shows the bug separation and the second is the recovering of the broken glass and noise reduction with Morphology.	62
4.6.4 Closing	62
Listing 4.6.4.1 Comparison of erosion, dilation and opening for a different image	62
Figure 4.6.4.1 Closing Examples generated by closed_image = cv2.erode(dilated_image, structuring_element, iterations=1)	63
4.6.5 Advanced Morphology Operations	63
Hit-Miss Transform	63
Listing 4.6.5.1. Hit-Miss Operation on a complex image	64
Figure 4.6.5.1 Hit-Miss Operation on a complex image	65
Thinning	65
Thickening	66
Listing 4.6.5.2 Code Snippet for Thickening	66
Medial Axis Transform	66
Listing 4.6.5.3 MAT Transform to show effects on cancer cells	67
Figure 4.6.5.2 MAT operation in Cancer Cells	68
4.7 Summary	68
4.8 References	69
