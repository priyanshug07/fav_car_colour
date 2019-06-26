# fav_car_colour
using openCV, hadoop HDFS and basics of ML predicting Bangalore's Favorite car Colour.

-A image processing project in which multiple phon shot pictures of bangalore's traffic is clicked each image containing multiple cars. openCV is used to first separate the car from the background and then with k- means cluster algorithm to pick out the dominant colour of that cropped image of the car which is cosidered to be the colour of the car. simaliar colours from different images are first mapped to their respective colour using the mapper function and the the reducer program is run to find the total number of cars belonging to a particular colour across all images.

# requirements

open cv2
python 2.7+
anaconda
hadoop Hdfs

# instructions
1. TO IDENTIFY AND EXTRACT ALL THE IMAGES OF THE CAR FROM THE IMAGE AND IDENTIFT THE COLOUR DOMINANCE (with plotting a graoh based on probability of colour)
 -> python3 removal.py
 
 IF RUNNING ON HADOOP THEN ALL THE IMAGES SHOULD BE ENCODED IN A TEXT FILE -
 -> python3 encoder.py
 
 2.TO map different colours from all tghe images and reduce similar outputs across all the images -
 -> python3 mapper.py
 
 -> python3 reducer.py
 
 # NOTE
 make sure anaconda with opencv2 library is installed in the system correctly and anaconda session is active.
