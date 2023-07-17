# Buscar dados de um doador/receptor

## Histórico de versão

| Data | Versão | Descrição | Autor |
|:----:|:------:|:---------:|:-----:|
| 13/07/23 | 1.0 | Adição de conteúdo | João Pedro Morbeck |

## 1. Breve Descrição

Este caso de uso é para quando o usuário atuando como médico ou médico chefe, faz uma busca pelos dados de um doador ou de um receptor, o intuito de realizar a busca é para a visualização, atualização ou exclusão de dados, além de comparar dados de outro receptor ou doador e aprovar ou não o transplante.

## 2. Atores

- 2.1 Médico que busca os dados de receptor ou doador
- 2.2 Médico chefe que busca os dados de receptor ou doador
- 3. Condições prévias
- 3.1 Usuário atuando como Médico ou médico chefe deverá realizar login
- 4. Fluxo Básico (FB)
- 4.1 Usuário seleciona a opção de buscar
- 4.2 O sistema disponibiliza uma lista com todos os receptores e doadores (FA02)(FA03)(RN01)
- 4.3 O usuário digita a informação em que deseja buscar (FA01)
- 4.4 O usuário seleciona a busca
- 4.5 O sistema disponibiliza uma tabela com doadores e receptores que possuem a informação buscada (FE01)
- 4.6 O usuário seleciona o doador ou receptor que procura
- 4.7 O sistema disponibiliza uma página com todos os dados do doador ou receptor selecionado

## 5. Fluxo alternativo (FA)

### FA01 - Busca com filtro

- 5.1.1 O usuário seleciona o filtro que deseja aplicar (RN02)
- 5.1.2 O usuário seleciona a busca
- 5.1.3 O sistema irá realizar a busca, filtrando os dados informados e disponibilizando em uma tabela
- 5.1.4 O usuário seleciona o doador ou receptor que procura
- 5.1.5 O sistema disponibiliza uma página com todos os dados do doador ou receptor selecionado

### FA02 - Busca de doadores

- 5.2.1 O usuário seleciona a opção de disponibilizar apenas doadores (RN02)
- 5.2.2 O sistema irá disponibilizar uma tabela com apenas os doadores
- 5.2.3 O usuário digita a informação em que deseja buscar (FA01)
- 5.2.4 O usuário seleciona a busca
- 5.2.5 O sistema disponibiliza uma tabela com doadores que possuem a informação buscada
- 5.2.6 O usuário seleciona o doador ou receptor que procura
- 5.2.7 O sistema disponibiliza uma página com todos os dados do doador selecionado

### FA03 - Busca de receptores

- 5.3.1 O usuário seleciona a opção de disponibilizar apenas receptores (RN02)
- 5.3.2 O sistema irá disponibilizar uma tabela com apenas os receptores
- 5.3.3 O usuário digita a informação em que deseja buscar (FA01)
- 5.3.4 O usuário seleciona a busca
- 5.3.5 O sistema disponibiliza uma tabela com receptores que possuem a informação buscada
- 5.3.6 O usuário seleciona o doador ou receptor que procura
- 5.3.7 O sistema disponibiliza uma página com todos os dados do receptor selecionado

## 6. Fluxo de exceção (FE)

### FE01 - Doador/Receptor buscado não existe

- 6.1 Usuário seleciona a opção de buscar
- 6.2 O sistema disponibiliza uma lista com todos os receptores e doadores
- 6.3 O usuário digita a informação em que deseja buscar (FA01)
- 6.4 O usuário seleciona a busca
- 6.5 O sistema não encontra nenhum dado com a informação desejada
- 6.6 O sistema apresenta uma mensagem de erro, indicando que nenhum doador ou receptor foi encontrado
- 6.7 O sistema oferece a opção de acrescentar um novo doador ou receptor (RN03)

## 7. Regra de Negócio (RN)

### RN01 - Acesso a todos os dados de doador/receptor

No passo 4.2 do fluxo básico, quando o usuário seleciona a opção de buscar, todos os doadores e receptores estarão disponibilizados para visualização.
RN02 - Filtragem de dados de doador/receptor</br></br>

Nos passos 5.1.1 do FA01, 5.2.1 do FA02 e 5.3.1 do FA03, o usuário têm opções de filtros para facilitar a busca.
RN03 - Adicionar novo doador/receptor</br></br>

No passo 6.7 do FE01, quando nenhum doador/receptor é encontrado, surge uma opção de acrescentar um novo doador/receptor e está opção leva para a inserção de paciente.

## 8. Pós-condições

Não se aplica
