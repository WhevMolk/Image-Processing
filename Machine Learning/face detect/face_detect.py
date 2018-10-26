import cv2

casc_path_face = "haarcascade_frontalface_default.xml"
casc_path_left_eye = "haarcascade_lefteye_2splits.xml"
casc_path_smile = "haarcascade_smile.xml"


casc_face = cv2.CascadeClassifier(casc_path_face)
casc_left_eye = cv2.CascadeClassifier(casc_path_left_eye)
casc_smile = cv2.CascadeClassifier(casc_path_smile)


# Start the camera twice to work around 
# "error: ..\..\..\modules\imgproc\src\color.cpp:7456: error: (-215)
# scn == 3 || scn == 4 in function cv::ipp_cvtColor"
camera_capture = cv2.VideoCapture(0)
camera_capture.release()
camera_capture = cv2.VideoCapture(0)

detect_eyes = True
detect_smile = True

while True:
    if not camera_capture.isOpened():
        print('Unable to load camera.')
        break

    # Capture frame-by-frame
    ret, frame = camera_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = casc_face.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30)
    )
    # Draw a rectangle around the faces
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0 ), 2)
    
    if (detect_eyes) :
        eyes = casc_left_eye.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(30, 30)
        )
        # Draw a rectangle around the eyes   
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
    if (detect_smile) :
        smiles = casc_smile.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=350,
            minSize=(40, 40)
        )
        # Draw a rectangle around the eyes   
        for (x, y, w, h) in smiles:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
camera_capture.release()
cv2.destroyAllWindows()