# En primer lugar importo la librería
from flask import Flask

# Ahora creo una aplicación base
aplicacion = Flask(__name__)

# Defino un punto donde Flask va a escuchar en la web
@aplicacion.route("/")
def inicio():

    cadena = """
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Calendario</title>

        <style>
            *{
                box-sizing:border-box;
            }

            body{
                margin:0;
                background:#f3f4f6;
                font-family:Arial, sans-serif;
                color:#333;
            }

            .contenedor{
                width:900px;
                max-width:95%;
                margin:50px auto;
            }

            h1{
                margin:0 0 5px 0;
                font-size:32px;
            }

            p{
                margin-top:0;
                color:#777;
            }

            main{
                display:grid;
                grid-template-columns:repeat(7,1fr);
                gap:8px;

                background:white;
                padding:20px;

                border-radius:15px;

                box-shadow:
                    0px 10px 30px rgba(0,0,0,0.1);
            }

            .dia{
                min-height:90px;

                background:#f8f8f8;

                border:1px solid #ddd;
                border-radius:8px;

                padding:10px;

                font-size:18px;
                font-weight:bold;

                transition:0.2s;

                cursor:pointer;
            }

            .dia:hover{
                transform:translateY(-4px);
                background:white;

                box-shadow:
                    0px 5px 15px rgba(0,0,0,0.15);
            }

            .feriado{
                background:#ffe5e5;
                border-color:#ffaaaa;
                color:#b30000;
            }

            .feriado:hover{
                background:#ffd5d5;
            }

            .numero{
                display:flex;

                width:35px;
                height:35px;

                align-items:center;
                justify-content:center;

                border-radius:50%;
            }

            .feriado .numero{
                background:#c62828;
                color:white;
            }

            .texto{
                margin-top:10px;
                font-size:11px;
                font-weight:normal;
                color:#777;
            }

            .feriado .texto{
                color:#b30000;
            }
        </style>

    </head>

    <body>

        <div class="contenedor">

            <h1>Calendario</h1>
            <p>Calendario mensual</p>

            <main>
    """

    # Recordamos cómo hacer estructuras de bucle
    for dia in range(1,31):

        if dia == 18:

            cadena += """
            <div class="dia feriado">
                <div class="numero">
            """

            cadena += str(dia)

            cadena += """
                </div>

                <div class="texto">
                    Día festivo
                </div>
            </div>
            """

        else:

            cadena += """
            <div class="dia">
                <div class="numero">
            """

            cadena += str(dia)

            cadena += """
                </div>
            </div>
            """

    cadena += """
            </main>

        </div>

    </body>
    </html>
    """

    return cadena


# Ejecuto la aplicación
if __name__ == "__main__":
    aplicacion.run(debug=True)