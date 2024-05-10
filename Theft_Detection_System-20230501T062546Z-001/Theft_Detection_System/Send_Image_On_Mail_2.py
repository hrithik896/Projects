import smtplib
import imghdr
from email.message import EmailMessage
import cv2
camera = cv2.VideoCapture(0)
i = 0
while i < 10:
    input('Press Enter to capture')
    return_value, image = camera.read()
    cv2.imwrite('opencv.png', image)
    i += 1
    Sender_Email = "jadhav.rahuljadhav.rahul701@gmail.com"
    Reciever_Email = "rahulraspberrypi@gmail.com"
    Password = input('Enter your email account password: ')
    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Check out the new logo" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content('Let me know what you think. Image attached!') 
    with open('opencv.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
del(camera)

