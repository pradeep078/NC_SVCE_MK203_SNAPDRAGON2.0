#! C:/Users/Lenovo/AppData/Local/Programs/Python/Python36/python.exe
import face_recognition
import cv2
import os.path


video_capture=cv2.VideoCapture(0)
img_name=input("enter image name:")
if(os.path.exists('C:/Users/Lenovo/Desktop/project/image/'+img_name+'.png')):
     my_image=face_recognition.load_image_file('C:/Users/Lenovo/Desktop/project/image/'+img_name+".png")
     my_encoding=face_recognition.face_encodings(my_image)[0]
     known_face_names=[img_name]
     known_face_encodings=[my_encoding]
     def fun_call():
          print("hello "+img_name)
     def fun_go():
          print("not identified")
     while(1):
          k=cv2.waitKey(1)
          ret,frame=video_capture.read()
          rgb_frame=frame[:,:,::-1]
          face_locations=face_recognition.face_locations(rgb_frame)
          face_encodings=face_recognition.face_encodings(rgb_frame,face_locations)
          for (top,right,bottom,left),face_encodings in zip(face_locations,face_encodings):
                match=face_recognition.compare_faces(known_face_encodings,face_encodings)
                name="unknown"
                if True in match:
                      first_match_index = match.index(True)
                      name = known_face_names[first_match_index]
                      fun_call()
                else:
                    fun_go()
               
                cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),3)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame,name,(left+6,bottom),font,1.0,(0,0,255),1)
          cv2.imshow("Face Recognition",frame)
          cv2.waitKey(1)

     video_capture.release()
     cv2.destroyAllWindows()
else:
   print(img_name+" does not exist")


