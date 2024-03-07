#include <iostream>
#include "opencv2/opencv.hpp"

using namespace std;
using namespace cv;

VideoCapture webCam(1);
Mat img;

vector<vector<int>> colours {{129,179,20,255,255,255},
                             {33,169,16,133,255,137}}; // Colours initiated

vector<Scalar> colourValues {{0, 0, 255}, {0, 255, 0}};

vector<vector<int>> points;

Mat imgToBeIdentified, mask;

Point getContours(Mat imgDilated) {

    vector<vector<Point>> contours;
    vector<Vec4i> hierarchy;

    findContours(imgDilated, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);

    vector<vector<Point>> contoursPoly(contours.size());
    vector<Rect> boundRectangles(contours.size());

    Point point(0, 0);

    for (int i = 0; i < contours.size(); i++) {

        int area = contourArea(contours[i]);

        string objType;

        if (area > 1000) {

            float perimeter = arcLength(contours[i], true);
            approxPolyDP(contours[i], contoursPoly[i], 0.02 * perimeter, true);

            boundRectangles[i] = boundingRect(contoursPoly[i]);

            point.x = boundRectangles[i].x + boundRectangles[i].width / 2;
            point.y = boundRectangles[i].y;


            drawContours(img, contoursPoly, i, Scalar(255, 0, 255), 2);
            rectangle(img, boundRectangles[i].tl(), boundRectangles[i].br(), Scalar(0, 255, 0), 5);
        }
    }

    return point;
}

vector<vector<int>> findColour() {

    cvtColor(img, imgToBeIdentified, COLOR_BGR2HSV);

    for (int i = 0; i < colours.size(); i ++)
    {
        Scalar lower(colours[i][0], colours[i][1], colours[i][2]);
        Scalar upper(colours[i][3], colours[i][4], colours[i][5]);

        inRange(imgToBeIdentified, lower, upper, mask);

        Point point = getContours(mask);

        if (point.x != 0 && point.y != 0) {
            points.push_back({point.x, point.y, i});
        }
    }

    return points;
}

void draw() {
    for (auto & point : points) {
        circle(img, Point(point[0], point[1]), 10, colourValues[point[2]], FILLED);
    }
}

int main() {

    while (true) {

        webCam.read(img);
        flip(img, img, 1);

        points = findColour();
        draw();

        imshow("AI Virtual Painter", img);
        waitKey(1);
    }

    return 0;
}