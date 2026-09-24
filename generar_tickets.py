import pandas as pd
import random

random.seed(42)
n_tickets = 1500

# Catálogo base de productos
productos = ['Tinto', 'Capuchino', 'Latte', 'Pan de Bono', 'Empanada', 'Torta de Chocolate', 'Jugo de Naranja', 'Galleta de Avena', 'Agua']

tickets = []
for i in range(n_tickets):
    ticket = []
    perfil = random.random()
    
    # 1. Simulación de patrones naturales de consumo
    if perfil < 0.4: 
        # Cliente tradicional: Café negro y horneado salado
        ticket.append('Tinto')
        if random.random() < 0.7: 
            ticket.append(random.choice(['Pan de Bono', 'Empanada']))
            
    elif perfil < 0.7: 
        # Cliente de indulgencia: Bebida con leche y postre
        ticket.append(random.choice(['Capuchino', 'Latte']))
        if random.random() < 0.6: 
            ticket.append(random.choice(['Torta de Chocolate', 'Galleta de Avena']))
            
    else: 
        # Cliente de paso: Bebidas frías
        ticket.append(random.choice(['Jugo de Naranja', 'Agua']))
        if random.random() < 0.3: 
            ticket.append(random.choice(['Empanada', 'Pan de Bono']))
    
    # 2. Inyección de compras impulsivas aleatorias (ruido estadístico)
    if random.random() < 0.2:
        ticket.append(random.choice(productos))
    
    # Limpiar duplicados dentro del mismo ticket
    ticket_unico = list(set(ticket))
    tickets.append(",".join(ticket_unico))

# 3. Construir y exportar la base de datos
df_transacciones = pd.DataFrame({
    'ID_Ticket': range(1000, 1000 + n_tickets),
    'Articulos_Comprados': tickets
})

df_transacciones.to_csv('dataset_tickets_caja.csv', index=False)

print("✅ Éxito: 'dataset_tickets_caja.csv' generado con 1500 facturas simuladas.")
print("-" * 60)
print("Muestra de los primeros 5 tickets de caja:")
print(df_transacciones.head())