Installed `RabbitMQ`

`rabbitmqadmin --host=94.237.62.149 --port=37892 list queues`

Explored the queues until I found the flag in the following:

`rabbitmqadmin --host=94.237.62.149 --port=37892 get queue=factory_idle count=6`

`HTB{th3_hunt3d_b3c0m3s_th3_hunt3r}`
