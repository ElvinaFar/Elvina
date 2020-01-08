import click
import pika 



def callback(ch, method, properties, body): # функция которая вызывается при получении сообщения
    print(body.decode('utf-8'))

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='chat')

def add_to_queue(message, name):
    channel.basic_publish(exchange='',
                        routing_key='chat',
                        body=f'{name} said: {message}')
    connection.close()
    print(f'{name} said: {message}')

def get_messages():
    channel.basic_consume(queue='chat', on_message_callback=callback, auto_ack=True)   
    channel.start_consuming()

@click.group() # создание группы команд
def cli():
    pass

@click.command(help='send message') # команда отправки сообщения
@click.option('--name', default='Anonymous', prompt='Your username', help='Username')
@click.option('--message', default='Test', prompt='Your message', help='Message to send')
def send(message,name):
    add_to_queue(message, name)
    
@click.command(help='get messages') # команда для получения сообщений (слушает очередь rabbitmq)
def get(): 
    get_messages()

cli.add_command(send)
cli.add_command(get)

if __name__ == '__main__':
    cli()
