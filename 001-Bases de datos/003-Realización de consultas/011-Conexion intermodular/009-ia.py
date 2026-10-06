# Primero importo las librerías
import mysql.connector              # Importo MySQL
from flask import Flask             # Importo Flask
from html import escape             # Para mostrar texto de BD de forma segura


# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
    host='localhost',
    user='tiendaestetoscopios',
    password='TiendaEstetoscopios123$',
    database='tiendaestetoscopios'
)


# Creo un cursor
cursor = connection.cursor()


# Ahora creo una aplicación base
aplicacion = Flask(__name__)


# Defino un punto donde Flask va a escuchar en la web
@aplicacion.route("/")
def inicio():

    # Ejecuto una petición a la base de datos
    cursor.execute("SELECT * FROM estetoscopios")

    # Recupero el resultado
    filas = cursor.fetchall()

    # Creo el HTML
    cadena = """
<!doctype html>
<html lang="es">
<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>StethoCare - Estetoscopios profesionales</title>

    <style>

        *{
            box-sizing:border-box;
        }

        body{
            margin:0;
            font-family:Arial, Helvetica, sans-serif;
            background:#f5f7fa;
            color:#1d2733;
        }


        /* ----------------------------- */
        /* CABECERA                      */
        /* ----------------------------- */

        header{
            background:white;
            border-bottom:1px solid #e5e8ec;
            position:sticky;
            top:0;
            z-index:100;
        }

        .cabecera{
            max-width:1400px;
            margin:auto;
            height:80px;

            display:flex;
            align-items:center;
            gap:30px;

            padding:0 30px;
        }


        /* LOGOTIPO */

        .logo{
            display:flex;
            align-items:center;
            gap:10px;

            font-size:22px;
            font-weight:bold;

            white-space:nowrap;
        }

        .logo-icono{
            width:42px;
            height:42px;

            background:#176b87;
            color:white;

            display:flex;
            align-items:center;
            justify-content:center;

            border-radius:12px;

            font-size:22px;
        }

        .logo span{
            color:#176b87;
        }


        /* BUSCADOR */

        .buscador{
            flex:1;
            position:relative;
        }

        .buscador input{
            width:100%;
            border:1px solid #d8dde3;

            padding:14px 50px 14px 18px;

            border-radius:30px;

            background:#f5f7fa;

            outline:none;

            font-size:14px;
        }

        .buscador input:focus{
            border-color:#176b87;
            background:white;
        }

        .buscador span{
            position:absolute;
            right:20px;
            top:13px;
            font-size:20px;
        }


        /* ICONOS CABECERA */

        .acciones{
            display:flex;
            align-items:center;
            gap:20px;
        }

        .accion{
            cursor:pointer;
            text-align:center;
            font-size:12px;
        }

        .accion .icono{
            display:block;
            font-size:23px;
            margin-bottom:3px;
        }

        .carrito{
            position:relative;
        }

        .contador{
            position:absolute;
            top:-7px;
            right:4px;

            background:#e74c3c;
            color:white;

            width:19px;
            height:19px;

            border-radius:50%;

            display:flex;
            align-items:center;
            justify-content:center;

            font-size:10px;
            font-weight:bold;
        }


        /* ----------------------------- */
        /* NAVEGACIÓN                    */
        /* ----------------------------- */

        nav{
            background:#176b87;
        }

        nav div{
            max-width:1400px;
            margin:auto;

            display:flex;
            gap:30px;

            padding:13px 30px;
        }

        nav a{
            color:white;
            text-decoration:none;
            font-size:14px;
        }

        nav a:hover{
            text-decoration:underline;
        }


        /* ----------------------------- */
        /* HERO                          */
        /* ----------------------------- */

        .hero{
            background:
                linear-gradient(
                    120deg,
                    #eaf7fa,
                    #d6edf3
                );

            padding:65px 30px;
        }

        .hero-contenido{
            max-width:1400px;
            margin:auto;

            display:grid;
            grid-template-columns:1.3fr 1fr;
            align-items:center;
            gap:50px;
        }

        .hero h1{
            font-size:48px;
            line-height:1.05;
            margin:0 0 20px 0;
            max-width:650px;
        }

        .hero h1 span{
            color:#176b87;
        }

        .hero p{
            color:#61717e;
            font-size:18px;
            line-height:1.6;
            max-width:600px;
        }

        .hero button{
            border:0;
            background:#176b87;
            color:white;

            padding:15px 25px;

            border-radius:8px;

            font-weight:bold;
            cursor:pointer;

            margin-top:15px;
        }

        .hero button:hover{
            background:#0f536a;
        }

        .hero-imagen{
            font-size:150px;
            text-align:center;
            filter:drop-shadow(0 20px 15px rgba(0,0,0,0.15));
        }


        /* ----------------------------- */
        /* VENTAJAS                      */
        /* ----------------------------- */

        .ventajas{
            max-width:1400px;
            margin:30px auto;

            display:grid;
            grid-template-columns:repeat(4,1fr);

            background:white;

            border:1px solid #e5e8ec;
            border-radius:12px;
        }

        .ventaja{
            padding:22px;
            display:flex;
            gap:15px;
            align-items:center;

            border-right:1px solid #e5e8ec;
        }

        .ventaja:last-child{
            border-right:0;
        }

        .ventaja-icono{
            font-size:28px;
        }

        .ventaja strong{
            display:block;
            font-size:14px;
        }

        .ventaja small{
            color:#84909a;
        }


        /* ----------------------------- */
        /* CONTENIDO                     */
        /* ----------------------------- */

        main{
            max-width:1400px;
            margin:50px auto;
            padding:0 30px;
        }

        .titulo-seccion{
            display:flex;
            justify-content:space-between;
            align-items:end;
            margin-bottom:25px;
        }

        .titulo-seccion h2{
            margin:0;
            font-size:30px;
        }

        .titulo-seccion p{
            color:#7a8791;
            margin:7px 0 0 0;
        }

        .numero-productos{
            color:#7a8791;
            font-size:14px;
        }


        /* ----------------------------- */
        /* GRID PRODUCTOS                */
        /* ----------------------------- */

        #productos{
            display:grid;

            grid-template-columns:
                repeat(auto-fill,minmax(260px,1fr));

            gap:22px;
        }


        /* ----------------------------- */
        /* PRODUCTO                      */
        /* ----------------------------- */

        article{
            background:white;

            border:1px solid #e4e8eb;
            border-radius:12px;

            overflow:hidden;

            transition:
                transform 0.2s,
                box-shadow 0.2s;

            position:relative;
        }

        article:hover{
            transform:translateY(-5px);

            box-shadow:
                0 12px 30px
                rgba(0,0,0,0.09);
        }


        .imagen-producto{
            height:220px;

            display:flex;
            align-items:center;
            justify-content:center;

            background:
                linear-gradient(
                    135deg,
                    #f8fafb,
                    #edf3f5
                );

            font-size:95px;

            position:relative;
        }


        .favorito{
            position:absolute;

            right:15px;
            top:15px;

            width:36px;
            height:36px;

            border:0;
            border-radius:50%;

            background:white;

            cursor:pointer;

            box-shadow:
                0 3px 10px
                rgba(0,0,0,0.08);
        }


        .etiqueta{
            position:absolute;

            left:15px;
            top:15px;

            background:#176b87;
            color:white;

            padding:6px 10px;

            border-radius:5px;

            font-size:11px;
            font-weight:bold;
        }


        .contenido-producto{
            padding:20px;
        }


        .categoria{
            color:#176b87;
            text-transform:uppercase;

            font-size:10px;
            font-weight:bold;

            letter-spacing:1px;
        }


        article h3{
            margin:8px 0 10px 0;

            font-size:18px;
            line-height:1.3;
        }


        .descripcion{
            color:#6f7c86;

            font-size:13px;
            line-height:1.5;

            height:60px;
            overflow:hidden;
        }


        .valoracion{
            color:#f3aa18;
            font-size:13px;

            margin:15px 0;
        }

        .valoracion span{
            color:#8b969e;
        }


        .pie-producto{
            display:flex;

            justify-content:space-between;
            align-items:center;

            margin-top:10px;
        }


        .precio{
            font-size:24px;
            font-weight:bold;

            color:#16232c;
        }

        .precio small{
            font-size:13px;
            color:#7b8790;
        }


        .comprar{
            width:43px;
            height:43px;

            border:0;
            border-radius:8px;

            background:#176b87;
            color:white;

            font-size:19px;

            cursor:pointer;

            transition:0.2s;
        }

        .comprar:hover{
            background:#0f536a;
            transform:scale(1.07);
        }


        .stock{
            margin-top:15px;

            font-size:11px;
            color:#258750;
        }


        /* ----------------------------- */
        /* NEWSLETTER                    */
        /* ----------------------------- */

        .newsletter{
            margin-top:70px;

            background:#162d3a;
            color:white;

            padding:50px;

            border-radius:15px;

            display:flex;
            align-items:center;
            justify-content:space-between;

            gap:40px;
        }

        .newsletter h2{
            margin:0 0 10px 0;
        }

        .newsletter p{
            color:#b6c4cc;
        }

        .newsletter form{
            display:flex;
        }

        .newsletter input{
            padding:14px;
            border:0;
            min-width:280px;

            border-radius:
                7px 0 0 7px;

            outline:none;
        }

        .newsletter button{
            border:0;

            background:#27a3c7;
            color:white;

            padding:0 20px;

            border-radius:
                0 7px 7px 0;

            cursor:pointer;
        }


        /* ----------------------------- */
        /* FOOTER                        */
        /* ----------------------------- */

        footer{
            background:#101e26;
            color:#9eabb3;

            margin-top:70px;
            padding:40px 30px;

            text-align:center;

            font-size:12px;
        }


        /* ----------------------------- */
        /* RESPONSIVE                    */
        /* ----------------------------- */

        @media(max-width:900px){

            .acciones{
                display:none;
            }

            .hero-contenido{
                grid-template-columns:1fr;
            }

            .hero-imagen{
                display:none;
            }

            .ventajas{
                grid-template-columns:1fr 1fr;
                margin:20px;
            }

            .newsletter{
                flex-direction:column;
                align-items:flex-start;
            }

        }


        @media(max-width:600px){

            .cabecera{
                padding:0 15px;
            }

            .logo span{
                display:none;
            }

            nav div{
                overflow:auto;
            }

            .hero h1{
                font-size:35px;
            }

            .ventajas{
                grid-template-columns:1fr;
            }

            .ventaja{
                border-right:0;
                border-bottom:1px solid #e5e8ec;
            }

            main{
                padding:0 15px;
            }

            .newsletter{
                padding:30px 20px;
            }

            .newsletter form{
                width:100%;
            }

            .newsletter input{
                min-width:0;
                width:100%;
            }

        }

    </style>

</head>

<body>


<header>

    <div class="cabecera">

        <div class="logo">

            <div class="logo-icono">
                ♡
            </div>

            Stetho<span>Care</span>

        </div>


        <div class="buscador">

            <input
                type="search"
                id="busqueda"
                placeholder="Buscar estetoscopios..."
            >

            <span>⌕</span>

        </div>


        <div class="acciones">

            <div class="accion">
                <span class="icono">♙</span>
                Mi cuenta
            </div>

            <div class="accion">
                <span class="icono">♡</span>
                Favoritos
            </div>

            <div class="accion carrito">

                <span class="contador" id="contador">
                    0
                </span>

                <span class="icono">🛒</span>

                Carrito

            </div>

        </div>

    </div>

</header>


<nav>

    <div>

        <a href="#">Todos los productos</a>
        <a href="#">Cardiología</a>
        <a href="#">Pediatría</a>
        <a href="#">Enfermería</a>
        <a href="#">Estudiantes</a>
        <a href="#">Accesorios</a>
        <a href="#">Ofertas</a>

    </div>

</nav>


<section class="hero">

    <div class="hero-contenido">

        <div>

            <h1>
                Escucha lo que
                <span>realmente importa</span>
            </h1>

            <p>
                Estetoscopios profesionales seleccionados
                para médicos, enfermeros, estudiantes y
                profesionales sanitarios.
            </p>

            <button onclick="irProductos()">
                Ver productos →
            </button>

        </div>

        <div class="hero-imagen">
            🩺
        </div>

    </div>

</section>


<section class="ventajas">

    <div class="ventaja">

        <div class="ventaja-icono">🚚</div>

        <div>
            <strong>Envío rápido</strong>
            <small>Entrega 24-48 horas</small>
        </div>

    </div>


    <div class="ventaja">

        <div class="ventaja-icono">✓</div>

        <div>
            <strong>Calidad profesional</strong>
            <small>Productos seleccionados</small>
        </div>

    </div>


    <div class="ventaja">

        <div class="ventaja-icono">↩</div>

        <div>
            <strong>Devolución fácil</strong>
            <small>30 días para devolver</small>
        </div>

    </div>


    <div class="ventaja">

        <div class="ventaja-icono">🔒</div>

        <div>
            <strong>Compra segura</strong>
            <small>Pago protegido</small>
        </div>

    </div>

</section>


<main>

    <div class="titulo-seccion">

        <div>

            <h2>Nuestros estetoscopios</h2>

            <p>
                Encuentra el modelo perfecto
                para tu especialidad.
            </p>

        </div>

        <div class="numero-productos">
            """ + str(len(filas)) + """ productos
        </div>

    </div>


    <section id="productos">
"""


    # Recorro todos los productos
    for fila in filas:

        id_producto = fila[0]
        nombre = escape(str(fila[1]))
        descripcion = escape(str(fila[2]))
        precio = float(fila[3])

        cadena += f"""

        <article
            class="producto"
            data-nombre="{nombre.lower()}"
            data-descripcion="{descripcion.lower()}"
        >

            <div class="imagen-producto">

                <span class="etiqueta">
                    PROFESIONAL
                </span>

                <button
                    class="favorito"
                    onclick="favorito(this)"
                >
                    ♡
                </button>

                🩺

            </div>


            <div class="contenido-producto">

                <div class="categoria">
                    Estetoscopios
                </div>

                <h3>
                    {nombre}
                </h3>

                <div class="valoracion">
                    ★★★★★
                    <span>(24)</span>
                </div>

                <p class="descripcion">
                    {descripcion}
                </p>


                <div class="pie-producto">

                    <div class="precio">
                        {precio:.2f}€
                        <small>IVA incl.</small>
                    </div>


                    <button
                        class="comprar"
                        onclick="comprar({id_producto}, '{nombre}')"
                        title="Añadir al carrito"
                    >
                        🛒
                    </button>

                </div>


                <div class="stock">
                    ● En stock · Envío inmediato
                </div>

            </div>

        </article>

        """


    # Termino el documento HTML
    cadena += """

    </section>


    <section class="newsletter">

        <div>

            <h2>
                Mantente al día
            </h2>

            <p>
                Novedades, ofertas y consejos
                para profesionales sanitarios.
            </p>

        </div>


        <form onsubmit="suscribir(event)">

            <input
                type="email"
                placeholder="Tu correo electrónico"
                required
            >

            <button>
                Suscribirme
            </button>

        </form>

    </section>


</main>


<footer>

    © 2026 StethoCare · Tienda especializada
    en material sanitario profesional

</footer>


<script>

    // -------------------------------
    // BUSCADOR EN TIEMPO REAL
    // -------------------------------

    let buscador =
        document.querySelector("#busqueda");


    buscador.oninput = function(){

        let texto =
            buscador.value.toLowerCase();

        let productos =
            document.querySelectorAll(".producto");


        productos.forEach(function(producto){

            let nombre =
                producto.dataset.nombre;

            let descripcion =
                producto.dataset.descripcion;


            if(
                nombre.includes(texto)
                ||
                descripcion.includes(texto)
            ){

                producto.style.display = "block";

            }else{

                producto.style.display = "none";

            }

        });

    };


    // -------------------------------
    // CARRITO
    // -------------------------------

    let carrito = [];


    function comprar(id,nombre){

        carrito.push({
            id:id,
            nombre:nombre
        });


        document.querySelector(
            "#contador"
        ).textContent = carrito.length;


        console.log(
            "Producto añadido:",
            nombre
        );

    }


    // -------------------------------
    // FAVORITOS
    // -------------------------------

    function favorito(boton){

        if(boton.textContent.trim() == "♡"){

            boton.textContent = "♥";

        }else{

            boton.textContent = "♡";

        }

    }


    // -------------------------------
    // HERO
    // -------------------------------

    function irProductos(){

        document
            .querySelector("#productos")
            .scrollIntoView({
                behavior:"smooth"
            });

    }


    // -------------------------------
    // NEWSLETTER
    // -------------------------------

    function suscribir(event){

        event.preventDefault();

        alert(
            "¡Gracias por suscribirte!"
        );

    }

</script>


</body>
</html>
"""


    # Devuelvo todo el HTML
    return cadena



# Ejecuto la aplicación
if __name__ == "__main__":

    aplicacion.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )


# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()