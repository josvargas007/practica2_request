from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal con menú de opciones
@app.route("/")
def index():
    return render_template("index.html")

# Inscripción de curso
cursos = ["Matemáticas", "Física", "Química", "Biología", "Lengua y Literatura", "Historia", "Geografía"]

@app.route("/inscripcion_curso", methods=["GET", "POST"])
def inscripcion_curso():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        curso = request.form["curso"]
        return f"Nombre: {nombre}, Apellido: {apellido}, Curso: {curso}"
    return render_template("inscripcion_curso.html",cursos=cursos)



# Registro de usuarios
@app.route("/registro_usuarios", methods=["GET", "POST"])
def registro_usuarios():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]
        password = request.form["password"]
        return f"Nombre: {nombre},Apellido:{apellido}, Email: {email}, Password: {password}"
    return render_template("registro_usuarios.html")

# Registro de productos
@app.route("/registro_productos", methods=["GET", "POST"])
def registro_productos():
    categorias = ["Electrónica", "Ropa", "Juguetes", "Hogar", "Deportes"]
    if request.method == "POST":
        producto = request.form["producto"]
        precio = request.form["precio"]
        descripcion = request.form["descripcion"]
        return f"Producto: {producto}, Precio: {precio}, Descripcion: {descripcion}"
    return render_template("registro_productos.html",categorias=categorias)

# Registro de libros
@app.route("/registro_libros", methods=["GET", "POST"])
def registro_libros():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        editorial = request.form["editorial"]
        anio_publicacion = request.form["anio_publicacion"]
        resumen = request.form["resumen"]
        tipo_medio = request.form["tipo_medio"]
        
        # Guardar los datos en la base de datos o realizar otras acciones
        
        return f"Libro registrado con éxito: {titulo,autor,editorial,anio_publicacion,resumen,tipo_medio}"
    return render_template("registro_libros.html")


if __name__ == "__main__":
    app.run(debug=True)