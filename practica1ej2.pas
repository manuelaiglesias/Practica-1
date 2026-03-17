{
  Escribe un programa que solicite al usuario una cantidad de segundos y muestre
cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
hora, 1 minuto y 1 segundo.   
}

segundos= int(input( "ingrese la cantidad de segundos a convertir..."))
hora= segundos//3600
minutos= (segundos%3600)//60
segundo_restantes= segundos%60
print(f" {segundos} segundos equibalen a {hora} horas {minutos} minutos y {segundo_restantes} segundos ")
