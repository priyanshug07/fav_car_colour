# fav_car_colour
Using openCV, hadoop HDFS and basics of ML predicting Bangalore's Favorite car Colour.

-A image processing project in which multiple images of bangalore's traffic were clicked with each image containing multiple cars. OpenCV was first used to separate the car from the background and then with k- means cluster algorithm to pick out the dominant colour from the cropped image of the car which is infact the colour of the car. Simaliar colours from different images are first mapped to their respective colour using the mapper function and the the reducer program is run to find the total number of cars belonging to a particular colour across all images.

# Requirements

open cv2
python 2.7+
anaconda
hadoop Hdfs

# Instructions
1. TO IDENTIFY AND EXTRACT ALL THE IMAGES OF THE CAR FROM THE IMAGE AND IDENTIFY THE COLOUR DOMINANCE (with plotting a graph based on probability of colour)
 -> python3 removal.py
 
 IF RUNNING ON HADOOP THEN ALL THE IMAGES SHOULD BE ENCODED IN A TEXT FILE -
 -> python3 encoder.py
 
 2.TO map different colours from all tghe images and reduce similar outputs across all the images -
 -> python3 mapper.py
 
 -> python3 reducer.py
 
 # NOTE
 make sure anaconda with opencv2 library is installed on the system correctly and anaconda session is active.
