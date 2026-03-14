# Predição Não-Destrutiva de Biomassa em Milho Silagem (*Zea mays L.*)

Este repositório contém o código-fonte de uma prova de conceito acadêmica focada em Agricultura de Precisão de ultrabaixo custo. O objetivo do pipeline é estimar a massa fresca do milho silagem de forma não-destrutiva, extraindo características fenológicas através de imagens RGB convencionais e aplicando modelos estatísticos simples.

## 📂 Estrutura do Repositório

* `processamento_imagem.py`: Script responsável pelo pré-processamento (OpenCV). Carrega a imagem original, realiza a conversão para o espaço HSV, aplica a limiarização da cor verde e calcula o percentual de área vegetativa útil da amostra.
* `modelo_regressao.py`: Script focado em Machine Learning (Scikit-Learn). Recebe os dados extraídos das imagens e os cruza com a massa real aferida em campo, gerando o modelo de Regressão Linear Simples, extraindo as métricas (R² e RMSE) e plotando o gráfico de calibração.
* `requirements.txt`: Lista de dependências e bibliotecas Python necessárias para rodar o projeto.
* `testphoto1.jpg` e `testphoto2.jpg`: Imagens padronizadas de amostra para validação e teste do algoritmo.

## 🚀 Passo a Passo para Execução (Reprodução do Experimento)

Para garantir o funcionamento correto dos scripts, siga as etapas abaixo na ordem apresentada.

**1. Preparação do Ambiente e Arquivos**
* Faça o download de todos os arquivos deste repositório (via `Download ZIP` ou `git clone`).
* Certifique-se de que as imagens de amostra (`testphoto1.jpg` e `testphoto2.jpg`) estejam na mesma pasta que os scripts Python.
* Instale as bibliotecas necessárias abrindo o seu terminal (ou prompt de comando) e executando:
```bash
pip install -r requirements.txt
