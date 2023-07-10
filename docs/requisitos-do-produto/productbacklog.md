# Backlog de requisitos

>*[Um requisito]* É uma declaração que identifica características ou restrições de um produto ou processo, as quais devem ser atendidas. Podendo ser, por exemplo, operacional, funcional, ou design, sendo inequívoca, testável (verificável) ou mensurável, e necessária para a aceitabilidade do produto ou processo (Dick, Hull, Jackson - Management Aspects of Requirements Engineering, págs. 207-230).

Para melhor visualização dos requisitos, podem ser vistos no nosso [mural](https://app.mural.co/invitation/mural/pessoal3153/1683652401659?sender=u6c0c7e7c95ba7c8ec1686363&key=332ea483-be51-4e1a-84e4-bb1db744dc32) ou nossa [planilha](https://docs.google.com/spreadsheets/d/1ZKEHNyYo_hBxK9R2Sjs1BWzV-quIr_ydlqZIk3Ac8Ew/edit?usp=sharing) de requisitos com o cálculo de priorização

## Épico

| Item | Épico |
| --- | --- |
| EP01 | Extração de informações de um PDF |
| EP02 | Visualização e manipulação de dados |
| EP03 | Comparação entre pacientes |
| EP04 | Relatórios, métricas e log do sistema |

## User Stories

| MVP        | Épico | US   | Descrição resumida da US                                                                                                                                                                                                                                                                                                                                     |
|------------|-------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MVP 02     | EP03  | US01 | Como médico responsável pela decisão final de aceitação ou rejeição de um órgão para transplante, eu quero utilizar o software para avaliar as informações do paciente e do órgão doador e tomar uma decisão informada e precisa, a fim de garantir o sucesso do transplante e a segurança do paciente receptor.                                             |
| Incremento | EP03  | US02 | Como um médico que precisa checar e dar um match em dois pacientes para transplante de órgãos entre eles, eu quero usar o aplicativo para checar os dados do paciente para garantir que eles são compatíveis e seguros para o transplante.                                                                                                                   |
| MVP 01     | EP02  | US03 | Como médico, quero visualizar os dados coletados em dashboards e widgets para poder analisar rapidamente o estado de saúde dos meus pacientes e tomar decisões informadas com base nessas informações.                                                                                                                                                       |
| Incremento | EP03  | US04 | Como um médico responsável por encontrar o receptor ideal para um transplante de órgãos, eu quero utilizar um aplicativo para comparar as informações de diferentes pacientes, usando algoritmos e fórmulas matemáticas, para determinar o receptor mais compatível e aumentar as chances de sucesso do transplante.                                         |
| MVP 01     | EP01  | US05 | Como médico, quero que os dados coletados dos meus pacientes (rins recebidos) sejam armazenados em uma base de dados, para que eu possa visualizá-los facilmente e tomar decisões informadas com base nessas informações.                                                                                                                                    |
| MVP 01     | EP01  | US06 | Como um médico, eu gostaria de ver um painel de controle com informações sobre os dados retirados do PDF, para que eu possa visualizar de forma clara e rápida os dados mais importantes.                                                                                                                                                                    |
| MVP 02     | EP03  | US07 | Como médico que realiza transplantes de rim, eu quero que o sistema produza uma resposta preliminar sobre a aceitação ou não do rim para o paciente receptor, para que eu possa tomar uma decisão rápida e eficiente sobre o transplante.                                                                                                                    |
| MVP 01     | EP04  | US08 | Como médico, quero ter acesso a um sistema que me permita criar, ler, atualizar e excluir relatórios e informações dos rins transplantados de forma rápida e fácil, para que eu possa manter um registro preciso e atualizado do histórico.                                                                                                                  |
| MVP 01     | EP01  | US09 | Como um médico, eu gostaria de poder enviar um documento em formato PDF para o sistema, para que ele possa extrair automaticamente as informações dos pacientes e dos rins a partir desse arquivo, para economizar tempo e evitar erros de digitação.                                                                                                        |
| Incremento | EP03  | US10 | Como um médico responsável por encontrar o receptor ideal para um transplante de rim, eu quero usar um software que gere automaticamente uma lista de possíveis receptores compatíveis com o rim doado. Isso me ajudará a identificar rapidamente os pacientes que têm maior probabilidade de sucesso no transplante e aumentar suas chances de recuperação. |
| MVP 02     | EP01  | US11 | Como um médico, eu gostaria de receber alertas quando o sistema encontrar informações incompletas ou inconsistentes nos documentos em PDF, para que eu possa corrigir esses problemas e garantir a qualidade dos dados.                                                                                                                                      |
| MVP 02     | EP04  | US12 | Como um médico responsável pela gestão de pacientes em lista de espera para transplante de rim, eu quero que o software produza estatísticas, métricas e relatórios para que eu possa avaliar o desempenho do programa e identificar oportunidades de melhoria em relação à alocação de órgãos.                                                              |
| MVP 02     | EP02  | US13 | Como um médico chefe do sistema, eu quero poder acessar a base de dados para visualizar informações estatísticas sobre os transplantes de rim realizados, para que eu possa avaliar a efetividade do sistema e identificar possíveis áreas de melhoria.                                                                                                      |
| Incremento | EP04  | US14 | Como um médico chefe do sistema, eu quero poder acessar os logs do sistema para monitorar as atividades dos usuários, para que eu possa garantir a segurança e a efetividade do sistema.                                                                                                                                                                     |
| Incremento | EP02  | US15 | Como um médico, eu quero poder editar as informações do paciente e do órgão doado caso haja uma mudança significativa em até 2 meses após a inserção dos dados, para manter as informações precisas e atualizadas, sem alterar o relatório final do ano.                                                                                                     |
| MVP 01     | EP02  | US16 | Como um médico, quero poder ver uma lista clara e fácil de entender dos possíveis receptores compatíveis com o rim doado, para que eu possa identificar rapidamente a melhor opção para o transplante.                                                                                                                                                       |
| MVP 02     | EP02  | US17 | Como um médico, quero poder registrar minha decisão de aceitar ou rejeitar o órgão para transplante no sistema, para que outros membros da equipe médica possam ter acesso a essa informação e tomar decisões baseadas nela.                                                                                                                                 |
| MVP 01     | EP02  | US18 | Como um médico, quero ser capaz de alterar os dados que o programa retirou do PDF, pois podem existir dados que foram retirados de maneira errônea e isto afetará na decisão final.                                                                                                                                                                          |
| Incremento | EP01  | US19 | Como um médico chefe do sistema, eu gostaria de poder definir os campos que devem ser extraídos dos documentos em PDF, para que o sistema possa se adaptar a diferentes tipos de documentos e garantir a consistência dos dados.                                                                                                                             |
| Incremento | EP02 | US20 | Como um médico, eu gostaria de poder buscar informações específicas de um paciente ou de um rim, para que eu possa encontrar rapidamente as informações necessárias para tomar uma decisão sobre o transplante. |
| Incremento | EP01 | US21 | Como um médico chefe do sistema, eu gostaria de poder treinar o sistema para reconhecer padrões específicos em documentos em PDF, para que o sistema possa se adaptar a novos tipos de documentos sem a necessidade de intervenção manual. |
| Incremento | EP03 | US22 | Como um médico, eu gostaria de poder filtrar os pacientes por diferentes critérios, como idade, tipo sanguíneo e histórico médico, para que eu possa identificar rapidamente os pacientes que são mais compatíveis com os rins doados. |
| MVP 02 | EP04 | US23 | Como um médico chefe, necessito que seja possível gerar relatórios semestrais e anuais de aceite ou recusa de rins, para que consiga manter um controle diante da postura dos médicos da minha equipe. |

## Backlog do MVP1

| Épico | US | Descrição da User Story |
| --- | --- | --- |
| EP01 | US05 | Como médico, quero que os dados coletados dos meus pacientes sejam armazenados em uma base de dados, para que eu possa visualizá-los facilmente e tomar decisões informadas com base nessas informações.
| EP02 | US18 | Como um médico, quero ser capaz de alterar os dados que o programa retirou do PDF, pois podem existir dados que foram retirados de maneira errônea e isto afetará na decisão final.
| EP01 | US06 | Como um médico, eu gostaria de ver um painel de controle com informações sobre os dados retirados do PDF, para que eu possa visualizar de forma clara e rápida os dados mais importantes.
| EP02 | US03 | Como médico, quero visualizar os dados coletados em dashboards e widgets para poder analisar rapidamente o estado de saúde dos meus pacientes e tomar decisões informadas com base nessas informações.
| EP04 | US08 | Como médico, quero ter acesso a um sistema que me permita criar, ler, atualizar e excluir relatórios e informações dos rins transplantados de forma rápida e fácil, para que eu possa manter um registro preciso e atualizado do histórico.
| EP02 | US16 | Como um médico, quero poder ver uma lista clara e fácil de entender dos possíveis receptores compatíveis com o rim doado, para que eu possa identificar rapidamente a melhor opção para o transplante.
| EP01 | US09 | Como um médico, eu gostaria de poder enviar um documento em formato PDF para o sistema, para que ele possa extrair automaticamente as informações dos pacientes e dos rins a partir desse arquivo, para economizar tempo e evitar erros de digitação.

## Backlog do MVP2
| Épico | US | Descrição da User Story |
| --- | --- | --- |
| EP02 | US17 | Como um médico, quero poder registrar minha decisão de aceitar ou rejeitar o órgão para transplante no sistema, para que outros membros da equipe médica possam ter acesso a essa informação e tomar decisões baseadas nela.
| EP03 | US01 | Como médico responsável pela decisão final de aceitação ou rejeição de um órgão para transplante, eu quero utilizar o software para avaliar as informações do paciente e do órgão doador e tomar uma decisão informada e precisa, a fim de garantir o sucesso do transplante e a segurança do paciente receptor.
| EP03 | US07 | Como médico que realiza transplantes de rim, eu quero que o sistema produza uma resposta preliminar sobre a aceitação ou não do rim para o paciente receptor, para que eu possa tomar uma decisão rápida e eficiente sobre o transplante.
| EP01 | US11 | Como um médico, eu gostaria de receber alertas quando o sistema encontrar informações incompletas ou inconsistentes nos documentos em PDF, para que eu possa corrigir esses problemas e garantir a qualidade dos dados.
| EP04 | US23 | Como um médico chefe, necessito que seja possível gerar relatórios semestrais e anuais de aceite ou recusa de rins, para que consiga manter um controle diante da postura dos médicos da minha equipe.
| EP04 | US12 | Como um médico responsável pela gestão de pacientes em lista de espera para transplante de rim, eu quero que o software produza estatísticas, métricas e relatórios para que eu possa avaliar o desempenho do programa e identificar oportunidades de melhoria em relação à alocação de órgãos.
| EP02 | US13 | Como um médico chefe do sistema, eu quero poder acessar a base de dados para visualizar informações estatísticas sobre os transplantes de rim realizados, para que eu possa avaliar a efetividade do sistema e identificar possíveis áreas de melhoria.

## Backlog do Incremento
| Épico | US | Descrição da User Story |
| --- | --- | --- |
| EP03 | US04 | Como um médico responsável por encontrar o receptor ideal para um transplante de órgãos, eu quero utilizar um aplicativo para comparar as informações de diferentes pacientes, usando algoritmos e fórmulas matemáticas, para determinar o receptor mais compatível e aumentar as chances de sucesso do transplante.
| EP03 | US22 | Como um médico, eu gostaria de poder filtrar os pacientes por diferentes critérios, como idade, tipo sanguíneo e histórico médico, para que eu possa identificar rapidamente os pacientes que são mais compatíveis com os rins doados.
| EP03 | US02 | Como um médico que precisa checar e dar um match em dois pacientes para transplante de órgãos entre eles, eu quero usar o aplicativo para checar os dados do paciente para garantir que eles são compatíveis e seguros para o transplante.
| EP02 | US20 | Como um médico, eu gostaria de poder buscar informações específicas de um paciente ou de um rim, para que eu possa encontrar rapidamente as informações necessárias para tomar uma decisão sobre o transplante.
| EP03 | US10 | Como um médico responsável por encontrar o receptor ideal para um transplante de rim, eu quero usar um software que gere automaticamente uma lista de possíveis receptores compatíveis com o rim doado. Isso me ajudará a identificar rapidamente os pacientes que têm maior probabilidade de sucesso no transplante e aumentar suas chances de recuperação.
| EP02 | US15 | Como um médico, eu quero poder editar as informações do paciente e do órgão doado caso haja uma mudança significativa em até 2 meses após a inserção dos dados, para manter as informações precisas e atualizadas, sem alterar o relatório final do ano.
| EP04 | US14 | Como um médico chefe do sistema, eu quero poder acessar os logs do sistema para monitorar as atividades dos usuários, para que eu possa garantir a segurança e a efetividade do sistema.
| EP01 | US19 | Como um médico chefe do sistema, eu gostaria de poder definir os campos que devem ser extraídos dos documentos em PDF, para que o sistema possa se adaptar a diferentes tipos de documentos e garantir a consistência dos dados.
| EP01 | US21 | Como um médico chefe do sistema, eu gostaria de poder treinar o sistema para reconhecer padrões específicos em documentos em PDF, para que o sistema possa se adaptar a novos tipos de documentos sem a necessidade de intervenção manual.

## Requisitos Não-Funcionais
| Nº | Classificação | Descrição |
| --- | --- | --- |
|  RNF01   | Requisito de Desempenho | A análise dos documentos deve ser feita em 1 minuto ou menos. |
|  RNF02   | Requisito de Confiabilidade | O sistema deve manter sigilo, privacidade e segurança dos dados contidos nele. |
|  RNF03   | Requisito de Confiabilidade | O sistema deve registrar as atividades dos usuários para manter a rastreabilidade das ações (log). |
|  RNF04   | Requisito de Usabilidade | O sistema deve estar disponível a qualquer momento e a qualquer dispositivo com acesso a internet e um navegador (site responsivo). |
|  RNF05   | Requisito de Confiabilidade | O acesso ao sistema deve ser restrito apenas à usuários cadastrados. |
| RNF06 | Requisito de Implementação | O site deve ser orientado a objetos |
| RNF07 | Requisito de Implementação | O backend deve ser desenvolvido em python, através do framework Django |
| RNF08 | Requisito de Implementação | O frontend deve ser desenvolvindo utilizando o ReactJS e JavaScript |
| RNF09 | Requisito de Implementação | O sistema de banco de dados deve ser modelado utilizando o MongoDB |



## Histórico de revisão
| Versão | Data | Descrição | Autor |
| --- | --- | --- | --- |
|  `1.0`   | 23/05/2023 | Criação inicial do documento. | [Bruno Martins](https://github.com/gitbmvb) |
|  `1.1`   | 23/05/2023 | Reorganização das tabelas dos MVPs 1, 2, e incremento. | [Bruno Martins](https://github.com/gitbmvb) |
|  `1.2`   | 24/05/2023 | Adicionando mais RNFs. | [Bruno Martins](https://github.com/gitbmvb) |