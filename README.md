# 📉 Modelo de Retención de Clientes (XGBoost + SHAP)

## 📖 ¿Para qué sirve y por qué utilizarlo?
El análisis de Churn (Fuga de Clientes) permite identificar qué usuarios están en riesgo de abandonar la marca antes de que lo hagan. 

En un entorno de retail o consumo masivo, su implementación es estratégica para:
1. **Retención Proactiva:** Permite dirigir campañas de fidelización únicamente a los clientes en riesgo, optimizando el presupuesto de marketing.
2. **Identificación de Puntos de Dolor:** Ayuda a entender si los clientes se van por precios, por mal servicio o por falta de interacción.
3. **Maximización del LTV (Life Time Value):** Retener a un cliente es matemáticamente más rentable que adquirir uno nuevo.

## 🎯 Objetivo del Proyecto
Desarrollar un modelo predictivo capaz de anticipar la fuga de clientes y, de manera crítica, explicar los motivos subyacentes de dicha fuga utilizando Inteligencia Artificial Explicable (XAI).

## 🛠 Metodología y Tecnologías
Se construyó un pipeline analítico avanzado superando los modelos tradicionales de clasificación de caja negra.
* **Motor Predictivo:** XGBoost Classifier, optimizado para funciones de pérdida logarítmica (logloss).
* **Interpretabilidad (XAI):** Valores SHAP (SHapley Additive exPlanations) para la atribución de importancia de variables a nivel global y local.
* **Librerías:** Pandas, Scikit-Learn, XGBoost, SHAP, Matplotlib.

## 🧠 Resultados y Explicabilidad del Negocio
El modelo XGBoost analizó 2000 perfiles de comportamiento transaccional. La integración con SHAP reveló los siguientes *insights* operativos:

1. **El servicio es el mayor riesgo:** La variable `Quejas_Servicio` es el factor principal de abandono.
2. **Digitalización como retención:** No estar inscrito en la aplicación móvil de lealtad (`Usa_App_Lealtad = 0`) incrementa drásticamente la probabilidad de fuga.
3. **Inactividad crítica:** Superar el umbral de `Dias_Inactivo` empuja al cliente fuera del ecosistema de la marca.

Este modelo permite a los equipos de operaciones y servicio al cliente enfocar sus esfuerzos no en guerras de precios, sino en la calidad del servicio en tienda y la adopción digital.