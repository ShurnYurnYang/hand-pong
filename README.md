# Computer Vision (CV) Pong
CV Pong is a recreation of the classic game 'Pong' on the OpenCV platform. CV Pong seeks to use hand tracking to replace the classic paddles in Pong and bring a new level of interaction to the player. CV Pong leverages the OpenCV library and pre-trained MediaPipe models to perform hand tracking. CV Pong represents a fun and interesting experiment into the application of computer vision to Human-Computer Interaction (HCI).

## Project Features
- Hand tracking for two hands (players) using the MediaPipe Landmarker model
- Draws a virtual hand skeleton based on landmark data from the computer vision system
- Optimized for continuous tracking of fast hand movements 
- Maintains relatively high landmark accuracy confidence throughout various hand/finger movements
- Accurate hand-ball collision detection using hand skeleton and landmarks
- Closely simulates original Pong ball physics and interaction
- Implements classic Pong game mechanics

## Examples
### Single-hand landmark detection and skeleton drawing
![box](examples/single-hand-tracking.gif)
### Two-hand landmark detection and skeleton drawing
![box](examples/two-hand-tracking.gif)
### Two-player game condition hand tracking
![box](examples/two-hand-tracking-game.gif)
### Full gameplay
![box](examples/gameplay.gif)
