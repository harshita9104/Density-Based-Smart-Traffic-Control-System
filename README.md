# Density Based Smart Traffic Control System

The system described effectively captures traffic density, analyzes lane data, and optimizes time allocation based on real-time and historical information. 

It emphasizes the significance of the density-based smart traffic control system by continuously adapting to changing traffic conditions, the system aims to improve overall traffic flow efficiency and minimize congestion at intersection

Image Preprocessing for Edge Detection:

Grayscale Conversion: RGB images are transformed into grayscale to simplify processing . Grayscale images offer better signal-to-noise ratio for analysis. Conversion involves computing weighted average of RGB values.

Weighted Average Calculation: The weighted average method considers the dominance of the green component in perceived brightness. The formula used is I=0.3R+0.59G+0.11B.

Gaussian Filtering: Gaussian noise, is removed using a Gaussian filter. This filtering step is crucial to prevent noise from being misidentified as edges during edge detection.

Edge Detection:
Canny Edge Detection:
Algorithm Application: Canny edge detection algorithm is applied to identify vehicle edges effectively while suppressing noise and irrelevant details.

Non-maximum Suppression: Keeps only the most important edges by comparing each edge pixel with its neighbors after thresholding.

Conversion to Binary Images: Detected edges are converted into binary images where each pixel is either black (0) or white (1), indicating the presence of edges.

Traffic Density Measurement: The number of white pixels (representing edges) in each image are calculated to compare traffic density across images of different roads

Capture Traffic Density:
   The system records the traffic density when the green light is active.
Comparing Lane Data:
   It gathers and analyzes data from all roads separately.
Allocation of Time:
   Using the collected data from all roads, the system compares current traffic density with historical patterns.
   Time is then allocated to each road based on this comparison, ensuring that roads with higher traffic density receive more time.
Optimization:
   The system continuously adjusts the allocation of time for each road based on real-time data and patterns
