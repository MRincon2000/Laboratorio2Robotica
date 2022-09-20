 <h1 align="center"> Programas para comunicarse con ROS y simulador Turtlesim</h1>
 
![Turtlesim](https://user-images.githubusercontent.com/49238418/191165513-74691628-c0f9-4c1e-bc53-c5555d371238.png)

Programas escritos en MATLAB y Python para comunicarse con el simulador Turtlesim y entrenarse en el uso de ROS.

## Inicializacion del core de ROS

Para inicializar un nuevo core de ROS se abre una nueva terminal mediante la combinacion de las teclas Ctrl+Alt+T. A continuación escribir el siguiente comando:

  ```
		roscore
  ```

![roscore](https://user-images.githubusercontent.com/49238418/191166831-d5a61b57-3dd5-4c72-85b9-1443ece8c0c3.png)

## Inicializacion del simulador Turtlesim

Para inicializar el simulador de Turtlesim abrir una nueva terminal aparte de la anterior y esvribir el comando:
 ```
		rosrun turtlesim turtlesim_node
  ```
![rosrun](https://user-images.githubusercontent.com/49238418/191167163-2552f06d-1139-435b-9d46-ef6eb7937655.png)

Y se abrirá una nueva instancia del simulador con un ícono aleatorio de la tortuga
![turlesim2](https://user-images.githubusercontent.com/49238418/191167299-0517516a-a95e-433a-a8db-1e16c8b5e972.png)

Y ya está todo listo para comenzar a usar el simulador.

## :hammer:Matlab
Suscriptor para obtener posición de la tortuga y servicio para moverla a coordenadas deseadas.

Abrir MATLAB desde su carpeta raiz con el comando:


  ```
		./matlab
  ```
![matlab](https://user-images.githubusercontent.com/49238418/191167846-b818b28f-6454-4ece-97e6-35ccc2d79bdc.png)

A continuacion abrir el script ROS_Matlab.m incluido en el repositorio

![CodigoMAT](https://user-images.githubusercontent.com/49238418/191168132-649e3fd0-5ab8-4f27-83fe-1730846ee0f9.png)

Este script se encuentra dividido en 4 secciones. La primera se encarga de realizar la cominicacion entre el nodo maestro de ROS y MATLAB:


  ```matlab
		rosinit;
  ```
Esta sección del script siempre debe ejecutarse al principio.

La segunda sección permite realizar el llamado a la función suscriptor() la cual permitirá obtener la información de la posición actual de la tortuga.

```matlab
%% SUSCRIBIRSE AL TOPICO turtle1 PARA VER LA POSICION Y ORIENTACION ACTUAL

SUBS=suscriptor() %Llama a la funcion suscriptor()
SUBS.LatestMessage %Obtiene el ultimo mensaje del topico y lo muestra.

  ```
La tercera sección permite realizar el llamado a la función traslación, la cual permite al usuario ingresar datos de posicion deseados para que la tortuga se mueva.

```matlab
%% ENVIAR POSICION ABSOLUTA PARA QUE LA TORTUGA SE MUEVA ALLI

traslacion() %Llama a la funcion traslacion()

  ```
Dependiendo de lo que el usuario desea hacer, puede ejecutar cualquiera de estas secciones.
  
Y la cuarta sección contiene las funciones que realizan tales tareas. Comenzando por la funcion Suscriptor se tiene:
  
  ```matlab
function SUBS=suscriptor()
    SUBS=rossubscriber('/turle1/pose'); %Crea un suscriptor al topico pose.
end
  ```
Esta funcion crea una variable SUBS de tipo rossusbscriber, la cual es una variable que se conecta al tópico público de ROS '/turle1/pose' que permite obtener los datos de posicion de la tortuga
A continuación se utiliza el atributo LatestMessage de dicha variable creada, lo cual permite obtener el último dato de posicion de la tortuga.

La salida obtenida es la siguiente:

![subs](https://user-images.githubusercontent.com/49238418/191170726-6b1ad094-80be-460b-a315-6028fc57a14b.png)

Y la funcion traslacion pide los datos de posicion deseados y los envia a la tortuga.
```matlab
function traslacion()
    x=input('Ingrese la coordenada X: ') %Solicita la coordenada x deseada.
    y=input('Ingrese la coordenada Y: ') %Solicita la coordenada y deseada.
    theta=input('Ingrese la orientacion Theta: ') % Solicita la orientacion.
    [client, request]= rossvcclient('/turtle1/teleport_absolute')
    %Crea un cliente al servicio teleport_absolulte y una variable request.
    %que contiene el tipo de mensaje que se puede enviar a dicho servicio.
    request.X=x %Modifica la coordenada x que se va a enviar.
    request.Y=y %Modifica la coordenada y que se va a enviar.
    request.Theta=theta % Modifica la orientación que se va a enviar.
    call(client,request) % Se envía el mensaje modificado al servicio.
end
  ```
