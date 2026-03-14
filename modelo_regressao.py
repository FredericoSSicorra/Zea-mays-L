import matplotlib.pyplot as plt
import numpy as np

x = np.array([1.6, 7.4, 11.7]) 
y = np.array([1.5, 2.8, 8.5]) 


slope, intercept = np.polyfit(x, y, 1) 
y_pred = slope * x + intercept        

# Cálculo do R² e RMSE
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)
rmse = np.sqrt(ss_res / len(y))

plt.rcParams['font.family'] = 'serif'

fig, ax = plt.subplots(figsize=(9, 6))

x_line = np.linspace(0, max(x) + 2, 100)
y_line = slope * x_line + intercept
ax.plot(x_line, y_line, color='#555555', linestyle='--', linewidth=2, label='Regressão Linear')

# Grupo 1 (1 planta) - Verde
ax.scatter(x[0], y[0], color='tab:green', edgecolors='black', s=150, zorder=5, label='Grupo 1 (1 planta)')
# Grupo 2 (5 plantas) - Laranja
ax.scatter(x[1], y[1], color='tab:orange', edgecolors='black', s=150, zorder=5, label='Grupo 2 (5 plantas)')
# Grupo 3 (10 plantas) - Azul
ax.scatter(x[2], y[2], color='tab:blue', edgecolors='black', s=150, zorder=5, label='Grupo 3 (10 plantas)')

ax.set_title('Correlação entre Cobertura Vegetal e Biomassa de Milho', fontsize=14)
ax.set_xlabel('Cobertura Vegetal na Imagem (%)', fontsize=12)
ax.set_ylabel('Biomassa Observada (kg)', fontsize=12)
ax.set_xlim(0, max(x) + 2)
ax.set_ylim(0, max(y) + 1)
ax.grid(True, linestyle=':', alpha=0.7)

sinal = '+' if intercept >= 0 else '-'
texto_estatisticas = (
    f"Modelo:\n"
    f"$y = {slope:.4f}x {sinal} {abs(intercept):.4f}$\n"
    f"$R^2 = {r_squared:.4f}$\n"
    f"$RMSE = {rmse:.3f}$ kg"
)

props = dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='gray', alpha=0.9)
ax.text(0.05, 0.95, texto_estatisticas, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

ax.legend(loc='lower right', fontsize=10)

plt.tight_layout()
plt.savefig('grafico_regressao_final.jpg', dpi=300)
print("Gráfico gerado e salvo como 'grafico_regressao_final.jpg'!")

plt.show()