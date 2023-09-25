import yagmail
#import keyring
#import smtplib

#yagmail.register('facerecognitionattendancemrec@gmail.com', 'CS13MREC')

#receiver_email= 'nandhusunkoju@gmail.com'
#print(keyring.get_password("yagmail","facerecognitionattendancemrec@gmail.com"))
#subject= 'I AM HERE'
#sender_password=input(f'Please, enter the password for(sender_email):\n')

yag = yagmail.SMTP('facerecognitionattendancemrec@gmail.com')

yag.send('facerecognitionattendancemrec@gmail.com','ATTENDANCE SUCCESSFUL',
attachments=["E:\projects\Face-Recognition-Attendance-System-master\Face-Recognition-Attendance-System-master\FRAS\Attendance\Attendance_2021-11-24_13-47-33.csv"])

print('Mail sent successful')