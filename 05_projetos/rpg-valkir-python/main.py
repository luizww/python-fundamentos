"""RPG de terminal ambientado na vila de Valkir."""

import random


CLASSES = {
    1: {"nome": "Guardião de Ferro", "hp": 40, "ataque": 10},
    2: {"nome": "Assassino das Sombras", "hp": 22, "ataque": 20},
    3: {"nome": "Paladino Carmesim", "hp": 30, "ataque": 14},
}


def escolher_opcao(mensagem, opcoes_validas):
    """Solicita uma opção até que o jogador informe um valor válido."""

    while True:
        try:
            opcao = int(input(mensagem))
        except ValueError:
            print("Digite apenas o número da opção.")
            continue

        if opcao in opcoes_validas:
            return opcao

        print("Escolha uma das opções disponíveis.")


def combate(jogador, inimigo, permitir_fuga=True):
    """Executa um combate por turnos e retorna True quando o jogador vence."""

    print(f"\n⚔️  {inimigo['nome']} entrou em combate!")

    while jogador["hp"] > 0 and inimigo["hp"] > 0:
        print(
            f"\n{jogador['nome']}: {jogador['hp']} HP | "
            f"{inimigo['nome']}: {inimigo['hp']} HP"
        )

        opcoes = {1, 2} if permitir_fuga else {1}
        mensagem = "[1] Atacar"
        if permitir_fuga:
            mensagem += "\n[2] Tentar fugir"
        mensagem += "\nEscolha: "

        escolha = escolher_opcao(mensagem, opcoes)

        if escolha == 2:
            if random.random() < 0.5:
                print("Você conseguiu escapar.")
                return False
            print("A fuga falhou!")
        else:
            dano = jogador["ataque"]
            if random.random() < 0.20:
                dano *= 2
                print("💥 Golpe crítico!")
            inimigo["hp"] = max(0, inimigo["hp"] - dano)
            print(f"Você causou {dano} de dano.")

        if inimigo["hp"] > 0:
            jogador["hp"] = max(0, jogador["hp"] - inimigo["ataque"])
            print(f"{inimigo['nome']} causou {inimigo['ataque']} de dano.")

    if jogador["hp"] <= 0:
        print("\nSua jornada terminou nas sombras de Valkir.")
        return False

    print(f"\n🏆 Você derrotou {inimigo['nome']}!")
    return True


def criar_jogador():
    """Cria o personagem a partir do nome, classe e item inicial."""

    nome = input("Como Valkir irá conhecer você? ").strip() or "Aventureiro"

    classe_id = escolher_opcao(
        "\nEscolha seu estilo de luta:\n"
        "[1] Guardião de Ferro\n"
        "[2] Assassino das Sombras\n"
        "[3] Paladino Carmesim\n"
        "Escolha: ",
        {1, 2, 3},
    )
    classe = CLASSES[classe_id]

    jogador = {
        "nome": nome,
        "classe": classe["nome"],
        "hp": classe["hp"],
        "hp_max": classe["hp"],
        "ataque": classe["ataque"],
    }

    item = escolher_opcao(
        "\nEscolha um item para a jornada:\n"
        "[1] Botas de couro (+10 HP)\n"
        "[2] Faquinha de serra (+2 de ataque)\n"
        "Escolha: ",
        {1, 2},
    )

    if item == 1:
        jogador["hp"] += 10
        jogador["hp_max"] += 10
    else:
        jogador["ataque"] += 2

    print(
        f"\n{jogador['nome']}, {jogador['classe']} — "
        f"{jogador['hp']} HP e {jogador['ataque']} ATK."
    )
    return jogador


def introducao():
    print(
        """
Valkir é uma vila pacata ao sudoeste do reino de Valdoria.

Depois de uma noite de lua avermelhada, animais desapareceram, plantações
foram destruídas e marcas gigantes surgiram ao redor das casas. Ao cair da
noite, um rugido fez portas tremerem e tochas se apagarem.

Se ninguém enfrentar a criatura, Valkir talvez não sobreviva ao amanhecer.
Você decide partir para salvar a vila.
"""
    )


def jornada():
    introducao()
    jogador = criar_jogador()

    print("\nNo limite da vila, um rato selvagem salta do matagal.")
    enfrentar_rato = escolher_opcao(
        "[1] Lutar\n[2] Desviar e continuar\nEscolha: ",
        {1, 2},
    )

    if enfrentar_rato == 1:
        venceu = combate(
            jogador,
            {"nome": "Rato Selvagem", "hp": 30, "ataque": 3},
        )
        if jogador["hp"] <= 0:
            return
        if venceu:
            jogador["hp"] = jogador["hp_max"]
            print("Após descansar, seu HP foi restaurado.")

    print(
        "\nMais adiante, uma criatura coberta por um líquido escuro bloqueia "
        "o caminho."
    )
    decisao = escolher_opcao(
        "[1] Enfrentar a criatura\n"
        "[2] Tentar conversar\n"
        "[3] Correr em direção a uma casa iluminada\n"
        "Escolha: ",
        {1, 2, 3},
    )

    if decisao == 2:
        print(
            "\nA criatura responde com palavras quebradas: "
            "'carne... corrupção... poder'. Não há acordo possível."
        )
    elif decisao == 3:
        casa = escolher_opcao(
            "\n[1] Entrar na casa\n[2] Continuar correndo\nEscolha: ",
            {1, 2},
        )
        if casa == 1:
            print(
                "\nA porta se fecha no último instante. Um antigo caçador "
                "revela a fraqueza da criatura e ajuda a proteger Valkir. "
                "Você sobreviveu e encontrou um novo aliado."
            )
            return
        print("\nA criatura alcança você na saída da floresta.")

    venceu = combate(
        jogador,
        {"nome": "Criatura Corrompida", "hp": 90, "ataque": 8},
        permitir_fuga=False,
    )

    if venceu:
        print(
            "\nCom a queda da criatura, o silêncio volta à floresta. "
            f"{jogador['nome']} retorna como o novo herói de Valkir."
        )


if __name__ == "__main__":
    jornada()

