from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    #return "Hola Mundo!!"
    cursos = ['PHP', 'JavaScript', 'Python', 'HTML', 'CSS', 'JAVA' ]
    data = {
        'saludo': 'Hola Mundo',
        'titulo': 'Pagina1',
        'cursos': cursos,
        'numeroCursos': len(cursos)
    }
    return render_template ('index.html', data=data)

if __name__ =='__main__':
    app.run(debug=True, port=5000)

