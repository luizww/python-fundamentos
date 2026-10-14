# Projetos em Python

Programas que combinam os fundamentos estudados em jogos, simulações e automações.

| Projeto | O que faz | Conceitos praticados |
| --- | --- | --- |
| [Sistema bancário](sistema_bancario.py) | Depósitos, saques e extrato no terminal | Funções, validações, listas e tuplas |
| [Valkir — RPG de terminal](rpg-valkir-python/) | Aventura com classes e combate por turnos | Dicionários, decisões e aleatoriedade |
| [TikTok PDF Organizer](tiktok-pdf-organizer/) | Pareia etiquetas e DANFEs pelo rastreio | PDFs, interface gráfica e testes |
| [Adivinhe o número](adivinhe_numero.py) | Jogo de adivinhação | Condicionais e números aleatórios |
| [Pedra, papel e tesoura](pedra_papel_tesoura.py) | Jogo contra o computador | Condicionais e entradas do usuário |

## Executar

Na raiz do repositório:

```bash
python 05_projetos/sistema_bancario.py
python 05_projetos/rpg-valkir-python/main.py
```

Para o aplicativo de PDFs, consulte as [instruções de instalação](tiktok-pdf-organizer/README.md#como-executar). Ele possui dependências próprias; os exercícios não precisam delas.

## Organização

Programas de um único arquivo ficam diretamente nesta pasta. Projetos com documentação, dependências ou testes possuem uma subpasta própria.

O sistema bancário mantém os dados em memória e limita três saques por execução; ainda não possui persistência nem controle por data.

[← Voltar à página inicial](../README.md)
