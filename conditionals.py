# if-else
edad = 20

if edad >= 18:
  print('Es mayor de edad')
else:
  print('Es menor de edad')

operacion = 1
if operacion == 1:
  print('Operación 1')
elif operacion == 2:
  print('Operación 2')
elif operacion == 3:
  print('Operación 3')
else:
  print('No existe esta operación')

HTTP_STATUS_CODE = 200

match HTTP_STATUS_CODE:
  case 200:
    print('OK')
    # return
  case 400:
    print('Bad request')
    # return
  case 401:
    print('Unauthorized')
    # return
  case 404:
    print('Not Found')
    # return


def getStatusMessage(status):
  match status:
    case 200:
      print('OK')
      return
    case 400:
      print('Bad request')
      return
    case 401:
      print('Unauthorized')
      return
    case 404:
      print('Not Found')
      return
