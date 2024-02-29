import smtplib

sender = "mojmail@gmail.com"
receiver = "mailodbiorcy@gmail.com"     # To wiadomo przetłumacz sobie
password = "okon"
subject = "test mail"
body = "I wrote a mail in python"
                                        # Ta wiadomośc message musi tak wyglądać ale no logiczna jest
message = f"""From:Snop{sender}             
To:Nicholas{receiver}
Subject{subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)        # stawia serwer (zawsze musi tak wyglądać ta zmienna)
server.starttls()                                             # startuje serwer

try:                                                    # try, catch to klasycznie nic do tłumaczenia
    server.login(sender, password)                      # Przekazujemy wystatowanemu serwerowi dane do logowania
    print("Zalogowano do emaila.")
    server.sendmail(sender, receiver, message)          # Serwer wysyła wiadomość (message) do recievera
    print("Wysłano maila.")
except smtplib.SMTPAuthenticationError:                 # te smtplib.STMPAuthe.... to nazwa errora
    print("Podano niewłaściwe dane.")