# Binance Tracker Python

Este programa es una aplicación de escritorio que permite a los usuarios visualizar los precios actuales de varias criptomonedas en tiempo real. Utiliza la API de Binance para obtener los precios y actualizarlos automáticamente en intervalos configurables. Además, el programa muestra cambios en los precios con un indicador visual: el fondo del precio cambia a verde si el precio ha aumentado y a rojo si ha disminuido.

## Características

- **Visualización de Precios**: Muestra los precios actuales de criptomonedas como BTC, ETH y BNB.
- **Actualización Automática**: Los precios se actualizan automáticamente en intervalos configurables por el usuario.
- **Indicadores Visuales**: Cambia el color de fondo del precio según si ha subido (verde) o bajado (rojo).
- **Manejo de Errores**: Incluye manejo de errores para situaciones como falta de conexión a Internet.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `requests`: Para realizar solicitudes HTTP a la API de Binance.
  - `dearpygui`: Para la interfaz gráfica de usuario.

## Instalación

1. Clona este repositorio o descarga el código fuente.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. Instala las bibliotecas necesarias ejecutando el siguiente comando:

   ```
   pip install -r requirements.txt
   ```

## Uso

1. Al iniciar la aplicación, verás una tabla con los precios actuales de las criptomonedas.
2. Puedes ajustar el intervalo de actualización de precios utilizando el slider.

4. Observa cómo el color de fondo de los precios cambia según la variación en el precio.