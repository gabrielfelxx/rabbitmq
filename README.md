# README - Exemplo de Consumo de Mensagens do RabbitMQ

Este repositório contém um pequeno exemplo de como consumir mensagens de uma fila RabbitMQ usando a biblioteca pika em Python.

## Pré-requisitos

- Python 3.x instalado em seu ambiente de desenvolvimento.
- Biblioteca pika instalada. Você pode instalá-la usando o pip:

```bash
pip install pika
```

- RabbitMQ instalado e em execução localmente. Você pode instalar o RabbitMQ seguindo as [instruções oficiais](https://www.rabbitmq.com/download.html).

## Como Usar

1. Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
```

2. Navegue até o diretório do repositório:

```bash
cd seu-repo
```

3. Abra o arquivo `consumer.py` em um editor de texto para revisar ou editar o código, se necessário. Certifique-se de que as informações de conexão ao RabbitMQ (host, porta, credenciais) estejam corretamente configuradas.

4. Execute o script Python:

```bash
python consumer.py
```

Isso iniciará o consumidor e ele estará pronto para receber mensagens da fila RabbitMQ definida no código.

## Observações

- Certifique-se de que o RabbitMQ esteja em execução e que a fila 'data_queue' exista.
- Este exemplo utiliza credenciais padrão ('guest'/'guest') para conexão ao RabbitMQ. Em um ambiente de produção, é altamente recomendável configurar credenciais mais seguras.
- Este é um exemplo simples e didático. Em uma aplicação real, você pode precisar lidar com erros, implementar lógica de processamento de mensagens mais complexa e configurar ações de recuperação em caso de falha.

## Autores

- Gabriel Felix

---

Você pode personalizar este README de acordo com as necessidades do seu projeto. Certifique-se de incluir informações importantes, como instruções de configuração, descrição da funcionalidade, contexto e quaisquer outros detalhes relevantes. Isso ajudará os colaboradores e outros desenvolvedores a entenderem e usarem seu código com facilidade.