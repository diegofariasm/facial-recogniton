# Como utilizar o projeto:

## Ferramentas necessárias:

- Python
- Poetry ( Gerenciador de pacotes )

## Como instalar o python:

1. Visite o [site oficial](https://www.python.org/downloads/).
2. Baixe a versão do python 3.11
3. Comece a instalação.
4. ![Instalação](https://www.sqlshack.com/wp-content/uploads/2018/08/word-image-84.png "Como fazer a instalação")
5. Finalize a instalação.


## Como instalar o poetry:


1. Primeiramente, acesse o [site oficial](https://python-poetry.org/docs/#installation)
2. Encontre o script de instalação pra sua plataforma. Exemplo do windows: ```(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - ```
3. Execute o script
4. Adicione os scripts do python para a variavel $PATH. [Tutorial](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/#:~:text=Go%20ahead%20and%20click%20on%20the%20Environment%20Variables,you%20have%20to%20decide%20which%20one%20to%20edit.) (A localização é dada na execução do script)
5. Reinicie o computador,
6. Cheque se poetry está instalado com ```poetry --version```.

## Rodando o projeto:

1. Entre na pasta raiz ( facial-recognition )
2. Execeute ```poetry install```
3. Utilize o comando ```poetry shell``` para poder entrar no ambiente vitual ( Necessário para rodar o código )
4. Rode o arquivo main.py. ```python .\facial_recognition\main.py```
5. Entre na rota dita ao rodar o código. Exemplo: ```https:localhost:5000```

### Observações:

Sempre que for rodar o código, confira se está no ambiente virtual.
Estando em um ambiente virtual, o prompt de comando terá uma aparência diferente, como a seguir:
#### Antes de rodar ``` poetry shell ```:
``` PS C:\Users\fushi\Desktop\facial-recognition> ```

#### Depois de rodar ```` poetry shell ```:
``` (facial-recognition-py3.11) PS C:\Users\fushi\Desktop\facial-recognition> ```

Note a diferença do ambiente virtual. (facial-recognition-py-3.11)

## Estrutura do projeto:

Esse projeto é estruturado em MVC, como a seguir:

1. Pasta onde é localizada as páginas do websit:  ``` views```   
2. Pasta onde é localizado os controllers do websit:  ``` controllers```   
3. Pasta onde é localizado os modelos de objeto do websit:  ``` models```   
4. Pasta onde é localizado os scripts de interação com a databas:  ``` dao```   
5. Pasta onde é localizado componentes do website. Javascript, images, css e etc:  ``` static```   

### Observações:

As pasta __pycache__ e __instance__ podem ser ignoradas.

