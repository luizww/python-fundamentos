# Projetos em Python

Programas que combinam os fundamentos estudados em jogos, simulações e automações.

| Projeto | O que faz | Conceitos praticados |
| --- | --- | --- |
| [Sistema bancário](sistema_bancario/main.py) | Depósitos, saques e extrato no terminal | Funções, validações, listas e tuplas |
| [Valkir — RPG de terminal](rpg_valkir/) | Aventura com classes e combate por turnos | Dicionários, decisões e aleatoriedade |
| [TikTok PDF Organizer](pdf_organizer/) | Pareia etiquetas e DANFEs pelo rastreio | PDFs, interface gráfica e testes |
| [Adivinhe o número](adivinhe_numero/main.py) | Jogo de adivinhação | Condicionais e números aleatórios |
| [Pedra, papel e tesoura](pedra_papel_tesoura/main.py) | Jogo contra o computador | Condicionais e entradas do usuário |

## Executar

Na raiz do repositório:

```bash
python projetos/sistema_bancario/main.py
python projetos/rpg_valkir/main.py
```

Para o aplicativo de PDFs, consulte as [instruções de instalação](pdf_organizer/README.md#como-executar). Ele possui dependências próprias; os exercícios não precisam delas.

## Organização

Cada projeto possui sua própria pasta. O arquivo main.py inicia o programa; documentação, dependências e testes ficam junto do projeto.

O sistema bancário mantém os dados em memória e limita três saques por execução; ainda não possui persistência nem controle por data.

[← Voltar à página inicial](../README.md)
