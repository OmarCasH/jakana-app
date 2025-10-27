from flask import Flask, render_template, request, flash, redirect, url_for,session
import json

app = Flask(__name__)
app.secret_key = 'Valeria**'

# --------------- RUTAS --------------------

  #------- PAG PRINCIPAL ---------
  
@app.route ('/')
def home():
  return render_template('index.html') 

  #------- PAG REGISTRO ----------

@app.route ('/registro', methods=['GET','POST'])
def registro():
  
  if request.method == 'POST' :
    
    usuario = request.form.get('usuario').strip().lower()
    email = request.form.get('email').strip().lower()
    contrasena = request.form.get('contrasena').strip()
    telefono = request.form.get('telefono').strip()
    
    try:
      with open ('static/js/usuarios.json', 'r+') as archivo:
        usuarios= json.load(archivo)
        
        for u in usuarios:
          if u['usuario'] == usuario:
            flash('El usuario ya Esta registrado')
            return render_template ('registro.html')
        
        usuarios.append({
          'usuario' : usuario,
          'email' : email,
          'contrasena' : contrasena,
          'telefono' : telefono
        })
        archivo.seek(0)
        json.dump(usuarios, archivo, indent=2)
        archivo.truncate()
        flash ('Usuario Creado Correctamente')
               
      return render_template ('registro.html')             
        
    except Exception as e :
      print(f"Error : {e}")
      flash('Error al registrar el usuario.')
      return render_template('registro.html')
    
  return render_template('registro.html')

  #------------ PAG LOGIN --------

@app.route ('/login', methods=['GET', 'POST']) 
def login():
  session.clear()
  
  if request.method == 'POST':
            
    usuario = request.form.get('usuario').strip().lower()
    contrasena = request.form.get('contrasena').strip()
        
    try:
      with open ('static/js/usuarios.json', 'r') as archivo:
        usuarios= json.load(archivo)    
    except:
      flash ('Error al Buscar el usuario')
      return render_template ('login.html')
    
    for u in usuarios:
      if u['usuario'] == usuario and u['contrasena'] == contrasena:
        session['usuario'] = usuario
        flash(f"Bienvenid@ {usuario.capitalize()}")
        return redirect(url_for('menu'))
      
      
      
    flash("Verifica tus Credenciales")
  
  return render_template('login.html')

  #-------- PAG ENCUESTA -----------

@app.route ('/encuesta')
def encuesta():
  return render_template('encuesta.html')
  
  #-------- PAG MENU PRINCIPAL -----------
  
@app.route ('/menu')
def menu():
  return render_template('menu.html')

  #-------- RUTA__BTN-EMERGENCIA -------

@app.route ('/emergencia', methods=('GET', 'POST'))
def emergencia():
  
  usuario_actual = session.get('usuario')
  
  if not usuario_actual:
    print(" quedo aca")
    return redirect('/menu')
  
  
  with open('static/js/usuarios.json', 'r') as archivo:
    usuarios = json.load(archivo)
    
  for u in usuarios:
    if u.get('usuario') == usuario_actual:
        telefono = u.get('telefono')
        break
    
  if telefono:
    url_whatsapp = f"https://wa.me/{telefono}?text=Necesito%20ayuda%20urgente"
    return redirect(url_whatsapp)
  else:
    return "No se encontró el teléfono del usuario", 404

if __name__ == "__main__":
  app.run(debug=True)

