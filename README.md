# 🎵 **YouTube Playlist Downloader to MP3**

[![GitHub Repo](https://img.shields.io/badge/GitHub-Baixar--Musicas--Python-blue?style=for-the-badge&logo=github)](https://github.com/gsfgabi/Baixar-Musicas-Python.git)

---

## 💡 **Motivação do Projeto**

Este projeto foi criado com base em outros exemplos, mas adaptado para atender ao objetivo específico de facilitar o download de músicas e playlists diretamente do YouTube. A ideia é oferecer uma solução prática, que elimine a dependência de sites de terceiros e entregue total controle ao usuário.  

---

## ✨ **Funcionalidades**

- 📥 **Download direto de músicas ou playlists completas** do YouTube.
- 🎶 **Conversão automática para MP3** com qualidade de áudio configurável (192kbps por padrão).
- 📂 **Escolha personalizada da pasta de destino**.
- 🔄 **Robustez contra falhas**: prossegue mesmo se algumas músicas falharem no download.

---

## 🛠️ **Pré-requisitos**

1. **Python 3.7 ou superior**: [Baixe aqui](https://www.python.org/downloads/).  
2. **Instale as dependências necessárias**:
   ```bash
   pip install yt-dlp
   ```
3. **FFmpeg**:  
   - **Baixe o FFmpeg** do site oficial: [Download FFmpeg](https://ffmpeg.org/download.html).
   - Extraia os arquivos e copie a pasta `bin` para um local acessível, como `C:/YOUTUBE/ffmpeg/bin`.  
   - **Adicione o caminho à variável de ambiente do sistema**:  
     1. No Windows, procure por "Variáveis de ambiente".
     2. Edite a variável `Path` e adicione o caminho completo para a pasta `bin`, por exemplo:
        ```plaintext
        C:/YOUTUBE/ffmpeg/bin
        ```
   - Certifique-se de que o caminho do FFmpeg está corretamente configurado no código:
     ```python
     '--ffmpeg-location': 'C:/YOUTUBE/ffmpeg/bin',
     ```

---

## 🚀 **Como usar**

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/gsfgabi/Baixar-Musicas-Python.git
   cd Baixar-Musicas-Python
   ```

2. **Instale o `yt-dlp`**, se ainda não tiver instalado:
   ```bash
   pip install yt-dlp
   ```

3. **Certifique-se de que o FFmpeg está configurado corretamente**.

4. **Execute o script**:
   ```bash
   python main.py
   ```

5. **Insira as informações solicitadas**:
   - **Link da música ou playlist do YouTube**.
   - **Nome da pasta de destino** (ou pressione **Enter** para usar o padrão `downloads`).

---

## 📝 **Exemplo de uso**

### Entrada:
```plaintext
Digite o link da música/playlist do YouTube: https://www.youtube.com/playlist?list=PLxD3ZqsToBRC123456
Digite o nome da pasta de destino (pressione Enter para usar 'downloads'): minhas_musicas
```

### Saída esperada:
```plaintext
Iniciando o download da música/playlist...
Download concluído!
Arquivos MP3 salvos na pasta 'minhas_musicas'.
```

---

## ⚙️ **Configurações no código**

Você pode personalizar as configurações do script editando estas opções no arquivo `main.py`:

- **Qualidade do áudio**:
  ```python
  'preferredquality': '192',  # Modifique para 128 ou 320 conforme necessário.
  ```
- **Formato do arquivo**:
  ```python
  'preferredcodec': 'mp3',  # Altere para outro formato, como 'wav' ou 'aac', se preferir.
  ```
- **Nome do arquivo gerado**:
  ```python
  'outtmpl': f'{output_dir}/%(title)s.%(ext)s',  # Modifique o padrão do nome do arquivo.
  ```

---

**Nota**: Use o script de forma responsável, respeitando os direitos autorais e os Termos de Uso do YouTube.  
