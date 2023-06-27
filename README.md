# FastTransplant

## 1. Introdução
FastTransplant é um projeto desenvolvido durante o semestre 2023.1 da Universidade de Brasília/Faculdade do Gama (UnB/FGA) por alunos de Requisitos de Software do prof. Dr. George Marsicano. 

O objetivo geral é aplicar os conceitos, técnicas, ferramentas e metodologias aprendidas em sala - principalmente aqueles concernentes à Engenharia de Requisitos - através da criação de um website que pudesse auxiliar profissionais do Hospital Universitário de Brasília (HUB) durante todo o processo de transplantes de rim (Saiba mais [aqui](https://mdsreq-fga-unb.github.io/2023.1-FastTransplant/)).

Algumas funcionalidades:
- Em 3 cliques você consegue adicionar doadores ou receptores de forma automática a partir de um documento PDF!
- É possível realizar milhares de testes de compatibilidade receptor-doador em segundos!
- O sistema mantém a segurança através de um sistema de login simples e funcional.
- Você pode cadastrar diversos médicos e monitorar as atividades deles na plataforma.

## 2. Integrantes
| Foto | Nome | Conta Github |
| :---: | :---: | :----: |
| <img src="https://github.com/AnaBeatrizMassuh.png" alt="Ana Beatriz(Membro Time)" style="width: 10vw"> | Ana Beatriz Massuh | [AnaBeatrizMassuh](https://github.com/AnaBeatrizMassuh) |
| <img src="https://github.com/gitbmvb.png" alt="Bruno(Membro Time)" style="width: 10vw"> | Bruno Martins | [gitbmvb](https://github.com/gitbmvb) |
| <img src="https://github.com/uMorbeck.png" alt="João(Membro Time)" style="width: 10vw"> | João Pedro Morbeck | [uMorbeck](https://github.com/uMorbeck) |

## 3. Como utilizar
### 3.1. Pré-requisitos
Antes de iniciar, certifique-se que você cumpre com os seguintes requisitos:
- Você possui instalada a versão mais recente do **python** (>=3.10.6)
- Você possui instalada a versão mais recente do **pip** (>=22.0.2)

### 3.2. Instalação
Primeiramente, baixe os arquivos do projeto através do comando:
```
git clone https://github.com/mdsreq-fga-unb/2023.1-FastTransplant.git
```
Na sequência, navegue até a pasta raiz do projeto e instale as dependências com os seguintes comandos:
```
cd 2023-3.1-FastTransplant
pip install -r requirements.txt
```
Por fim, inicie o servidor com o comando:
```
python3 manage.py runserver
```

### 3.3. Contribuições
1. Leia o [Manual de Contribuição]().
2. Faça um *fork* deste repositório na sua conta github.
3. Crie uma *branch* na sua máquina local : `git checkout -b <nome_da_branch>`.
4. Realize as mudanças necessárias, e em seguida faça um *commit* através do comando `git commit -m "mensagem do commit"`
5. Envie as mudanças para o repositório remoto: `git push origin <nome_da_branch>`
6. Solicite um *pull request* através da sua conta Github.

## 4. Backlog
Você pode acessar a nosso backlog [aqui](https://docs.google.com/spreadsheets/d/1ZKEHNyYo_hBxK9R2Sjs1BWzV-quIr_ydlqZIk3Ac8Ew/edit?usp=sharing). Para informações mais detalhadas, como a Visão de Produto, Visão de Projeto, Processo de Desenvolvimento, etc., acesse a nossa [gitpages](https://mdsreq-fga-unb.github.io/2023.1-FastTransplant/).

## 5. Deploy
Você pode acessar a API agora mesmo por meio da URL [fast-transplant.com](fast-transplant.com).