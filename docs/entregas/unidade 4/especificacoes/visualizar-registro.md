# Visualizar registro de transplantes

## Histórico de versão

| Data | Versão | Descrição | Autor |
|:----:|:------:|:---------:|:-----:|
| 13/07/23 | 1.0 | Adição de conteúdo | Ana Beatriz Massuh |

## 1. Breve Descrição

O médico chefe acessa o sistema e visualiza uma lista de registros de transplantes, podendo filtrar, ordenar ou pesquisar por algum critério. Ele também pode selecionar um registro para ver mais detalhes ou voltar para a lista.

## 2. Atores

Médico chefe que busca os dados de receptor ou doador

## 3. Condições prévias

O médico chefe está logado no sistema e há registros de transplantes cadastrados.

## 4. Fluxo Básico (FB)

- O médico chefe seleciona a opção de visualizar registros de transplantes.
- O sistema exibe uma lista de registros de transplantes, contendo informações como data, tipo, doador, receptor.
- O médico chefe pode filtrar, ordenar ou pesquisar os registros por algum critério.
- O médico chefe pode selecionar um registro para ver mais detalhes.
- O médico chefe pode voltar para a lista de registros ou encerrar a visualização.

## 5. Fluxo alternativo (FA)

Se não houver registros de transplantes cadastrados, o sistema exibe uma mensagem informando isso e solicita que o médico chefe cadastre ou importe os dados.
Resultado esperado: O médico chefe visualiza os registros de transplantes.

## 6. Fluxo de exceção (FE)

- O médico chefe seleciona a opção de visualizar registros de transplantes.
- O sistema tenta acessar o banco de dados, mas encontra uma falha de conexão ou indisponibilidade do serviço.
- O sistema exibe uma mensagem de erro informando o problema e pedindo que o médico chefe tente novamente mais tarde ou contate o suporte técnico.
- O médico chefe pode tentar novamente ou encerrar a visualização..

## 7. Regra de Negócio (RN)

- Somente o médico chefe pode visualizar os registros de transplantes.
- Os registros de transplantes devem conter informações obrigatórias como data, tipo, doador, receptor e status.
- Os registros de transplantes devem ser armazenados em um banco de dados seguro e confiável.
- Os registros de transplantes devem ser atualizados sempre que houver alguma alteração no status do transplante.
- Os registros de transplantes devem seguir as normas éticas e legais de doação e recepção de órgãos.
- Os registros de transplantes devem ser protegidos contra acesso não autorizado ou adulteração.

## 8. Pós-condições

Não se aplica
