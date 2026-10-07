from flask import Flask
import calendar

aplicacion = Flask(__name__)


@aplicacion.route("/")
def inicio():

    cadena = """
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Super Calendario 1978 - 2026</title>

        <style>
            *{
                box-sizing:border-box;
            }

            body{
                margin:0;
                font-family:Arial, sans-serif;
                background:#eeeeee;
                color:#222;
            }

            header{
                background:#222;
                color:white;
                padding:30px;
                text-align:center;
                position:sticky;
                top:0;
                z-index:100;
                box-shadow:0px 5px 15px rgba(0,0,0,0.3);
            }

            header h1{
                margin:0;
                font-size:35px;
            }

            header p{
                margin:8px 0 0 0;
                color:#aaa;
            }

            main{
                width:95%;
                margin:auto;
            }

            .anio{
                background:white;
                margin:30px 0;
                padding:25px;
                border-radius:15px;
                box-shadow:0px 5px 20px rgba(0,0,0,0.1);
            }

            .anio h2{
                font-size:40px;
                margin:0 0 20px 0;
                border-bottom:5px solid #222;
                padding-bottom:10px;
            }

            .meses{
                display:grid;
                grid-template-columns:
                    repeat(auto-fit,minmax(300px,1fr));
                gap:20px;
            }

            .mes{
                border:1px solid #ccc;
                border-radius:10px;
                overflow:hidden;
                background:#fafafa;
            }

            .mes h3{
                margin:0;
                padding:12px;
                background:#333;
                color:white;
                text-align:center;
                text-transform:uppercase;
                font-size:14px;
                letter-spacing:2px;
            }

            .cabecera-dias,
            .dias{
                display:grid;
                grid-template-columns:repeat(7,1fr);
            }

            .cabecera-dias div{
                background:#ddd;
                padding:8px 2px;
                text-align:center;
                font-size:10px;
                font-weight:bold;
            }

            .dia{
                min-height:45px;
                padding:5px;
                border-right:1px solid #eee;
                border-bottom:1px solid #eee;
                font-size:12px;
                transition:0.2s;
                cursor:pointer;
            }

            .dia:hover{
                background:#222;
                color:white;
                transform:scale(1.1);
                position:relative;
                z-index:10;
                box-shadow:0px 3px 10px rgba(0,0,0,0.4);
            }

            .vacio{
                background:#f3f3f3;
            }

            .fin-semana{
                background:#fff0f0;
            }

            .hoy{
                background:#ffcc00;
                color:#111;
                font-weight:bold;
                border-radius:5px;
            }

            footer{
                text-align:center;
                padding:50px;
                color:#777;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>SUPER CALENDARIO</h1>
            <p>1978 — 2026</p>
        </header>

        <main>
    """

    nombres_meses = [
        "",
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
    ]


    # ==========================================
    # PRIMER BUCLE: AÑOS
    # ==========================================

    for anio in range(1978, 2027):

        cadena += """
        <section class="anio">
        """

        cadena += "<h2>" + str(anio) + "</h2>"

        cadena += """
        <div class="meses">
        """


        # ======================================
        # SEGUNDO BUCLE: MESES
        # ======================================

        for mes in range(1, 13):

            cadena += """
            <div class="mes">
            """

            cadena += "<h3>" + nombres_meses[mes] + "</h3>"

            cadena += """
                <div class="cabecera-dias">
                    <div>L</div>
                    <div>M</div>
                    <div>X</div>
                    <div>J</div>
                    <div>V</div>
                    <div>S</div>
                    <div>D</div>
                </div>

                <div class="dias">
            """


            # Averiguamos qué día de la semana
            # empieza el mes y cuántos días tiene

            primer_dia, numero_dias = calendar.monthrange(
                anio,
                mes
            )


            # ==================================
            # CASILLAS VACÍAS
            # ==================================

            for vacio in range(primer_dia):

                cadena += """
                <div class="dia vacio"></div>
                """


            # ==================================
            # TERCER BUCLE: DÍAS
            # ==================================

            for dia in range(1, numero_dias + 1):

                dia_semana = calendar.weekday(
                    anio,
                    mes,
                    dia
                )

                clase = "dia"

                # Sábado o domingo
                if dia_semana == 5 or dia_semana == 6:
                    clase += " fin-semana"


                # Marcamos el 6 de octubre de 2026
                # como ejemplo
                if (
                    anio == 2026
                    and mes == 10
                    and dia == 6
                ):
                    clase += " hoy"


                cadena += (
                    "<div class='"
                    + clase
                    + "'>"
                    + str(dia)
                    + "</div>"
                )


            cadena += """
                </div>
            </div>
            """


        cadena += """
            </div>
        </section>
        """


    cadena += """
        </main>

        <footer>
            Super Calendario · 1978 - 2026
        </footer>

    </body>
    </html>
    """

    return cadena


if __name__ == "__main__":
    aplicacion.run(debug=True)