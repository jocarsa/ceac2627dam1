sudo mysql -u root -p

CREATE DATABASE blogceacdam2627;

USE blogceacdam2627;

CREATE TABLE articulos (
	id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(255),
  fecha DATE,
  contenido TEXT
);

INSERT INTO articulos (titulo, fecha, contenido) VALUES

(
    'Desarrollo de aplicaciones empresariales a medida',
    '2026-10-26',
    'En JOCARSA desarrollamos soluciones de software personalizadas para empresas, utilizando tecnologías como PHP, Python, JavaScript y bases de datos SQL.'
),

(
    'Inteligencia artificial aplicada a la empresa',
    '2026-10-25',
    'La integración de modelos de inteligencia artificial permite automatizar procesos, analizar información y crear nuevas herramientas que mejoran la productividad empresarial.'
),

(
    'Formación profesional en desarrollo de aplicaciones',
    '2026-10-24',
    'La enseñanza de programación, bases de datos y desarrollo de interfaces constituye una parte fundamental de mi actividad como docente de informática.'
),

(
    'Implementación de modelos de lenguaje locales',
    '2026-10-23',
    'El uso de Ollama permite ejecutar modelos de inteligencia artificial en servidores propios, ofreciendo mayor control sobre los datos y reduciendo la dependencia de servicios externos.'
),

(
    'Automatización de procesos mediante Python',
    '2026-10-22',
    'Python facilita el desarrollo de herramientas para procesar documentos, generar informes, analizar datos y automatizar tareas repetitivas dentro de una organización.'
),

(
    'Diseño de interfaces de usuario con JOCARSA IU',
    '2026-10-21',
    'El desarrollo de un sistema propio de componentes visuales permite mantener la coherencia gráfica y funcional entre diferentes aplicaciones empresariales.'
),

(
    'Gestión académica mediante aplicaciones web',
    '2026-10-20',
    'Las plataformas educativas personalizadas permiten gestionar alumnos, asignaturas, calificaciones, asistencias y entregas desde una interfaz centralizada.'
),

(
    'Integración de inteligencia artificial en Moodle',
    '2026-10-19',
    'La combinación de Moodle con servicios de inteligencia artificial abre nuevas posibilidades para personalizar el aprendizaje y automatizar procesos educativos.'
),

(
    'Desarrollo de sistemas CRM para empresas',
    '2026-10-18',
    'Los sistemas CRM permiten gestionar prospectos, clientes, campañas comerciales y oportunidades de venta, facilitando el seguimiento de la actividad empresarial.'
),

(
    'Diseño de aplicaciones CAD en el navegador',
    '2026-10-17',
    'Las tecnologías SVG y JavaScript permiten desarrollar herramientas de dibujo técnico para crear planos arquitectónicos, distribuir mobiliario y diseñar instalaciones.'
),

(
    'Transcripción automática de audio con Whisper',
    '2026-10-16',
    'Los sistemas de reconocimiento de voz permiten convertir grabaciones y vídeos en documentos de texto, subtítulos y materiales educativos reutilizables.'
),

(
    'Administración de servidores Linux',
    '2026-10-15',
    'La administración de servidores Ubuntu incluye la configuración de Apache, bases de datos, servicios web, certificados de seguridad y sistemas de monitorización.'
),

(
    'Desarrollo de sistemas ERP personalizados',
    '2026-10-14',
    'Un ERP desarrollado a medida permite integrar la gestión de clientes, empleados, productos, facturación y operaciones empresariales en una única plataforma.'
),

(
    'Sistemas RAG para consultar documentación',
    '2026-10-13',
    'La generación aumentada por recuperación combina modelos de lenguaje con bases de conocimiento para responder preguntas utilizando documentación específica.'
),

(
    'Creación de plataformas de formación online',
    '2026-10-12',
    'El desarrollo de entornos educativos digitales permite distribuir contenidos, organizar cursos, evaluar actividades y realizar un seguimiento del progreso del alumnado.'
),

(
    'Simulaciones de vida artificial con JavaScript',
    '2026-10-11',
    'Las simulaciones de agentes autónomos permiten estudiar comportamientos emergentes, reproducción, consumo energético y adaptación a entornos virtuales.'
),

(
    'Monitorización de infraestructuras informáticas',
    '2026-10-10',
    'La recopilación de métricas de CPU, memoria, almacenamiento y conectividad permite detectar incidencias y mejorar el rendimiento de los servidores.'
),

(
    'Desarrollo de reproductores de vídeo educativos',
    '2026-10-09',
    'Los reproductores personalizados permiten integrar subtítulos, controles de reproducción, navegación temporal y funcionalidades específicas para contenidos formativos.'
),

(
    'Aplicaciones web con Flask y SQLite',
    '2026-10-08',
    'La combinación de Flask y SQLite facilita la creación de aplicaciones ligeras con autenticación, gestión de datos, servicios API y paneles de administración.'
),

(
    'El futuro del desarrollo de software con inteligencia artificial',
    '2026-10-07',
    'La evolución de la inteligencia artificial está transformando la programación y generando nuevas oportunidades en arquitectura de software, automatización y desarrollo de productos digitales.'
);

--ahora el usuario 

