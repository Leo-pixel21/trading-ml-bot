# Trading ML Bot

Este proyecto utiliza modelos de Machine Learning (MLP, KNN, Random Forest) para generar señales de compra, venta o retención de Bitcoin en tiempo real mediante un bot conectado a Binance API y alertas vía WhatsApp (Twilio).

## Estructura del repositorio

- `notebooks/`: Jupyter Notebooks con análisis exploratorio, entrenamiento de modelos y resultados.
- `src/`: Código fuente del bot, modelos y utilidades.
- `models/`: Modelos entrenados y escaladores.
- `data/`: Datos históricos utilizados.
- `img/`: Visualizaciones y gráficas del proyecto.

## Cómo ejecutar
```bash
pip install -r requirements.txt
python main.py
```

## Tecnologías
- Python
- scikit-learn
- Binance API
- Twilio
- yfinance

## Resultados
Se incluyen métricas como MAE, MSE, MAPE y una matriz de confusión para evaluar el rendimiento de los modelos.

