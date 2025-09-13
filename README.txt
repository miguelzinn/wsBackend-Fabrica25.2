Projeto Django - Lyrics Finder 🎶

Descrição:
Este projeto é uma aplicação web desenvolvida com Django que permite o cadastro de artistas e músicas, com busca automática de letras utilizando a API pública lyrics.ovh.

Funcionalidades:
- CRUD completo para Artistas (nome, nacionalidade)
- CRUD completo para Músicas (título, artista, letra)
- Integração com a API lyrics.ovh para buscar letras de músicas
- Interface web simples e funcional

Requisitos:
- asgiref==3.9.1
- certifi==2025.8.3
- charset-normalizer==3.4.3
- Django==5.2.6
- idna==3.10
- requests==2.32.5
- sqlparse==0.5.3
- tzdata==2025.2
- urllib3==2.5.0


Instalação:
1. Clone o repositório
2. Crie um ambiente virtual
3. Instale as dependências com "pip install -r requirements.txt"
4. Execute as migrações com "python manage.py migrate"
5. Inicie o servidor com "python manage.py runserver"

Arquivos importantes:
- .gitignore → ignora arquivos desnecessários
- requirements.txt → lista de dependências do projeto
- README.txt → este documento

Observações:
- Não é permitido utilizar APIs que foram usadas em sala, como BuscaCEP.
- A letra da música é buscada automaticamente ao cadastrar ou editar uma música.
- Em caso de falha na API, uma mensagem de erro será exibida no campo de letra.

Autor:
Miguel Giovanno Porto Vieira — Desafio Backend Fábrica 25.2

