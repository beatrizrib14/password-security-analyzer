import string
import getpass

def analisar_senha(senha):

    criterios = {
        "Pelo menos 12 caracteres": len(senha) >= 12,
        "Letra maiúscula": any(c.isupper() for c in senha),
        "Letra minúscula": any(c.islower() for c in senha),
        "Número": any(c.isdigit() for c in senha),
        "Caractere especial": any(c in string.punctuation for c in senha)
    }

    print("\n--- RESULTADO DA ANÁLISE ---")

    for criterio, atendido in criterios.items():
        status = "Atendido" if atendido else "Não atendido"
        print(f"{criterio}: {status}")

    pontos = sum(criterios.values())

    if pontos == 5:
        print("\nComposição: Forte")
    elif pontos >= 3:
        print("\nComposição: Moderada")
    else:
        print("\nComposição: Fraca")


print("PASSWORD SECURITY ANALYZER")

senha = getpass.getpass("Digite uma senha para análise: ")

analisar_senha(senha)
