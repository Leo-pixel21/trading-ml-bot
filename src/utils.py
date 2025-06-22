# Funciones de utilidad (preprocesamiento, indicadores, etc.)

def calculate_ema(data, period=10):
    return data.ewm(span=period, adjust=False).mean()
