from flask import render_template, request, url_for, flash, redirect
from app import app, yag
import traceback

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if not name or not email or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))

        subject = 'Contact Form Submission'
        body = f'Name: {name}\nEmail: {email}\nMessage:\n{message}'
        try:
            email_user = "omartra069@gmail.com"
            yag.send(to=email_user, subject=subject, contents=body)
            flash('Email sent successfully')
            print('Email sent successfully')
            return redirect(url_for('index'))
        except Exception as e:
            traceback.print_exc()
            flash('Failed to send email')
        
    
    return render_template('index.html')

