# Calculate the histogram of the original image
hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.subplot(2, 4, 5)
plt.plot(hist_original)
plt.xlabel('Histogram of Original Image')
plt.axvline(x=127, color='r', linestyle='dashed', linewidth=2)

# Add annotations
max_value_original = np.argmax(hist_original)
plt.annotate('Dominant Intensity Values', xy=(max_value_original, hist_original[max_value_original]), xytext=(max_value_original+50, hist_original[max_value_original]+500), 
             arrowprops=dict(facecolor='black', shrink=0.05))