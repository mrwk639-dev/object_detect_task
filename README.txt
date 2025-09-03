this program is written in python using opencv the goal is to load an input image and detect the shapes inside like square rectangle circle or triangle then for each detected shape the program also finds the color by converting the shape area into hsv color space and checking the hue value so it can tell if it is red green or blue

the steps of the code are simple first the image is converted to gray then blurred and edges are detected using canny then contours are extracted for every contour the algorithm checks the number of vertices to decide the shape and builds a mask to calculate the average color inside the shape

the result is an output image where each shape is surrounded by a green contour and labeled with both the shape name and the color
