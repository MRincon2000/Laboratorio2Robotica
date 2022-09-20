rosinit;

%% SUSCRIBIRSE AL TOPICO turtle1 PARA VER LA POSICION Y ORIENTACION ACTUAL

SUBS= suscriptor() %Llama a la funcion suscriptor()
SUBS.LatestMessage %Obtiene el ultimo mensaje del topico y lo muestra.

%% ENVIAR POSICION ABSOLUTA PARA QUE LA TORTUGA SE MUEVA ALLI

traslacion() %Llama a la funcion traslacion()



%% FUNCIONES
function SUBS =suscriptor()
    SUBS=rossubscriber('/turtle1/pose'); %Crea un suscriptor al topico pose.
end

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
