# AI Virtual Painter

Real-time finger and object painting using advanced computer vision technology with custom hand gestures and customizable colours.
The project has 2 parts:

### Finger Painter
Uses hand detection models/algorithms to let you paint in the real 
world in real-time using your finger. Allows you to change the colour of the ink using hand gestures (thumbs up 
and down) and allows you to erase the text using your fist.
Implemented in Python and uses OpenCV, MediaPipe and NumPy.

### Chroma Painter
Uses object and colour detection models/algorithms to allow you to write in the real world in real-time using an object 
of a particular colour. The colour of the object is the colour of the text.
Implemented in C++ and uses OpenCV.

<img src="https://github.com/Jai0212/AI-Virtual-Painter/assets/86296165/4e552f5c-e403-4f1c-b140-a014d1478a5c" alt="Screenshot" width="1000">
Finger Painter showing the hand tracking and the various colours

## Features
- **Real-Time Painting using your Finger:** Allows you to paint virtually in the real world with almost no latency using
your finger
- **Custom Gestures:** Seamlessly change ink color with intuitive gestures like thumbs up and thumbs down
- **Erasing:** Erase content effortlessly by making a fist gesture
- **Free Movement:** Utilize multi-finger gestures to move around without leaving a trace
- **Painting with Real-World Objects:** Paint with the color of a real-world coloured object, such as a red pen
- **Accurate Real-Time Display:** Real-time updates and precise gesture/object detection for accurate painting on the screen
- **Advanced Detection/Tracking Models:** Accuracy enhanced with specially optimized hand and object detection models/algorithms
- **User-Friendly:** Intuitive gestures with an easy-to-use intuitive interface
- **Expandable:** Ability to expand the project by adding more colours and gestures based on personal preferences


![Screenshot 2024-03-07 at 2 41 44 AM](https://github.com/Jai0212/AI-Virtual-Painter/assets/86296165/d8b75c81-f2fc-4ba2-906a-dd0cebb48415)
Finger Painter showing the erase option when doing the fist gesture

## Technical Aspects
The program was created in CLion using C++ and Python. The libraries used were OpenCV, MediaPipe and NumPy.

### Finger Painter
The computer vision aspect of the project was implemented using OpenCV.
The hand-tracking algorithm was implemented using MediaPipe. The custom gestures
for changing colours and erasing were created from scratch by analysis of the hand 
coordinates.

There are a total of 4 colours in the finger virtual painter (more colours can be added 
by adding the RGB values inside the list). The initial colour is purple. When you do thumbs up or down,
the colour changes. If you indicate a fist, the eraser will toggle. This is done by checking the
particular distance and arrangement of the hand coordinates at each frame for accuracy. 
In case you want to move your hand around (without drawing), you can have more than one finger up.  

All this was accomplished by creating specific functions and analyzing the hand coordinates.

### Chroma Painter
The object detection was achieved with the help of OpenCV.
I first created a colour and object detection model and configured the colours to enable the colour 
detection model to identify the particular colour.

If found, the colour model matches the colour with the set of available colours. With the help of
computer vision object detection, the model detects the object and then draws the particular colour on
the topmost part of the object. This allows you to draw with almost any colour in the real world with the
help of any real object.

### General Note
The webcam image refreshes with every change in movement thereby providing accurate and real time updates based
on the gesture/object movement.

The drawing was imprinted in the real world by inverting the images and performing specific operations
to allow real-time and real-world display of your drawings as if they were floating in the air.

I have left the hand tracking lines and the object detector indicator on for a better understanding of how
the project works.

![Screenshot 2024-03-07 at 2 42 25 AM](https://github.com/Jai0212/AI-Virtual-Painter/assets/86296165/484ec2df-46cb-4e20-bce0-612e27a7fd07)
Chroma Painter showing the object detection and drawing based on colour of object

## Usage and Requirements
The program can be run on any normal laptop with a webcam. To use the project, you can use any IDE that 
supports C++ (3.17) and Python (3.11). You need to download all the files as is.

### Finger Painter
To use this, you need Python and any IDE that runs Python. You will first need to download the packages
opencv-python, mediapipe and numpy. You can do so using the pip install command in the terminal or 
directly from the IDE.

To run the program, in the directory 'Finger_Painter', run the file 'FingerPainter'. The webcam
will open up and you can use the project. Raise your index finger to draw. Close your fist and move it 
around to erase. Make a thumbs up or thumbs down to change the colour. Hold up more than one finger 
to move around the webcam region without drawing.

### Chroma Painter
To use this, you will need C++ and any IDE that runs C++. You will first need to install opencv using
Homebrew (use any online tutorial to learn how to install opencv using Homebrew). You might need to 
change some file locations depending on where your opencv package is saved in the CMakeLists.txt file.

To run the program, run the main.cpp file and the webcam should open up. Take any coloured object, for
example, a red pen/cup/marker or any holdable red item. Using that, you will be able to draw.

### General Note

For better usage of the program, I would recommend standing about 1 meter away from your webcam for
proper hand detection and more screen space to draw. Make sure only one hand is visible to the webcam. 
To stop, you must terminate the program from the IDE.
In case the webcam does not open up when you run the file, try changing the '1' in the line of code
'web_cam = cv.VideoCapture(1)' to 0 or 2. It depends on your laptop and which webcam you want to use.

## Acknowledgement
I worked on this project alone and will not be actively working on the project anymore 
(I will be creating other related projects). However, I would love any suggestions/feedback/collaborative requests.

## Author and Date
by Jai Joshi  
7th March, 2024
