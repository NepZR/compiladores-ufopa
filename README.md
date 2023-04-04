<img align="right" src="http://www.ufopa.edu.br/ppge/images/ppge/imagens/Ufopa_braso_PNG_fundo_transparente.png" style="width: 80px;" alt="UFOPA's Logo" />

# Compiladores - Projeto
> Projeto associado e desenvolvido nas aulas de "Compiladores", no Semestre 2022.2 da UFOPA, feito com ❤️ por Lucas Rodrigues (<a href="https://github.com/NepZR/" target="_blank">@NepZR</a>).
> 
#### ⚠️ Disclaimer: o código deste projeto está sendo desenvolvido em paralelo com as aulas e atividades. Este documento (README) será mantido atualizado conforme novas alterações forem realizadas no repositório.

---

### 📂 Códigos e pastas
- `programs`: arquivos de texto/códigos produzidos especificamente para serem processados pelo Compilador em desenvolvimento deste projeto. Seguem o padrão `nome_do_arquivo.dl` - sempre finalizando com a extensão `.dl`. 
- `Project_Java`: projeto original, desenvolvido em Java.
- `Project_Python`: adaptação do `Project_Java` para a Linguagem Python 3 (neste projeto, utilizada a 3.10). Normalmente, esta será a versão **mais atualizada** dentro deste repositório, considerando a **preferência do desenvolvedor**.

---

### 🏗️ Estrutura
> A estrutura será resumida e atualizada conforme o projeto desenvolvido em Python, contudo, ela manterá certo alinhamento para facilitar a abstração para a versão em Java, se necessário.

- Pacote `Project_Python`
  - Executável `DL.py`
    - Funcionalidade: código principal (`main`) para instanciar as classes do projeto, especificar o nome do arquivo a ser lido, e executar os procedimentos associados ao compilador.
  - Pacote `lexer`
    - Classe `Tag`
      - Nome do arquivo: `Tag.py`;
      - Especificidades: classe do tipo `ENUM`;
      - Funcionalidade: fornece as enumerações - Tags - para identificação dos tipos em Tokens processados pelo compilador;
      - Padrão para Tags: `Tag.NOME_TAG`, exemplo: `Tag.LIT_REAL`.
    - Classe `Token`
      - Nome do arquivo: `Token.py`;
      - Funcionalidade: realiza a estruturação dos Tokens, associando a Tag (tipo) e o Lexema (valor) após leitura do compilador;
      - Padrão para Tokens: `<Tag.NOME_TAG, Lexema>`, exemplo: `<Tag.LIT_REAL, 3.1415>`.
    - Classe `Lexer`
      - Nome do arquivo: `Lexer.py`
      - Especificidades: Tabela Hash (`dict`) para associação das palavras e suas respectivas Tags reservadas do compilador (_e.g._ inteiro: `Tag.INT`).
      - Funcionalidade: responsável pela leitura, processamento do código de entrada (com extensão `.dl`), e geração/associação dos Tokens com seus respectivos tipos e valores - `<Tag, Lexema>`, seguindo o padrão descrito na Classe `Token`.

---

### 🚀 Funcionalidades

