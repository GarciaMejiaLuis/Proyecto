# Proyecto de Aplicación Web de Viajes

Este proyecto consiste en una aplicación web que permite a los usuarios calcular precios de viajes, registrar y gestionar usuarios, así como visualizar y filtrar información relacionada con los viajes almacenada en una base de datos. La aplicación está desarrollada en Python utilizando el framework Flask y utiliza una base de datos SQLite para el almacenamiento de datos.

## Estructura del Proyecto

- *app.py:* Archivo principal que contiene la lógica de la aplicación y las rutas.
- *templates/:* Carpeta que contiene los archivos HTML para las diferentes páginas de la aplicación.
- *static/:* Carpeta para almacenar archivos estáticos como hojas de estilo CSS o imágenes.

## Instrucciones de Uso

1. *Clonar el Repositorio:*
   bash
   git clone https://github.com/tuusuario/proyecto-viajes.git
   cd proyecto-viajes
   

2. *Crear un Entorno Virtual:*
   bash
   python -m venv venv
   

3. *Activar el Entorno Virtual:*
   - En Windows:
     bash
     .\venv\Scripts\activate
     
   - En macOS/Linux:
     bash
     source venv/bin/activate
     

4. *Instalar Dependencias:*
   bash
   pip install -r requirements.txt
   

5. *Configurar Base de Datos:*
   Asegúrate de modificar la configuración de la base de datos en app.py según tus necesidades.

6. *Ejecutar la Aplicación:*
   bash
   python app.py
   

   Visita [http://127.0.0.1:5000/](http://127.0.0.1:5000/) en tu navegador para acceder a la aplicación.

## Áreas de Oportunidad y Mejoras Futuras

1. *Almacenar Información Adicional de Vuelos:*
   Ampliar la base de datos para incluir información detallada sobre vuelos, como horarios, aerolíneas, tipos de vuelos, etc. Esto permitirá realizar análisis de datos más complejos y detallados.

2. *Mejorar Filtrado y Visualización de Datos:*
   Ampliar las funciones de la aplicación para que los usuarios puedan realizar un filtrado más amplio de los datos, por ejemplo, filtrar por aerolínea, tipo de vuelo, etc. Además, implementar gráficas utilizando bibliotecas como Matplotlib para presentar visualmente la información de manera más atractiva y comprensible.

3. *Implementar Autenticación más Robusta:*
   Reforzar la autenticación de usuarios con medidas como la gestión de sesiones más seguras, el uso de tokens de acceso y la implementación de políticas de contraseñas más robustas.

4. *Mejorar la Interfaz de Usuario (UI):*
   Realizar mejoras en la interfaz de usuario para hacerla más intuitiva y fácil de usar. Esto podría incluir la implementación de un diseño más moderno, la optimización para dispositivos móviles, etc.

5. *Agregar Funcionalidades Avanzadas:*
   Explorar la posibilidad de agregar funcionalidades avanzadas, como la integración con APIs de compañías aéreas para obtener información en tiempo real, la implementación de alertas para ofertas de vuelos, etc.
