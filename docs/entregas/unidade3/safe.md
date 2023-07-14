# SAFe

## Introdução

O SAFe é um framework complexo de gestão de empresas, para esta disciplina iremos utilizar a gestão de requisitos para definir o tema, épico, capacidade, funcionalidade e histórias de usuário do projeto.

## Tema

Gestão, análise e armazenamento de dados de receptores, doadores e transplantes de rins

## Épicos

- EP01 - Gestão de Dados
- EP02 - Análise de Dados

## Capacidades

| **Épico** | **Capacidade 1**                   | **Capacidade 2**             | **Capacidade 3**                |  
|:---------:|:----------------------------------:|:----------------------------:|:-------------------------------:|
| EP01      | CP01 - Coleta de dados             | CP02 - Manipulação de dados  | CP03 - Registro de dados        |
| EP02      | CP04 - Análise automática de dados | CP05 - Visualização de dados | -                               |

## Funcionalidades

| **Épico** | **Capacidade**                     | **Funcionalidade 1**            | **Funcionalidade 2**                     |
|:---------:|:----------------------------------:|:-------------------------------:|:----------------------------------------:|
| EP01      | CP01 - Coleta de dados             | F01 - Extração de dados de PDF  | F02 - Inserção de dados                  |
| EP01      | CP02 - Manipulação de dados        | F03 - Atualização de dados      | F04 - Exclusão de dados                  |
| EP01      | CP03 - Registro de dados           | F05 - Registro de transplantes  | F06 - Registro de autorizações           |
| EP02      | CP04 - Análise automática de dados | F07 - Busca por compatibilidade | F08 - Cálculo de grau de compatibilidade |
| EP02      | CP05 - Visualização de dados       | F09 - Apresentação de dados     | F10 - Download dos dados                 |

## Histórias de usuário

| **Épico** | **Capacidade** | **Funcionalidade** | **História de usuário**                     |
|:---------:|:--------------:|:------------------:|:-------------------------------------------:|
| EP01      | CP01           | F01                | Eu como médico, gostaria de extrair os dados a partir de um arquivo PDF, para que possa agilizar o processo |
| EP01      | CP01           | F01                | Eu como médico, gostaria de editar os dados extraídos de um arquivo PDF, para que eu faça correções caso necessário |
| EP01      | CP01           | F02                | Eu como médico, gostaria de registrar um receptor no sistema, para que o sistema armazene os dados para mim |
| EP01      | CP01           | F02                | Eu como médico, gostaria de registrar um doador no sistema, para que o sistema armazene os dados para mim |
| EP01      | CP02           | F03                | Eu como médico, gostaria de alterar os dados de um receptor, para caso haja alterações nos seus dados |
| EP01      | CP02           | F03                | Eu como médico, gostaria de alterar os dados de um doador, para caso haja alterações nos seus dados |
| EP01      | CP02           | F03                | Eu como médico, gostaria de aprovar um transplante, para que o transplante seja autorizado a ser feito |
| EP01      | CP02           | F04                | Eu como médico, gostaria de deletar os dados de um receptor, para caso os dados estejam desatualizados e não serão utilizados|
| EP01      | CP02           | F04                | Eu como médico, gostaria de deletar os dados de um receptor, para caso os dados estejam desatualizados e não serão utilizados|
| EP01      | CP03           | F05                | Eu como médico chefe, gostaria de registrar todos os transplantes que foram efetuados, para que eu possa manter o controle do programa de transplantes |
| EP01      | CP03           | F05                | Eu como médico chefe, gostaria de registrar todos os transplantes que foram aprovados, para que eu possa manter o controle do programa de transplantes |
| EP01      | CP03           | F05                | Eu como médico chefe, gostaria de registrar o grau de sucesso de todos os transplantes, para que eu possa manter o controle do programa de transplantes |
| EP01      | CP03           | F06                | Eu como médico chefe, gostaria de registrar quem que aprovou cada transplante, para que eu possa manter a gestão de médicos cirurgiões |
| EP01      | CP03           | F06                | Eu como médico chefe, gostaria de registrar o grau de sucesso de transplantes aprovados por cada médico, para que eu possa manter a gestão de médicos cirurgiões |
| EP02      | CP04           | F07                | Eu como médico, gostaria que o sistema avaliasse a compatibilidade doador-receptor, para que me ajude a tomar uma decisão baseada em dados |
| EP02      | CP04           | F07                | Eu como médico, gostaria de fazer uma busca por receptores compatíveis com um rim específico, para que eu possa fazer uma escolha orientada |
| EP02      | CP04           | F08                | Eu como médico, gostaria que o sistema realizasse os cálculos necessários para identificar a compatibilidade de transplante, para que eu possa fazer um escolha orientada |
| EP02      | CP04           | F08                | Eu como médico, gostaria que o sistema realizasse uma pré-aprovação caso os cálculos estejam corretos, para que me ajude a fazer um trabalho de maneira mais eficiente |
| EP02      | CP05           | F09                | Eu como médico, gostaria que os dados de receptores fossem apresentados para mim em formato de gráficos e tabelas, para que eu possa ver e analisar os registros |
| EP02      | CP05           | F09                | Eu como médico, gostaria que os dados de doadores fossem apresentados para mim em formato de gráficos e tabelas, para que eu possa ver e analisar os registros |
| EP02      | CP05           | F10                | Eu como médico, gostaria de baixar os dados de receptores e doadores em formato PDF, para que eu possa enviar facilmente para minha equipe |
| EP02      | CP05           | F10                | Eu como médico chefe, gostaria de baixar os dados dos registros em formato PDF, para que eu possa enviar facilmente para minha equipe |
