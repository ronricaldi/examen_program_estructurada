

vehiculo = (input("Ingrese tipo de vehiculo: "))
match vehiculo :
    case "moto":
        tarifa=5
    case "auto":
        tarifa=10
    case "camion":
        tarifa=20

    
horario = int(input("Ingrese horario: 1/24 hrs. "))

if (horario>4 and horario <=8) or (horario >16 and horario <= 20):
    tarifa_total = tarifa * 1.15
    print ("tarifa a pagar: ", tarifa_total)
    
    
