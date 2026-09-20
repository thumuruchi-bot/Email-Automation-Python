import smtplib

sender_email = "sender@example.com"
receiver_email = "receiver@example.com"
message = "Subject: Test Mail\n\nHello from Python!"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender_email, "your_password")

server.sendmail(sender_email, receiver_email, message)

server.quit()

print("Email Sent Successfully")
