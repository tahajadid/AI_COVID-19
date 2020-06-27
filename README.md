# AI_COVID-19

Wearing a face mask is certainly not an iron-clad guarantee that you won’t get sick – viruses can also transmit through the eyes and tiny viral particles, known as aerosols, can penetrate masks. However, masks are effective at capturing droplets, which is a main transmission route of coronavirus, and some studies have estimated a roughly fivefold protection versus no barrier alone (although others have found lower levels of effectiveness). So why not using the Cameras in our supermarkets just for reminding people to put the mask on their faces.  This is a solution that can help the supermarkets or maybe the government. It based on an Artificial_Intelligence Algorithm using OpenCV

I've Make a video to show you a test of this project
You can find it into my Youtube channel, and you can visit by cliking on the following Link :
  
  https://www.youtube.com/watch?v=3QPOokDPNdc


Use :

1. __YOU NEED to download the file "shape_predictor_68_face_landmarks.dat" in the Link__ : 

  https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/shape_predictor_68_face_landmarks.dat

2. __For more information about this library you can visit the following Link : 
  
  https://www.pyimagesearch.com/2017/04/24/eye-blink-detection-opencv-python-dlib/
  
3. __You need aldo to have OpenCV Library, it's simple to download it with some command line, this is the official website of OpenCV :
  
  https://www.learnopencv.com/install-opencv-3-4-4-on-ubuntu-16-04/
  
*I've 16.04 Ubuntu Version but it can work on the last version of Ubuntu 

4. __After all you just need to put in the same Folder that's mean the three files :

  "haarcascade_frontalface_alt2.xml"
  "shape_predictor_68_face_landmarks.dat"
  "MaskDetect.py"
 
5. __Go into your folder and open the Terminal

6. __Put the following command to Start the Magic 
 
 ==> python MaskDetect.py --shape-predictor shape_predictor_68_face_landmarks.dat
