# 🛒 Análisis de la Cesta de la Compra (Reglas de Asociación)

## 📖 ¿Para qué sirve y por qué utilizarlo?
El análisis de la cesta de la compra (Market Basket Analysis) es una técnica de minería de datos que descubre patrones ocultos de consumo masivo. 

En operaciones de retail y cadenas de restaurantes, su implementación es el núcleo de la rentabilidad:
1. **Ventas Cruzadas "Sin Culpa":** Permite a los cajeros recomendar productos que matemáticamente hacen sentido para el cliente, aumentando el ticket promedio sin forzar la venta.
2. **Diseño de Combos:** Identifica qué artículos se consumen juntos naturalmente para empaquetarlos en promociones atractivas.
3. **Optimización de Vitrinas:** Ayuda a organizar el *layout* de las tiendas ubicando productos altamente asociados cerca unos de otros.

## 🎯 Objetivo del Proyecto
Procesar un historial de tickets de caja para extraer Reglas de Asociación, calculando la probabilidad de que la compra de un producto "A" derive en la compra de un producto "B", midiendo la fuerza real de esa conexión.

## 🛠 Metodología y Tecnologías
Se implementó el algoritmo Apriori para superar el simple conteo manual, evaluando las métricas estadísticas de **Confianza** (probabilidad de aceptación) y **Lift** (fuerza de la asociación por encima de la casualidad).
* **Motor Analítico:** Algoritmo Apriori (Minería de Datos).
* **Preprocesamiento:** Transformación de transacciones a matrices One-Hot Encoding.
* **Librerías:** Pandas, MLxtend (Machine Learning Extensions).

## 🧠 Resultados y Aplicación de Negocio
El algoritmo analizó un volumen de 1500 facturas simuladas, logrando identificar las conexiones más fuertes del menú. 

Al filtrar por las reglas con un **Lift superior a 1.2** (conexiones no casuales), el sistema generó un pipeline de recomendaciones directas. Este modelo entrega a la gerencia de operaciones directrices claras: *"Si un cliente pide el producto X, el sistema instruye ofrecer el producto Y"*, conociendo de antemano el porcentaje exacto de probabilidad de cierre de esa venta adicional.