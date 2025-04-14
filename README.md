# 🔐 criptografia_ads.py

**Desenvolvido por Lucas Lemos Pavesi**  
Prova da disciplina **Segurança da Informação** - IFTM - 2025

---

## 📌 Sobre o Projeto
Este projeto é uma ferramenta de linha de comando desenvolvida para criptografar e descriptografar mensagens de forma segura, utilizando criptografia simétrica por blocos.

Foi implementado o algoritmo **AES (Advanced Encryption Standard)** no modo **GCM**, que oferece confidencialidade e integridade, e uma **derivação de chave segura com Scrypt**, resistente a ataques de força bruta.

Todo o sistema foi desenvolvido em **um único arquivo Python (.py)**.

Conforme exigido pela atividade da disciplina, com um menu interativo pelo próprio Terminal, opções para salvar e ler arquivos criptografados, e sem dependências complexas.

---

## 🛠 Tecnologias Utilizadas
- **Python 3.10+**
- Biblioteca [pycryptodome](https://pypi.org/project/pycryptodome/) para operações criptográficas
- AES em modo GCM (Galois/Counter Mode)
- Scrypt para derivação segura da chave

---

## ▶️ Como Executar o Programa

1. Instale a biblioteca necessária:
```bash
pip install pycryptodome
```

2. Execute o script Python:
```bash
python criptografia_ads.py
```

3. Utilize o menu interativo:
- **Criptografar**: Digite uma mensagem e uma chave, e escolha se deseja salvar em arquivo.
- **Descriptografar**: Escolha se deseja ler de um arquivo, insira a chave correta e veja a mensagem original.

---

## ✅ Funcionalidades
- Criptografar mensagens com AES GCM
- Derivar a chave com Scrypt
- Descriptografar mensagens com a mesma chave usada na criptografia
- Salvar mensagens criptografadas em arquivos `.txt`
- Ler mensagens criptografadas de arquivos
- Interface simples via terminal
- Segurança reforçada com `getpass` (a senha não é exibida na digitação)

---

## 💡 Explicação do Funcionamento

1. **Menu principal**: Apresenta opções de criptografar, descriptografar ou sair.
2. **Criptografia**:
   - Solicita uma chave (senha) do usuário, sem exibi-la.
   - Solicita a mensagem de entrada.
   - Gera uma chave segura com base na senha usando Scrypt.
   - Criptografa a mensagem com AES em modo GCM.
   - Exibe o texto criptografado e oferece a opção de salvá-lo em um arquivo.
3. **Descriptografia**:
   - Solicita a chave (senha) do usuário.
   - O usuário pode digitar a mensagem criptografada manualmente ou ler de um arquivo.
   - O sistema decodifica o texto, reconstrói a chave com a senha e descriptografa.
   - Exibe a mensagem original.

---

## 🎥 Demonstração em Vídeo

Assista ao vídeo demonstrando o funcionamento completo do sistema de criptografia:

🔗 [Clique aqui para assistir à demonstração](https://youtu.be/MSAl6fs3nk4)

> O vídeo mostra os processos de criptografia, salvamento em arquivo, leitura e descriptografia interativa, tudo em um único script Python.

---

## 👨‍🎓 Sobre
Este projeto foi desenvolvido como parte da Prova 1 da disciplina de **Segurança da Informação** do curso de **Análise e Desenvolvimento de Sistemas - IFTM**.

**Aluno:** Lucas Lemos Pavesi  
**Professor:** Júnio Moreira  
**Data de Entrega:** 14/03/2025

---

**Repositório privado e de uso exclusivo para fins avaliativos.**

