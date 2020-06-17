"""Web Routes"""
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask import render_template
import src

app = Flask(__name__)
app.secret_key = "mantenimiento y pruebas"

@app.route('/')
def index():
    """Index Web"""
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(e):
    flash("404 Not Found", "error")
    return render_template('home.html'), 404

@app.route('/params/<name>/')
def params(name):
    """Params Web"""
    return 'El parametro es: ' + name


@app.route('/hello')
def hello():
    """Do or do not, there is no try"""
    return 'Hello, World!'

@app.route('/login', methods=["POST", "GET"])
def login():
    """Login Route, {Log out, Log in}"""
    if "patient" in session or "doctor" in session:
        output = redirect(url_for('index'))
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        
        for patient in src.DataFacade.getAllPatients():
            if patient.email == email and patient.password == password:
                session["patient"] = email
                flash("Has iniciado sesión con éxito", "info")
                output = redirect(url_for('index'))
        for doctor in src.DataFacade.getAllDoctors():
             if doctor.email == email and doctor.password == password:
                session["doctor"] = email
                flash("Has iniciado sesión con éxito", "info")
                output = redirect(url_for('index'))
        if not "patient" in session and not "doctor" in session:
            flash("Usuario y/o contraseña incorrecto", "error")
            output = render_template('login.html')
    else:
        output = render_template('login.html')
    return output
    
@app.route('/logout')
def logout():
    session.pop("patient",None)
    session.pop("doctor",None)
    flash("Has cerrado sesión", "error")
    return redirect(url_for('index'))

@app.route('/covid')
def covid():
    return render_template('covid.html')

@app.route('/covid/autotest')
def covid_autotest():
    return render_template('covid_autotest.html')

@app.route('/areaprivada/horario')
def areaprivada_horario():
    output = redirect(url_for('index'))
    if "doctor" in session:
        for doctor in src.DataFacade.getAllDoctors():
            if doctor.email == session["doctor"]:
                output = render_template('doctor.html',doctor=doctor)
    return output

@app.route('/areaprivada/citas', methods=["POST", "GET"])
def areaprivada_citas():
    output = redirect(url_for('index'))
    if "patient" in session:
        for patient in src.DataFacade.getAllPatients():
            if patient.email == session["patient"]:
                if request.method == "POST":
                    day = request.form["day"]
                    time = request.form["time"]
                    for workingDay in patient.doctor.workingDays:
                        if workingDay.__str__() == day:
                            for workingTime in workingDay.workingTimes:
                                print(workingTime.__str__() == time,time,workingTime)
                                if workingTime.__str__() == time:
                                    if patient.appointment_active is not None:
                                        patient.appointment_active.workingTime.appointment = None
                                    appoint = src.Appointment.Appointment(patient,workingTime)                                
                                    patient.appointment_active = appoint
                                    workingTime.appointment = appoint

                output = render_template('appointments.html',patient=patient)
    return output

if __name__ == '__main__':
    app.run(port=80)
