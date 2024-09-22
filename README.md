Documentação para Executar Projeto Python pelo Prompt de Comando:


Pré-requisitos:

1. Python: 
Certifique-se de que o Python está instalado. Você pode baixar a versão mais recente em python.org.

2. Pip: 
O gerenciador de pacotes pip deve estar instalado. Ele geralmente é incluído com a instalação do Python.



Passos para Executar o Projeto:

1. Abrir o Prompt de Comando:
Pressione Win + R, digite cmd e pressione Enter para abrir o Prompt de Comando.

2. Navegar até a Pasta do Projeto:
Use o comando cd para acessar o diretório onde seus arquivos de projeto estão localizados. 

3. Bash

4. Exemplo: para navegar deve ser da o  “CD em minusculo, seguido da localização do projeto”cd C:\Users\Roberta\Downloads\Python



 Criar um Ambiente Virtual (Opcional):
Para isolar as dependências do projeto, você pode criar um ambiente virtual. Execute:

1. bash

2. Copiar código

3. python -m venv env



Para ativar o ambiente virtual, digite:

1. bash

2. Copiar código

3..\env\Scripts\activate

4. Após ativar, você verá o nome do ambiente virtual no início da linha de comando.



 Instalar Dependências:
Examine o arquivo pyproject.toml para identificar as dependências necessárias. Instale-as usando o comando pip. Por exemplo, se você precisar de flask e requests, use:

1. bash

2. Copiar código

3. pip install flask requests

5. Rodar o Projeto



Identifique qual arquivo Python é o ponto de entrada do seu projeto (main.py). Para executar esse arquivo, use o seguinte comando:

1. bash

2. Copiar código

3. python nome_do_arquivo_principal.py

4. Substitua python main.py pelo nome real do seu arquivo.




Exemplo de como os comandos devem ser executados no Prompt de Comando:

1. bash

2. Copiar código

3. cd C:\Users\Roberta\Downloads\Python

4. python -m venv env

5..\env\Scripts\activate

6. pip install flask requests

7. python main.py 



Observações:
Sair do Ambiente Virtual: Para sair do ambiente virtual, você pode simplesmente digitar deactivate no Prompt de Comando.
Verificar Versões: Para verificar se o Python e o pip estão instalados corretamente, você pode executar:

1. bash

2. Copiar código

3. python --version

4. pip --version
