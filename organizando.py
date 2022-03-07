import os


#1 Criar pasta para organização
# pasta para: Imagens, Audios, Videos, Documentos e Outros

#2 Pegar nome dos arquivos

#3 Determinando tipo de arqiuvo pela extensão

#4 Mover arquivos para as pastas correspondentes


audios_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.mov', '.avi', '.gif', '.jfif']
imagens_ext = ['.jpg', '.jpeg', '.png']
documentos_ext = ['.txt', '.log', '.pdf', '.doc', '.docx', '.csv', '.xls', '.xlsx', '.pptx']



def pegar_extensao(nome):
	index = nome.rfind('.')
	return nome[index:]



def organiza(diretorio):
	AUDIO_DIR = os.path.join(diretorio, 'audios')
	IMAGENS_DIR = os.path.join(diretorio, 'imagens')
	DOCS_DIR = os.path.join(diretorio, 'documentos')
	VIDEOS_DIR = os.path.join(diretorio, 'videos')
	OUTROS_DIR = os.path.join(diretorio, 'outros')

	if not os.path.isdir(AUDIO_DIR):
		os.mkdir(AUDIO_DIR)
	if not os.path.isdir(IMAGENS_DIR):
		os.mkdir(IMAGENS_DIR)
	if not os.path.isdir(DOCS_DIR):
		os.mkdir(DOCS_DIR)
	if not os.path.isdir(VIDEOS_DIR):
		os.mkdir(VIDEOS_DIR)
	if not os.path.isdir(OUTROS_DIR):
		os.mkdir(OUTROS_DIR)


	nome_arquivos = os.listdir(diretorio)
	nova_pasta = ''
	for arquivo in nome_arquivos:
		if os.path.isfile(os.path.join(diretorio, arquivo)):
			#Extensão do arquivo com letras minusculas rs
			extensao = str.lower(pegar_extensao(arquivo))
			print(arquivo, extensao)
			if extensao in audios_ext:
				nova_pasta = AUDIO_DIR
			elif extensao in videos_ext:
				nova_pasta = VIDEOS_DIR
			elif extensao in imagens_ext:
				nova_pasta = IMAGENS_DIR
			elif extensao in documentos_ext:
				nova_pasta = DOCS_DIR
			else:
				nova_pasta = OUTROS_DIR
			#move o arquivo para a pasta correspondente 
			velho = os.path.join(diretorio, arquivo)
			novo = os.path.join(nova_pasta, arquivo)
			os.rename(velho, novo)
			print('Moveu:', velho,'-->', novo)


if __name__ == '__main__':
	organiza('Livros')	 





