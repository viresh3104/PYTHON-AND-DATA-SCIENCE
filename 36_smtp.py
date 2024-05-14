import smtplib

hostname = "smtp.gmail.com"
email = "vireshnavtake.cloud@gmail.com"
password = "osskhcbaonvvyflo"

with smtplib.SMTP(host=hostname) as connect:
    connect.starttls()  # Sec
    connect.login(user = email, password = password)
    connect.sendmail(
        from_addr = email,
        to_addrs= "srushti.bhosale.ai@ghrcem.raisoni.net , sapananavtake27@gmail.com",
        msg=f"subject : hi i am viresh , i sent this mail by using python along with smtplib \n\n thats set , inform me if this mail is recived or not"
    )


    # "srushtibhosle04@gmail.com"
    # "srushti.bhosle.ai@ghrcem.raisoni.net"