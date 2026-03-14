import cv2
import numpy as np
import os

def redimensionar_manter_proporcao(imagem, largura_max=None, altura_max=None):
    (h, w) = imagem.shape[:2]
    if largura_max is None and altura_max is None: return imagem
    if largura_max is None:
        r = altura_max / float(h)
        dim = (int(w * r), altura_max)
    else:
        r = largura_max / float(w)
        dim = (largura_max, int(h * r))
    return cv2.resize(imagem, dim, interpolation=cv2.INTER_AREA)

def processar_imagem_biomassa(caminho_imagem):
    img = cv2.imread(caminho_imagem)
    if img is None:
        print(f"Erro: Não foi possível carregar a imagem: '{caminho_imagem}'.")
        return

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([15, 10, 10])
    upper_green = np.array([100, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    resultado_segmentado = cv2.bitwise_and(img, img, mask=mask)

    # 1. Calcula o tamanho total da foto 
    total_pixels = mask.shape[0] * mask.shape[1]
    
    # 2. Conta quantos pixels brancos  existem na máscara
    pixels_verdes = cv2.countNonZero(mask) 
    
    # 3. Calcula a porcentagem
    porcentagem_verde = (pixels_verdes / total_pixels) * 100
    
    print("-" * 50)
    print(f"ANÁLISE DA IMAGEM: {caminho_imagem}")
    print(f"Total de pixels na foto: {total_pixels}")
    print(f"Pixels úteis detectados: {pixels_verdes}")
    print(f"-> DADO EXTRAÍDO (Eixo X): {porcentagem_verde:.2f}% de Área Foliar")
    print("-" * 50)

    cv2.imwrite("figura_artigo_1_mascara.jpg", mask)
    cv2.imwrite("figura_artigo_2_fundo_preto.jpg", resultado_segmentado)

    LARGURA_MAX = 800
    ALTURA_MAX = 600
    img_tela = redimensionar_manter_proporcao(img, largura_max=LARGURA_MAX, altura_max=ALTURA_MAX)
    mask_tela = redimensionar_manter_proporcao(mask, largura_max=LARGURA_MAX, altura_max=ALTURA_MAX)
    resultado_tela = redimensionar_manter_proporcao(resultado_segmentado, largura_max=LARGURA_MAX, altura_max=ALTURA_MAX)

    cv2.imshow("1 - Foto Original", img_tela)
    cv2.imshow("2 - Mascara OpenCV", mask_tela)
    cv2.imshow("3 - Planta Segmentada", resultado_tela)

    cv2.waitKey(0) 
    cv2.destroyAllWindows()

if __name__ == "__main__":
    caminho_teste = "testphoto1.jpg"
    
    if os.path.exists(caminho_teste):
        processar_imagem_biomassa(caminho_teste)
    else:
        print(f"Erro: Imagem '{caminho_teste}' não encontrada.")
