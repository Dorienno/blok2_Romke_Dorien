from flask import Flask, render_template, request
from flask_mysqldb import MySQL 
from email.message import EmailMessage
import mysql.connector
import ssl
import smtplib


app = Flask(__name__)

email_sender = 'ploansystemen@gmail.com'
email_password = 'ccxpsfcrspeblnes'
email_receiver = 'ploansystemen@gmail.com'

# hosten alle agenda
@app.route("/")
def home():
    return render_template("alle-agenda.html")

# hosten log-in scherm
@app.route("/log-in")
def log_in():
    return render_template("log-in.html")

# hosten afwezig agenda
@app.route("/afwezig-agenda")
def afwezig_agenda():
    return render_template("afwezig-agenda.html")

# hosten alle agenda
@app.route("/alle-agenda")
def alle_agenda():
    return render_template("alle-agenda.html")

# hosten overige agenda
@app.route("/overige-agenda")
def overige_agenda():
    return render_template("overige-agenda.html")

# hosten terrein agenda

@app.route("/terrein-agenda")
def terrein_agenda():
    return render_template("terrein-agenda.html")

# hosten vogels agenda
@app.route("/vogels-agenda")
def vogels_agenda():
    return render_template("vogels-agenda.html")

# hosten thank-you pagina
@app.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")

# hosten verlof pagina
@app.route("/verlof", methods=['GET', 'POST'])
def verlof():
    if request.method == "GET":
        return render_template("verlof.html")
    
    # if form post send to email
    if request.method == "POST":
        name = request.form.get('name')
        dateOne = request.form.get('dateOne')
        dateTwo = request.form.get('dateTwo')
        message = request.form.get('reden')
        subject = "Verlof aanvraag"
        body=f"Name: {name}\nVan: {dateOne}\nTot: {dateTwo}\nReden:{message}"
        
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        
    return render_template("thank-you.html")

# hosten support pagina
@app.route("/support", methods=['GET', 'POST'])
def support():
    if request.method == "GET":
        return render_template("support.html")
    
    # if form post send to email
    if request.method == "POST":
        organisatie = request.form.get('organisatie')
        message = request.form.get('message')
        subject = "Support"
        body=f"Organisatie: {organisatie}\nMessage:{message}"
        
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
    
    context = ssl.create_default_context()
    
    # Stuur email. 
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        
    return render_template("thank-you.html")

    
    # hosten new_user html
@app.route("/new-user", methods=["GET", "POST"])
def new_user():
    # connect to database
    mydb = mysql.connector.connect(
    host="oege.ie.hva.nl",
    user="witdcm",
    password="MEVO5MBqeC2f94",
    database="zwitdcm"
    )

    mycursor = mydb.cursor()

    
    if request.method == "GET":
        return render_template("new-user.html")
    
    # Post input form to database. Add new user.
    if request.method == "POST":
        
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        phoneNumber = request.form['phoneNumber']
        cur = mydb.cursor()
        cur.execute("INSERT INTO userInfo (name, email, address, phoneNumber) VALUES (%s, %s, %s, %s)", (name, email, address, phoneNumber))   
        mydb.commit()
           
    print(name)
    return "gelukt"

# blijven runnen. 
if __name__ == "__main__":
    app.run(debug=True)