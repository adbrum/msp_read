# msp_read
## Código para leitura de dados do microcontrolador MSP430

## Crontab - Executar o script ao iniciar a máquina.


PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
@reboot python /home/pi/lisimetro/broker_lisimetro.py >>/home/pi/error_start_lisimetro.log 2>&1  
@reboot sleep 5 && python /home/pi/lisimetro/broker_lisimetro.py &  


