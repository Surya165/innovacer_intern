import smtplib
import sys
sys.path.append("..")
import config
def sendMail(email,message):
    print("Sent mail to ",email)
    return
    print("starting")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    print("server created")
    server.login(config.EMAIL, config.PASSWORD)
    print("logged in")
    server.sendmail(
      config.EMAIL,
      "dineshpentakota7897@gmail.com",
      "this message is from python")
    print("mail sent")
    server.quit()
    print("Quitting server")
    return
