import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import os

if not os.path.exists('dataset_tickets_caja.csv'):
    print("⚠️ Faltan los datos. Ejecuta primero: py generar_tickets.py")
else:
    # 1. Cargar las facturas
    df = pd.read_csv('dataset_tickets_caja.csv')

    # 2. Transformar los datos a formato matriz matemática (One-Hot Encoding)
    # Convierte la lista de productos separados por coma en columnas de 1s (compró) y 0s (no compró)
    cesta_matriz = df['Articulos_Comprados'].str.get_dummies(sep=',')

    # 3. Aplicar el Algoritmo Apriori
    # Buscamos combinaciones de productos que aparezcan en al menos el 5% de los tickets
    print("🔍 Analizando 1500 tickets buscando patrones frecuentes...")
    itemsets_frecuentes = apriori(cesta_matriz, min_support=0.05, use_colnames=True)

    # 4. Generar Reglas de Asociación de Alto Impacto
    print("🧠 Calculando métricas de venta cruzada (Confianza y Lift)...")
    reglas = association_rules(itemsets_frecuentes, metric="lift", min_threshold=1.2)

    # Ordenar por el Lift (las conexiones más fuertes primero)
    reglas = reglas.sort_values(by='lift', ascending=False)

    # 5. Imprimir el Dashboard Gerencial en Consola
    print("\n🛒 TOP OPORTUNIDADES DE VENTA CRUZADA 'SIN CULPA' 🛒")
    print("-" * 65)
    
    # Extraer las mejores 4 reglas para mostrarlas de forma limpia
    for index, row in reglas.head(4).iterrows():
        # Limpiar el formato de texto de la librería
        antecedente = list(row['antecedents'])[0]
        consecuente = list(row['consequents'])[0]
        confianza = row['confidence'] * 100
        lift = row['lift']

        print(f"👉 Si el cliente pide [{antecedente}] ➡️ Ofrecer [{consecuente}]")
        print(f"   📈 Probabilidad de aceptación: {confianza:.1f}%")
        print(f"   🚀 Multiplicador de conexión (Lift): {lift:.2f}x\n")

    # 6. Exportar reporte para el equipo de marketing u operaciones
    reglas.to_csv('reporte_ventas_cruzadas.csv', index=False)
    print("📁 Reporte algorítmico exportado como 'reporte_ventas_cruzadas.csv'")