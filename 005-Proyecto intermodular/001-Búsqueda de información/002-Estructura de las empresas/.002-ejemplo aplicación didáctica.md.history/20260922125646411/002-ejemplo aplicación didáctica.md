Aplicación:
Marcas + PRogramación + BBD
Segundo: Programación aplicaciones móviles

BBDD alumnos, preguntas
Hacer tests es sencillo, 
Redactar todas las posibles respuestas a cada pregunta incorrecta
Requiere trabajo de profesor

50 - 
Este proyecto tal y como lo estás comentando es viable

Sí. Y hay un dato interesante: **el sector al que apuntas tiene empresas que van desde pequeños equipos de decenas de personas hasta compañías valoradas en más de 1.000 millones de dólares**. Tu concepto —quiz + feedback pedagógico inmediato tanto al acertar como al fallar— encaja en *formative assessment / game-based learning / adaptive learning*, donde están [Kahoot!](https://kahoot.com/?utm_source=chatgpt.com), [Wayground (antes Quizizz)](https://wayground.com/?utm_source=chatgpt.com), [Wooclap](https://www.wooclap.com/?utm_source=chatgpt.com) y Nearpod.

### Algunos comparables

| Empresa                 | Tipo                             | Tamaño / alcance                      | Financiación / valoración                                  | Facturación conocida o estimada          |
| ----------------------- | -------------------------------- | ------------------------------------- | ---------------------------------------------------------- | ---------------------------------------- |
| **Kahoot!**             | quizzes gamificados              | escala mundial                        | adquirida por **NOK 17.200 M (~$1.7B)**                    | en Q2 2023 facturaba ~$41 M/trimestre    |
| **Wayground / Quizizz** | quizzes + actividades + IA       | 90% escuelas EEUU; 150+ países        | **$47 M levantados**; valoración reportada ~$300 M en 2021 | estimación externa 2025: **$47.5 M/año** |
| **Wooclap**             | preguntas/interacción educativa  | +50 M learners                        | inversión reciente **€25 M**                               | estimación externa 2024: **$9.9 M/año**  |
| **Nearpod**             | lecciones + quizzes + evaluación | 1.2 M profesores cuando fue adquirida | adquirida por aproximadamente **$650 M**                   | no pública                               |
| **Duolingo**            | aprendizaje gamificado           | 52.7 M usuarios diarios a final 2025  | cotizada                                                   | **$1.038 B/año** en 2025                 |

Hay que distinguir las cifras auditadas de las estimaciones privadas. Duolingo, por ejemplo, declara oficialmente ingresos de **$1.037,6 M en 2025**, +39% interanual. 

En Kahoot!, la operación que terminó llevándola a manos privadas valoró el capital en **NOK 17.200 millones**, aproximadamente $1.7B. ([PR Newswire][1]) En el momento de anunciarse la operación, Kahoot comunicaba aproximadamente **$41 M de ingresos trimestrales** y más de un millón de usuarios de pago. ([TechCrunch][2])

Quizizz, que desde 2025 se llama **Wayground**, es probablemente el comparable más interesante para lo que planteas. La empresa levantó **$31,5 M en una Serie B en 2021** y $47 M acumulados; TechCrunch informó entonces de una valoración aproximada de **$300 M**. ([PR Newswire][3]) Actualmente afirma utilizarse en el 90% de las escuelas estadounidenses y más de 150 países. ([Wayground][4]) Una fuente privada estima unos **$47,5 M de ingresos en 2025 y ~430 empleados**, pero tomaría estas dos últimas cifras como orientativas, no como cuentas auditadas. ([Latka][5])

Nearpod es otro caso especialmente interesante. Cuando Renaissance anunció su adquisición en 2021, Nearpod tenía aproximadamente **300 empleados** y había captado algo menos de $31 M de capital; la operación fue reportada en aproximadamente **$650 M**. ([EdSurge][6])

Y hay un ejemplo europeo de una escala mucho más cercana: Wooclap. Una estimación externa situaba en 2024 la empresa en unos **71 empleados y $9,9 M de ingresos**, aunque nuevamente es una estimación privada. ([Latka][7]) Más significativamente, la propia empresa anunció una inversión de **€25 M** y afirma superar los **50 millones de learners**. ([Wooclap][8])

## Lo interesante para tu proyecto

No necesitas empezar ni remotamente con esas estructuras. De hecho, yo separaría el desarrollo de una empresa de este tipo en algo así:

| Fase                       | Equipo aproximado | Presupuesto anual orientativo | Objetivo de facturación |
| -------------------------- | ----------------: | ----------------------------: | ----------------------: |
| Fundador / MVP             |               1–2 |                      €10k–50k |                  €0–50k |
| Microempresa               |               2–5 |                     €50k–200k |               €50k–300k |
| Producto comercial         |              5–10 |                    €200k–600k |                €300k–1M |
| EdTech pequeña consolidada |             10–30 |                       €0.6–2M |                   €1–5M |
| EdTech mediana             |            30–100 |                         €2–8M |                  €5–20M |
| Escala internacional       |          100–500+ |                       €8–50M+ |               €20–100M+ |

Estas bandas son **un modelo orientativo mío**, no estadísticas sectoriales: sirven para dimensionar el negocio, no como benchmark contable.

Y aquí veo una diferencia importante en tu planteamiento. No lo vendería conceptualmente como simplemente:

**"un Kahoot para niños".**

Hay una propuesta educativa bastante más interesante:

**pregunta → respuesta → explicación → aprendizaje → siguiente pregunta.**

Es decir, que **el quiz sea el mecanismo de aprendizaje y no solamente el mecanismo de evaluación**.

Por ejemplo:

> ¿Por qué vemos primero el relámpago y después escuchamos el trueno?
>
> A) Porque el relámpago ocurre antes
> B) Porque la luz viaja más rápido que el sonido ✓
> C) Porque las nubes bloquean el sonido
> D) Porque el trueno se produce en el suelo

