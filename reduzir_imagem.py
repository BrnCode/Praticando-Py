import os 
from PIL import Image

def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('jpg'):
        return True
    return False

def reduzir_tamanho_imagens(input_dir, output_dir, ext='.jpg'): #ext='.jpg' é o formato padrão para as imagens redimencionadas
    lista_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    for nome in lista_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')
        redimencionada = imagem.resize((600, 600))
        nome_sem_ext = os.path.splitext(nome)[0]
        redimencionada.save(os.path.join(output_dir, nome_sem_ext + ext ))
     # print(lista_arq uivos)
print('')
print('Suas imagens foram redimecionadas rs')
print('')

if __name__ == "__main__":
    diretorio = 'C:\\Users\\bruno\\OneDrive\\Área de Trabalho\\imag'
    reduzir_tamanho_imagens(diretorio, 'output')
  