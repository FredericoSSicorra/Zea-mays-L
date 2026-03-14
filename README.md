# Predição Não-Destrutiva de Biomassa em Milho Silagem (*Zea mays L.*)

Este repositório contém o código-fonte de uma prova de conceito acadêmica focada em Agricultura de Precisão de ultrabaixo custo. O objetivo do pipeline é estimar a massa fresca do milho silagem de forma não-destrutiva, extraindo características fenológicas através de imagens RGB convencionais e aplicando modelos estatísticos simples.

*Nota: Este repositório foi anonimizado para fins de revisão por pares (blind review).*

## 📂 Estrutura do Repositório

* `processamento_imagem.py`: Script responsável pelo pré-processamento (OpenCV). Carrega a imagem original, realiza a conversão para o espaço HSV, aplica a limiarização da cor verde e calcula o percentual de área vegetativa útil da amostra.
* `modelo_regressao.py`: Script focado em Machine Learning (Scikit-Learn). Recebe os dados extraídos das imagens e os cruza com a massa real aferida em campo, gerando o modelo de Regressão Linear Simples, extraindo as métricas (R² e RMSE) e plotando o gráfico de calibração.
* `requirements.txt`: Lista de dependências e bibliotecas Python necessárias para rodar o projeto.
* `testphoto1.jpg` e `testphoto2.jpg`: Imagens padronizadas de amostra para validação e teste do algoritmo.

## 🚀 Como Executar (Reprodução do Experimento)

**1. Instalação das dependências**
Certifique-se de ter o Python 3 instalado. No terminal, instale as bibliotecas necessárias executando:
```bash
pip install -r requirements.txt
