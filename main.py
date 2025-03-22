import requests
import dearpygui.dearpygui as dpg
import time

PRICE_ENDPOINT = "https://api.binance.com/api/v3/ticker/price"
 
def precio_actual(par):
  r = requests.get(f"{PRICE_ENDPOINT}?symbol={par}")
  info = r.json()
  
  try:
    r = requests.get(f"{PRICE_ENDPOINT}?symbol={par}")
    r.raise_for_status()  # Error para las respuestas 4xx o 5xx
    info = r.json()
    return float(info["price"])
  except requests.ConnectionError:
    print("Error: No hay conexion a internet.") # Error si no hay internet
    return None
  except requests.HTTPError as http_err:
    print(f"Ocurrio un error HTTP: {http_err}") # Errores HTTP
    return None
  except Exception as err:
    print(f"Ha ocurrido un error: {err}") # Cualquier otra Exception
    return None

monedas = [
  {
    "symbol": "BTCUSDT",
    "nombre": "BTC/USDT",
    "precio": precio_actual("BTCUSDT"),
    "precio_previo": None
  },
  {
    "symbol": "ETHUSDT",
    "nombre": "ETH/USDT",
    "precio": precio_actual("ETHUSDT"),
    "precio_previo": None
  },
  {
    "symbol": "BNBUSDT",
    "nombre": "BNB/USDT",
    "precio": precio_actual("BNBUSDT"),
    "precio_previo": None
  }
]

precios_ids = []
intervalo = 5

def actualizar_precio():
  for i, moneda in enumerate(monedas):
    moneda["precio_previo"] = moneda["precio"]
    moneda["precio"] = precio_actual(moneda["symbol"])
    dpg.set_value(precios_ids[i], moneda["precio"])  # Actualizar precio ya existente en UI

    if moneda["precio_previo"] == None:
      return
    
    # Verificar si el precio sube, baja, o se mantiene. Para cambiar el color en consecuencia
    if moneda["precio"] > moneda["precio_previo"]:
      dpg.bind_item_theme(precios_ids[i], "precio_sube")
    elif moneda["precio"] < moneda["precio_previo"]:
      dpg.bind_item_theme(precios_ids[i], "precio_baja")
    else:
      dpg.bind_item_theme(precios_ids[i], "precio_igual")

def cambiar_intervalo(sender, app_data):
  global intervalo
  intervalo = app_data  # Actualizar intervalo usando valor de slider

dpg.create_context()

with dpg.window(label="Binance App", width=600, height=350):
  # Crear temas para cambios de precio
  with dpg.theme(tag="precio_sube"):
    with dpg.theme_component(dpg.mvText):
      dpg.add_theme_color(dpg.mvThemeCol_Text,(255, 0, 0, 128))

  with dpg.theme(tag="precio_baja"):
    with dpg.theme_component(dpg.mvText):
      dpg.add_theme_color(dpg.mvThemeCol_Text,(0, 255, 0, 128))

  with dpg.theme(tag="precio_igual"):
    with dpg.theme_component(dpg.mvText):
      dpg.add_theme_color(dpg.mvThemeCol_Text,(255, 255, 255, 128))
  
  # Crea un cuadro de texto con un mensaje "Cryptos Disponibles".
  dpg.add_text("Cryptos Disponibles")

  # Crea una tabla con los titulos moneda y precio
  with dpg.table(header_row=True):
    dpg.add_table_column(label="Moneda")
    dpg.add_table_column(label="Precio")
    
    # Crea las filas de la tabla.
    for info in monedas:
      with dpg.table_row():
        dpg.add_text(info["nombre"])

        id_precio = dpg.add_text(info["precio"]) # Guardar id para modificarlo despues
        precios_ids.append(id_precio) # Guardarlo a la lista
        
        dpg.bind_item_theme(id_precio, "precio_igual")

  dpg.add_separator()

  # Agrega un slider para cambiar el intervalo de cambio de precio
  dpg.add_text("Actualizar precio cada:")
  dpg.add_slider_int(label="segundos", default_value=5, min_value=1, max_value=15, callback=cambiar_intervalo, width=100)
  
dpg.create_viewport(title="Precio Crypto", width=600, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()

ultima_actualizacion = time.time()

# Actualizar precio al transcurrir intervalo
while dpg.is_dearpygui_running():
  tiempo_actual = time.time()

  if tiempo_actual - ultima_actualizacion >= intervalo:
    actualizar_precio()
    ultima_actualizacion = tiempo_actual
  
  dpg.render_dearpygui_frame()

dpg.destroy_context()
