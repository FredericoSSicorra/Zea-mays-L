import cv2
import numpy as np

def processar_imagem_biomassa(caminho_imagem):
    img = cv2.imread(caminho_imagem)

    if img is None:
        print(f"Erro: Não foi possível carregar a imagem no caminho '{caminho_imagem}'.")
        return

    # Conversão do espaço de cores BGR para HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Calibração dos limiares de cor 
    lower_green = np.array([15, 10, 10])
    upper_green = np.array([100, 255, 255])
    
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Extração apenas do material vegetativo útil 
    resultado_segmentado = cv2.bitwise_and(img, img, mask=mask)

    # Salvar as imagens processadas para análise
    cv2.imwrite("figura_artigo_1_mascara.jpg", mask)
    cv2.imwrite("figura_artigo_2_fundo_preto.jpg", resultado_segmentado)

    # Debug
    dimensao_tela = (600, 800)
    img_tela = cv2.resize(img, dimensao_tela)
    mask_tela = cv2.resize(mask, dimensao_tela)
    resultado_tela = cv2.resize(resultado_segmentado, dimensao_tela)

    cv2.imshow("1 - Foto Original", img_tela)
    cv2.imshow("2 - Mascara OpenCV (Calibrada)", mask_tela)
    cv2.imshow("3 - Planta Segmentada", resultado_tela)

    cv2.waitKey(0) 
    cv2.destroyAllWindows()

if __name__ == "__main__":
    caminho_teste = "./dados/amostra_milho_01.jpg" 
    
    print("Iniciando processamento da imagem...")
    processar_imagem_biomassa(caminho_teste)
    print("Processamento concluído. Imagens salvas no diretório atual.")