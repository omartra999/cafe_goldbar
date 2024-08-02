from flask import Flask
import yagmail

app = Flask(__name__)

email_user = "omartra069@gmail.com"
email_password = "vumv wpwy rzbk ipyz"
app.secret_key = 'siqwmdlso'
yag = yagmail.SMTP(email_user, email_password)
from app import routes