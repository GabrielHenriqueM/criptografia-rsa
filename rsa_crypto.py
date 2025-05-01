from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def gerar_chaves():
    chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    chave_publica = chave_privada.public_key()
    return chave_privada, chave_publica

def cifrar_mensagem(mensagem: str, chave_publica):
    mensagem_bytes = mensagem.encode('utf-8')
    return chave_publica.encrypt(
        mensagem_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def decifrar_mensagem(mensagem_cifrada, chave_privada):
    mensagem_decifrada = chave_privada.decrypt(
        mensagem_cifrada,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return mensagem_decifrada.decode('utf-8')

if __name__ == "__main__":
    print("="*50)
    print("PROVA 2 - CRIPTOGRAFIA ASSIMÉTRICA COM RSA")
    print("="*50)

    priv, pub = gerar_chaves()
    print("\nPar de chaves gerado com sucesso!")

    mensagem = "Mensagem Secreta: Feliz Dia do Trabalhador!"
    print(f"\nMensagem original:\n{mensagem}")

    cifrada = cifrar_mensagem(mensagem, pub)
    print(f"\nMensagem cifrada (em bytes):\n{cifrada[:60]}...")

    decifrada = decifrar_mensagem(cifrada, priv)
    print(f"\nMensagem decifrada:\n{decifrada}")

    print("\nProcesso concluído com sucesso!")
    print("="*50)
