from flask import Flask, render_template, request, flash

# Creación de la aplicación Flask
app = Flask(__name__)
app.secret_key = "clave_secreta_calculadora" # Necesario para flash messages

@app.route("/", methods = ["GET", "POST"])
def calculadora():
    """
    Funcion principal que maneja las peticiones GET y POST de la calculadora.
    - GEt: Muestra el formulario vacío
    - POST: Procesa los datos enviados y realiza la operacion matematica
    """

    resultado = None
    error = None


    # Si el metodo es POSt, se esta enviando el formulario
    if request.method == 'POST':
        try:
            # Obtener los valores del formulario
            primer_numero = float(request.form.get("primer_numero"))
            segundo_numero = float(request.form.get("segundo_numero"))
            operacion = request.form.get("operacion")
            
            # Realizar la operación matematica seleccionada
            if operacion == "suma":
                resultado = primer_numero + segundo_numero
            elif operacion == "resta":
                resultado = primer_numero - segundo_numero
            elif operacion == "multiplicacion":
                resultado = primer_numero * segundo_numero
            elif operacion == "division":
                # Verificar división por cero
                if segundo_numero == 0:
                    error = "Error: No se puede dividir por cero"
                else:
                    resultado = primer_numero / segundo_numero
        except ValueError:
            # Manejo de error si no se ingresan números válidos
            error = "Error: Por favor ingrese números válidos"
            
    # Renderizar la plantilla HTML con los datos correspondientes
    return render_template("calculadora.html", resultado=resultado, error=error)

if __name__ == "__main__":
    # Ejecutar la aplicación Flask
    app.run(debug=True)