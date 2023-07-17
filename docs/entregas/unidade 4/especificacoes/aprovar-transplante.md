# Aprovar transplante

## Histórico de versão

| Data | Versão | Descrição | Autor |
|:----:|:------:|:---------:|:-----:|
| 13/07/23 | 1.0 | Adição de conteúdo | Bruno Martins Valério Bomfim |

## 1. Breve Descrição

Este caso de uso é para quando o usuário atuando como médico ou médico-chefe, faz o teste de compatibilidade entre um doador e vários receptores, ou vários doadores e um receptor - e então decide se irá aceitar ou recusar a entrega de um órgão para um determinado receptor.

## 2. Atores

- 2.1 Médico que aceita/recusa um rim depois do teste de compatibilidade.
- 2.2 Médico-chefe que aceita/recusa um rim depois do teste de compatibilidade.

## 3. Condições prévias

- 3.1 O médico ou médico-chefe deverá estar logado, e o teste de compatibilidade deverá ter sido feito.

## 4. Fluxo Básico (FB)

- 4.1 O usuário (médico/médico-chefe) faz o login no sistema.
- 4.2 O usuário seleciona o subitem “Realizar teste” no menu “Compatibilidade”.
- 4.3 O usuário seleciona no menu de doadores, um específico.
- 4.4 O usuário seleciona no menu de receptores, um específico.
- 4.5 O usuário clica no botão “Pesquisar”.
- 4.6 O sistema devolve uma div com a resposta prévia, se o receptor é compatível ou incompatível.
- 4.7 O médico clica no botão “Detalhar”, para conferir informações mais específicas.
- 4.8 O médico observa informações mais detalhadas sobre o teste.
- 4.9 O médico decide se irá aceitar ou recusar o órgão através de um dropdown (Aceitar/Recusar).
- 4.10 O médico descreve os motivos de aceitação ou recusa.
- 4.11 O médico clica no botão “Registrar” para mandar as informações para o sistema.

## 5. Fluxo alternativo (FA)

### FA01 - Comparar 1 doador com vários receptores

- 5.1.1 O usuário (médico/médico-chefe) faz o login no sistema.
- 5.1.2 O usuário seleciona o subitem “Realizar teste” no menu “Compatibilidade”.
- 5.1.3 O usuário seleciona no menu de doadores, um específico.
- 5.1.4 O usuário seleciona no menu de receptores, “Todos”.
- 5.1.5 O usuário clica no botão “Pesquisar”.
- 5.1.6 O sistema devolve uma lista com a resposta prévia, se os receptores são compatíveis ou incompatíveis.
- 5.1.7 O médico clica no botão “Detalhar”, para conferir informações mais específicas.
- 5.1.8 O médico observa informações mais detalhadas sobre o teste.
- 5.1.9 O médico decide se irá aceitar ou recusar o órgão através de um dropdown (Aceitar/Recusar).
- 5.1.10 O médico descreve os motivos de aceitação ou recusa.
- 5.1.11 O médico clica no botão “Registrar” para mandar as informações para o sistema.

### FA02 - Comparar vários doadores com 1 receptor

- 5.2.1 O usuário (médico/médico-chefe) faz o login no sistema.
- 5.2.2 O usuário seleciona o subitem “Realizar teste” no menu “Compatibilidade”.
- 5.2.3 O usuário seleciona no menu de doadores, “Todos”.
- 5.2.4 O usuário seleciona no menu de receptores, um específico.
- 5.2.5 O usuário clica no botão “Pesquisar”.
- 5.2.6 O sistema devolve uma lista com a resposta prévia, se o receptor é compatível ou incompatível.
- 5.2.7 O médico clica no botão “Detalhar”, para conferir informações mais específicas.
- 5.2.8 O médico observa informações mais detalhadas sobre o teste.
- 5.2.9 O médico decide se irá aceitar ou recusar o órgão através de um dropdown (Aceitar/Recusar).
- 5.2.10 O médico descreve os motivos de aceitação ou recusa.
- 5.2.11 O médico clica no botão “Registrar” para mandar as informações para o sistema.

## 6. Fluxo de exceção (FE)

### FE01 - Não existem doadores para comparar

- 6.1 O usuário (médico/médico-chefe) faz o login no sistema.
- 6.2 O usuário seleciona o subitem “Realizar teste” no menu “Compatibilidade”.
- 6.3 O usuário vai até o menu dropdown para selecionar um doador específico, mas não existe nenhum cadastrado no banco de dados.
- 6.4 Aparecerá um label avisando “Não foram encontrados registros de doadores”.

## 7. Regra de Negócio (RN)

- Os registros de transplantes devem conter informações obrigatórias como data, tipo, doador, receptor e status.
- Os registros de transplantes devem ser armazenados em um banco de dados seguro e confiável.
- Os registros de transplantes devem ser atualizados sempre que houver alguma alteração no status do transplante.
- Os registros de transplantes devem seguir as normas éticas e legais de doação e recepção de órgãos.
- Os registros de transplantes devem ser protegidos contra acesso não autorizado ou adulteração.

## 8. Pós-condições

Não se aplica.