#### 📚 Analisador Léxico
|  **Tag** |                **Lexema**                 |                       **Token (Exemplo)**                       | **Reservada (Keyword)** |
|:--------:|:-----------------------------------------:|:---------------------------------------------------------------:|:-----------------------:|
|  ASSIGN  |                     =                     |                       `<Tag.ASSIGN, "=">`                       |           Não           |
|    ID    |         Palavras para associação          |  `<Tag.ID, "a">`<br>`<Tag.ID, "soma">`<br>`<Tag.ID, "teste">`   |           Não           |
|    SUM   |                     +                     |                        `<Tag.SUM, "+">`                         |           Não           |
|    SUB   |                     -                     |                        `<Tag.SUB, "-">`                         |           Não           |
|    MUL   |                     *                     |                        `<Tag.MUL, "*">`                         |           Não           |
|    DIV   |                     /                     |                        `<Tag.DIV, "/">`                         |           Não           |
|    OR    |                    \|                     |                        `<Tag.OR, "\|">`                         |           Não           |
|    AND   |                     &                     |                        `<Tag.AND, "&">`                         |           Não           |
|    NOT   |                     !                     |                        `<Tag.NOT, "!">`                         |           Não           |
|    NE    |                    !=                     |                        `<Tag.NE, "!=">`                         |           Não           |
|    LT    |                     <                     |                         `<Tag.LT, "<">`                         |           Não           |
|    LE    |                    <=                     |                        `<Tag.LE, "<=">`                         |           Não           |
|    GT    |                     >                     |                         `<Tag.GT, ">">`                         |           Não           |
|    GE    |                    >=                     |                        `<Tag.GE, ">=">`                         |           Não           |
|  COMMENT |          Linhas iniciadas com //          |   `<Tag.COMMENT, "// Teste">`<br>`<Tag.COMMENT, "//abcdef">`    |           Não           |
|   SEMI   |                     ;                     |                        `<Tag.SEMI, ";">`                        |           Não           |
|   COMMA  |                     ,                     |                       `<Tag.COMMA, ",">`                        |           Não           |
|  LPAREN  |                     (                     |                       `<Tag.LPAREN, "(">`                       |           Não           |
|  RPAREN  |                     )                     |                       `<Tag.RPAREN, ")">`                       |           Não           |
|  LIT_INT |        Números inteiros, sem ponto        |         `<Tag.LIT_INT, "15">`<br>`<Tag.LIT_INT, "28">`          |           Não           |
| LIT_REAL | Números reais, decimal separado por ponto |      `<Tag.LIT_REAL, "3.1415">`<br>`<Tag.LIT_REAL, "15.">`      |           Não           |
|  PROGRAM |                 programa                  |                   `<Tag.PROGRAM, "programa">`                   |         **Sim**         |
|   BEGIN  |                  inicio                   |                     `<Tag.BEGIN, "inicio">`                     |         **Sim**         |
|    END   |                    fim                    |                       `<Tag.END, "fim">`                        |         **Sim**         |
|    INT   |                  inteiro                  |                     `<Tag.INT, "inteiro">`                      |         **Sim**         |
|   REAL   |                   real                    |                      `<Tag.REAL, "real">`                       |         **Sim**         |
|   BOOL   |                 booleano                  |                     `<Tag.BOOL, "booleano">`                     |         **Sim**         |
|   TRUE   |                verdadeiro                 |                   `<Tag.TRUE, "verdadeiro">`                     |         **Sim**         |
|   FALSE  |                   falso                   |                     `<Tag.FALSE, "falso">`                      |         **Sim**         |
|   READ   |                   leia                    |                      `<Tag.READ, "leia">`                       |         **Sim**         |
|   WRITE  |                  escreva                  |                    `<Tag.WRITE, "escreva">`                     |         **Sim**         |
|    EOF   |                    -1                     |                        `<Tag.EOF, "-1">`                        |           Não           |
|    UNK   |  Tags desconhecidas ou não implementadas  |                        `<Tag.UNK, ".">`                         |           Não           |

---

<h3 style="text-align: justify;">
  👨🏻‍💻 Developer/Maintainer
</h3>

<table style="display: flex;">
  <tr>
    <td align="center"><a href="https://github.com/NepZR"><img style="width: 150px; height: 150;" src="https://avatars.githubusercontent.com/u/37887926" width="100px;" alt=""/><br /><sub><b>Lucas Darlindo Freitas Rodrigues</b></sub></a><br /><sub><b>Data Engineer | Python Dev.</sub></a><br /><a href="https://www.linkedin.com/in/lucasdfr"><sub><b>LinkedIn (lucasdfr)</b></sub></a></td>
  </tr>
<table>