Si responde **B**:

> ✓ Correcto. La luz viaja aproximadamente a 300.000 km/s, mientras que el sonido en el aire lo hace aproximadamente a 343 m/s. Por eso vemos el relámpago prácticamente inmediatamente.

Pero si responde **A**:

> ✗ No exactamente. El relámpago y el trueno proceden prácticamente del mismo fenómeno. Lo que cambia es el tiempo que tardan la luz y el sonido en llegar hasta nosotros.

Y aquí hay una posibilidad todavía más potente: **no tener solamente una explicación general para la pregunta, sino una explicación específica para cada respuesta incorrecta**.

Eso permitiría que el software identificase *qué concepto ha entendido mal el niño*. Entonces pasarías de un sistema de quizzes a algo mucho más cercano a un **tutor adaptativo**.

Por ejemplo:

**Pregunta 1 → error B → detecto misconception X → explicación → pregunta de refuerzo → compruebo si lo ha entendido → continúo.**

Eso cambia bastante el producto y, potencialmente, también el modelo de negocio.

### Una escala que veo especialmente interesante

Con un producto SaaS educativo, no hace falta una barbaridad de clientes para crear una empresa razonable.

Supongamos:

**familias: €5/mes**

10.000 familias × €5 × 12 = **€600.000/año**

50.000 familias → **€3 M/año**

100.000 familias → **€6 M/año**

Pero para alguien con experiencia docente, probablemente es incluso más interesante un modelo **B2B2C para colegios/academias**, porque el profesor crea/asigna quizzes y los alumnos los realizan.

Por ejemplo, un hipotético precio medio de **€1.500/año por centro**:

100 centros → €150.000
500 centros → €750.000
1.000 centros → **€1,5 M**
5.000 centros → **€7,5 M**

Eso significa que **una empresa de 5–10 personas podría tener perfectamente sentido económico** mucho antes de acercarse al tamaño de Kahoot o Wayground.

Y hay otra lección que extraería de los comparables: **el software es sólo una parte del coste**. Una vez construido el motor de preguntas, cuentas, estadísticas, gamificación, clases, etc., una parte enorme del activo pasa a ser **el contenido educativo**: preguntas, explicaciones, currículo, ilustraciones, traducciones, revisión pedagógica y actualización. Wayground, por ejemplo, ha evolucionado desde los quizzes hacia evaluaciones, presentaciones, vídeos, flashcards, adaptaciones por nivel e IA. ([Wayground][9])

Por tanto, para plantear tu empresa yo pensaría inicialmente en **3–5 personas**, no 30: producto/programación, contenido pedagógico, diseño/UX infantil y comercial/colegios, pudiendo solaparse varios roles al principio. Con un fundador técnico y docente, una parte especialmente cara del arranque puede cubrirse internamente, lo que reduce bastante el capital inicial necesario.

Si quieres, puedo hacer el siguiente paso, que creo que sería muy útil: **analizar 10 competidores directos (Kahoot, Quizizz/Wayground, Blooket, Gimkit, Quizlet, Socrative, Nearpod, etc.) y construir una tabla con usuarios, empleados, facturación, precios, financiación, modelo de negocio y funcionalidades**, y a partir de ahí detectar **qué hueco concreto de mercado podría ocupar tu producto**.

[1]: https://www.prnewswire.com/news-releases/agreement-for-launch-of-a-recommended-all-cash-offer-of-nok-35-per-share-to-the-shareholders-of-kahoot-asa-301877449.html?utm_source=chatgpt.com "AGREEMENT FOR LAUNCH OF A RECOMMENDED ALL CASH OFFER OF NOK 35 PER SHARE TO THE SHAREHOLDERS OF KAHOOT! ASA"
[2]: https://techcrunch.com/2023/07/14/kahoot-acquired/?utm_source=chatgpt.com "Gamified e-learning platform Kahoot gets $1.7B acquisition offer from Goldman Sachs, Lego and more | TechCrunch"
[3]: https://www.prnewswire.com/news-releases/quizizz-gains-momentum-raises-31-5-million-to-motivate-every-student-301322655.html?utm_source=chatgpt.com "Quizizz gains momentum, raises $31.5 million to motivate every student"
[4]: https://help.wayground.com/support/solutions/articles/158000403991-what-is-wayground-?utm_source=chatgpt.com "What is Wayground? :"
[5]: https://getlatka.com/companies/wayground?utm_source=chatgpt.com "Wayground Revenue 2025: $47.5M ARR, $34.5M Raised"
[6]: https://www.edsurge.com/news/2021-02-19-renaissance-learning-to-acquire-nearpod-in-blockbuster-650m-all-cash-deal?utm_source=chatgpt.com "Renaissance Learning to Acquire Nearpod in Blockbuster $650M All-Cash Deal | EdSurge News"
[7]: https://getlatka.com/companies/wooclap/funding?utm_source=chatgpt.com "Wooclap Revenue 2024: $9.9M ARR (Bootstrapped)"
[8]: https://www.wooclap.com/es/blog/impact-expansion-25m/?utm_source=chatgpt.com "La EdTech Wooclap recauda 25 millones de euros de Impact Expansion"
[9]: https://wayground.com/?lng=es-ES&utm_source=chatgpt.com "Quizizz is now Wayground | Teacher AI and Resources"
