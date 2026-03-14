import cv2
import numpy as np
import os

def redimensionar_manter_proporcao(imagem, largura_max=None, altura_max=None):
    (h, w) = imagem.shape[:2]
    
    if largura_max is None and altura_max is None:
        return imagem
        
    if largura_max is None:
        r = altura_max / float(h)
        dim = (int(w * r), altura_max)
    else:
        r = largura_max / float(w)
        dim = (largura_max, int(h * r))
        
    imagem_redimensionada = cv2.resize(imagem, dim, interpolation=cv2.INTER_AREA)
    return imagem_redimensionada

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

    resultado_segmentado = cv2.bitwise_and(img, img, mask=mask)

    cv2.imwrite("figura_artigo_1_mascara.jpg", mask)
    cv2.imwrite("figura_artigo_2_fundo_preto.jpg", resultado_segmentado)

    # Debug
    LARGURA_MAX_TELA = 800 
    ALTURA_MAX_TELA = 600
    
    img_tela = redimensionar_manter_proporcao(img, largura_max=LARGURA_MAX_TELA, altura_max=ALTURA_MAX_TELA)
    mask_tela = redimensionar_manter_proporcao(mask, largura_max=LARGURA_MAX_TELA, altura_max=ALTURA_MAX_TELA)
    resultado_tela = redimensionar_manter_proporcao(resultado_segmentado, largura_max=LARGURA_MAX_TELA, altura_max=ALTURA_MAX_TELA)

    cv2.imshow("1 - Foto Original", img_tela)
    cv2.imshow("2 - Mascara OpenCV (Calibrada)", mask_tela)
    cv2.imshow("3 - Planta Segmentada", resultado_tela)

    cv2.waitKey(0) 
    cv2.destroyAllWindows()

if __name__ == "__main__":
    caminho_teste = "./dados/amostra_milho_01.jpg"
    
    if not os.path.exists("./dados"):
        os.makedirs("./dados")
        print("Pasta './dados' criada. Coloque sua imagem lá e renomeie para 'amostra_milho_01.jpg'.")
    
    if os.path.exists(caminho_teste):
        print("Iniciando processamento da imagem...")
        processar_imagem_biomassa(caminho_teste)
        print("Processamento concluído. Imagens salvas no diretório atual.")
    else:
        print(f"Erro: Imagem de teste não encontrada em '{caminho_teste}'.")
        print("Certifique-se de que a imagem está na pasta './dados'.")
