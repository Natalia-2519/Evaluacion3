from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])
            promedio = (nota1 + nota2 + nota3) / 3
            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"
        except ValueError:
            promedio = "Error: Ingresa valores numéricos válidos"
            estado = ""

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = None
    cantidad_letras = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        nombres = [nombre1, nombre2, nombre3]
        nombre_mayor = max(nombres, key=len)
        cantidad_letras = len(nombre_mayor)

    return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, cantidad_letras=cantidad_letras)

if __name__ == '__main__':
    app.run(debug=True)




