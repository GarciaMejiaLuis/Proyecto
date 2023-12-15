from flask import Blueprint, render_template
from flask import request
from .models import db, Persona

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/formulario')
def formulario():
    return render_template('formulario.html')


@main.route('/iniciarSesion')
def iniciarSesion():
    return render_template('iniciarSesion.html')

@main.route('/submit_form', methods=['POST'])
def submit_form():
    nombre=request.form.get('nombre')
    apellido=request.form.get('apellido')
    email=request.form.get('email')

    email = request.form.get('email')
    nickname = request.form.get('nickname')
    contrasena = request.form.get('contrasena')

    # Verificar si el nickname ya existe en la base de datos
    persona_existente = Persona.query.filter_by(email=email).first()

    if persona_existente:
        # El email ya está registrado, mostrar la página de ya_registrado
        return render_template('ya_existe.html')

    else:
        # El nickname no está registrado, agregar la nueva persona a la base de datos
        # Generar salt
        salt = os.urandom(16)
        # Hash de la contraseña con el salt
        contrasena_salted = contrasena.encode('utf-8') + salt
        contrasena_hash = hashlib.pbkdf2_hmac('sha256', contrasena_salted, salt, 100000).hex()

        nueva_persona = Persona(email=email, nickname=nickname, contrasena=contrasena_hash)
        db.session.add(nueva_persona)
        db.session.commit()

        sesion_nueva_persona = PersonaSesion(user_id=nueva_persona.id, contrasena_hash=contrasena_hash, salt=salt)
        db.session.add(sesion_nueva_persona)
        db.session.commit()

        # Redirigir a la página de éxito
        return redirect(url_for('main.exito'))





    nueva_persona=Persona(nombre=nombre,
                          apellido=apellido,
                          email=email)
    db.session.add(nueva_persona)
    db.session.commit()
    

    return render_template('exito.html')    















@main.route('/ver_registros')
def ver_registros():
    personas=Persona.query.all()
    return render_template('ver_registros.html',
                           personas=personas)


#####################para el formuario de buscar vuelos ################################

@main.route('/submit_voleto', methods=['POST'])
def submit_voleto():
    tiempo_viaje=request.form.get('tiempo_viaje')
    fecha_inicio=request.form.get('fecha_inicio')
    fecha_final=request.form.get('fecha_final')
    #precio / filtros

    busqueda=Viaje(tiempo_viaje=tiempo_viaje,
                          fecha_inicio=fecha_inicio,
                          fecha_final=fecha_final)
    db.session.add(Viaje)
    db.session.commit()

    return render_template('exito.html')    

@main.route('/ver_precios')
def ver_precios():
    Viaje=Viaje.query.all()
    return render_template('ver_registros.html',
                           personas=personas)




