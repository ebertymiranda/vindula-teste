# Controle de Filmes

Este é um projeto Django destinado a controlar os filmes que você já assistiu, os filmes que gostaria de assistir, e também permite a importação de filmes a partir de uma planilha Excel.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.x
- Virtualenv (recomendado)
- Redis (para o Celery)

### Configuração do Ambiente Virtual (opcional, mas recomendado)

```bash
# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows

# Instale as dependências
pip install -r requirements.txt
```

### Configuração do Banco de Dados
#### Aplique as migrações
```bash
python manage.py migrate
```
#### Em um terminal separado, inicie o Celery Worker
```bash
celery -A controle_filmes worker -l info
```
#### Inicie o servidor Django
```bash
python manage.py runserver
```
O aplicativo estará disponível em http://127.0.0.1:8000/

## Funcionalidades

### 1. Cadastro de Filmes

- Adicione filmes à sua lista, especificando o título e a data em que assistiu ou gostaria de assistir.
  
### 2. Importação de Filmes a partir de uma Planilha Excel

- Utilize a funcionalidade de importação para adicionar vários filmes de uma só vez, utilizando uma planilha Excel.

### 3. Relatórios

- Visualize os filmes que você já assistiu, os que ainda não assistiu e os que gostaria de assistir em gráficos usando Chart.js.

### 4. Autocomplete

- O frontend possui um recurso de autocomplete para facilitar o registro de visualizações.
