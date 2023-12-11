# This repository includes the codes and images that were generated for Image Processing and Generative AI Book by Manning Publications.
# Codes and images will be organized chapter by chapter 
# The layout of the chapter, the codes and images will be listed under each title:
3.1 Human Perception and Its Role in Data Augmentation
3.2 Depth: Shepard Tables Illusion
Figure 3.2.1. Shepard’s Tables created by link 3.2.1.
Listing 3.2.1. Shepard Table starter code to label  perception
3.2.1 Computing the Depth
Figure 3.2.1.1 Stereo Depth. Top left: Illustration of left and right eye vision. Top right: Distortion between two eyes vision. Bottom left: Left Eye vision illusion. Bottom right: Right vision illusion
Listing 3.2.1.1 Stereo vision depth using opencv
3.3 Brightness: Checker shadow illusion
Figure 3.3.1 Checkerboard illusion [5] .
Figure 3.3.2 Checkerboard with a green cylinder. Left: The computational view of checkerboard. Right: Shadow effect with gray cylinder around the green cylinder (listing 3.3.1).
Listing 3.3.1 Representing Light illusion with Python
Figure 3.3.3 Checkerboard illusion  explained in four parts in [6]
Figure 3.3.4 Checkerboard illusion computed by the formula that  Herault Jeanny introduced and image by Edward Adelson
Listing 3.3.2 Benoit and Jeanny OpenCv code for  brain representation of checkerboard
3.4 Distortion: Ames Room
Figure 3.4.1 Ames Room downloaded from [11]
Figure 3.4.2. Ames Room illusion of three people at the same height
As we discussed an Ames room manipulates human perception to create an illusion of size and distance. Listing 3.4.1 shows basic two objects moving on a three 3d plane in a trapezoidal room. Generative AI can manipulate digital perception, creating new data that appears real. For example, a GAN can be trained to generate images that look like real photographs to human observers.
In a more direct application, generative AI can be used to create digital Ames rooms to create movie scenes like Willy Wonka and Lord of the Ring which used manual techniques to create the effect. A GAN could be trained on images of Ames rooms and then generate new ones.
Listing 3.4.1 Representing Ames Room with Moving Objects in a 3D Room
3.5. Motion Illusion: Ego Motion
Listing 3.5.1 Ego Motion to illustrate motion ego with apparent illision
3.6 Manual Image Preparation
Figure 3.6.1 Flow chart of manual labeling process for generating perception.
Listing 3.6.1 Image Annotation Example
Figure 3.6.2 The Mueller & Lyer Illusion, Arrows
3.7 Summary
3.8 References

# Requirements

- Python 3
- OpenCV
- numpy
- json
- PIL/PILLOW
- matplotlib
- retina_parvo extension of OpenCV
- pygame
- os
- glob
  
