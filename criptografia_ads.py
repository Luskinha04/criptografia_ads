# criptografia_ads.py
# Desenvolvido por Lucas Lemos Pavesi - Prova de Segurança da Informação

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import base64
import getpass
import os


# Função para limpar o terminal
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# Função para exibir o cabeçalho visual do sistema
def mostrar_logo():
    print("=" * 70)
    print("SISTEMA DE CRIPTOGRAFIA AES - PROVA DE SEGURANÇA DA INFORMAÇÃO")
    print("Desenvolvido por Lucas Lemos Pavesi - IFTM - 2025")
    print("=" * 70)


# Função para criptografar mensagem com AES GCM + Scrypt
def criptografar_avancado(mensagem: str, senha: str) -> str:
    salt = get_random_bytes(16)
    chave = hashlib.scrypt(senha.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
    cipher = AES.new(chave, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(mensagem.encode())

    partes = {
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "salt": base64.b64encode(salt).decode(),
        "nonce": base64.b64encode(cipher.nonce).decode(),
        "tag": base64.b64encode(tag).decode(),
    }
    return "*".join(partes.values())


# Função para descriptografar mensagem cifrada
def descriptografar_avancado(texto_criptografado: str, senha: str) -> str:
    try:
        partes = texto_criptografado.split("*")
        if len(partes) != 4:
            return "\n⚠ Erro: formato inválido da mensagem criptografada."

        ciphertext, salt, nonce, tag = map(base64.b64decode, partes)
        chave = hashlib.scrypt(senha.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
        cipher = AES.new(chave, AES.MODE_GCM, nonce=nonce)
        texto = cipher.decrypt_and_verify(ciphertext, tag)
        return texto.decode()
    except Exception:
        return "\n⚠ Erro: a senha está incorreta ou os dados estão corrompidos."


# Função para salvar mensagem criptografada em um arquivo
def salvar_em_arquivo(nome_arquivo: str, conteudo: str):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)


# Função para ler mensagem criptografada de um arquivo
def ler_de_arquivo(nome_arquivo: str) -> str:
    if not os.path.exists(nome_arquivo):
        return ""
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.read()


# Modo de criptografar
def criptografar_modo():
    senha = getpass.getpass("Digite a chave de criptografia: ")
    mensagem = input("Digite a mensagem a ser criptografada: ")
    resultado = criptografar_avancado(mensagem, senha)
    print("\n🔒 Mensagem criptografada com sucesso!")
    print(f"Resultado: {resultado}")
    salvar = input("\nDeseja salvar a mensagem em um arquivo? (s/n): ").lower()
    if salvar == "s":
        nome = input("Digite o nome do arquivo (ex: mensagem.txt): ")
        salvar_em_arquivo(nome, resultado)
        print("Arquivo salvo com sucesso!")
    input("\nPressione Enter para voltar ao menu...")


# Modo de descriptografar
def descriptografar_modo():
    senha = getpass.getpass("Digite a chave de descriptografia: ")
    escolha = input("Deseja ler a mensagem de um arquivo? (s/n): ").lower()
    if escolha == "s":
        nome = input("Digite o nome do arquivo (ex: mensagem.txt): ")
        mensagem_cifrada = ler_de_arquivo(nome)
        if mensagem_cifrada == "":
            print("\n⚠ Erro: arquivo não encontrado ou vazio.")
            input("\nPressione Enter para voltar ao menu...")
            return
    else:
        mensagem_cifrada = input("Digite a mensagem criptografada: ")

    resultado = descriptografar_avancado(mensagem_cifrada, senha)
    if resultado.startswith("\n⚠ Erro"):
        print(resultado)
    else:
        print("\n🔓 Mensagem descriptografada com sucesso!")
        print(f"Resultado: {resultado}")
    input("\nPressione Enter para voltar ao menu...")


# Menu interativo
def menu():
    while True:
        limpar_tela()
        mostrar_logo()
        print("1 - Criptografar mensagem")
        print("2 - Descriptografar mensagem")
        print("0 - Sair")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            criptografar_modo()
        elif escolha == "2":
            descriptografar_modo()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")


# Execução principal do programa
if __name__ == "__main__":
    menu()
