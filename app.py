from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

productos_list = [
    {'id': 1, 'nombre': 'Remera', 'descripcion': 'Remera Nike', 'precio': 50000.00},
    {'id': 2, 'nombre': 'Pantalon', 'descripcion': 'Pantalon Nike', 'precio': 70000.00}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nuevo_producto = {
            'id': len(productos_list) + 1,
            'nombre': request.form['nombre'],
            'descripcion': request.form['descripcion'],
            'precio': float(request.form['precio'])
        }
        productos_list.append(nuevo_producto)
        return redirect(url_for('index'))
    return render_template('index.html', productos=productos_list)

if __name__ == '__main__':
    app.run(debug=True)
