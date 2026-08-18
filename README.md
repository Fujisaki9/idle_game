# ⚔️ Idle Game RPG

Um jogo RPG idle desenvolvido em console como projeto de aprendizado de **Programação Orientada a Objetos (POO)** em 
Python.

É um jogo de texto em console, onde o jogador evolui seu herói, enfrenta inimigos, coleta materiais e aprimora 
equipamentos ao longo de diferentes zonas.

---

## 📋 Sobre o projeto

Criei esse projeto para praticar os fundamentos da POO. Foi meu primeiro contato com o tema e, como gosto de jogos, 
decidi fazer um.

## 🛠️ Tecnologias e Bibliotecas utilizadas

- **Linguagem:** `Python`
- **Bibliotecas:** `rich` (formatação visual e exibição) e algumas bibliotecas nativas.
- **Ambiente:** PyCharm

---

## ⚙️ Funcionalidades

- **Sistema de combate** — Combate em turnos contra inimigos e bosses com cálculo de dano variável.
- **Zonas** — 9 zonas com dificuldade crescente, cada uma com inimigos e um boss final.
- **Progressão do herói** — Sistema de XP e níveis com ganho de atributos.
- **Inventário** — Coleta e gerenciamento de materiais dropados pelos inimigos.
- **Codex** — Sistema de coleções com recompensas específicas permanentes.
- **Forja** — Sistema de craft de equipamentos épicos, únicos e lendários.
- **Aprimoramento** — Sistema de upgrade de equipamentos com progressão de atributos por nível.
- **Save/Load** — Salvamento automático do progresso em arquivo `.json`.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python** instalado.
2. Clone o repositório: `git clone https://github.com/Fujisaki9/idle_game.git`.
3. Instale as dependências: `pip install rich`.
4. Execute o programa: `python main.py`

-> ⚠️ **PyCharm:** Habilite *Emulate terminal in output* em `Run > Edit configurations > Edit configuration templates >
 Python > Modify options` para visualizar a interface colorida.

---

## Aprendizados

- Fundamentos da POO: classes, herança, encapsulamento (getters/setters), composição. Tentei encaixar abstração e 
- polimorfismo, mas ainda estou buscando os lugares certos para aplicá-los.
- Funcionalidades de algumas bibliotecas.
- Validação de inputs do usuário.
- Organização do código em múltiplos arquivos.
- Sistema de save utilizando arquivo .json.

Desenvolvido por **Celso Henrique Pereira Benassi**.