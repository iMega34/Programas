
from funcion import Funcion
from metodos import Metodos

from colorama import Fore, Style
from os import system

def main():
    while True:
        system("cls")
        print(Fore.CYAN + Style.BRIGHT + f"+{14 * '-'} SUMAS DE RIEMANN {14 * '-'}+")
        print(Fore.LIGHTYELLOW_EX + "\n    <<< Métodos >>>")
        print("\n1)\tPunto izquierdo\n2)\tPunto derecho\n3)\tPunto medio\n4)\tTrapecio\n" + Fore.LIGHTRED_EX + "5)\tSalir del programa")
        metodo = int(input(Fore.LIGHTYELLOW_EX + "\nSelecciona una opción para continuar\n>>> "))

        while metodo not in [1, 2, 3, 4, 5]:
            metodo = input(Fore.LIGHTYELLOW_EX + "Selecciona una opción válida para continuar\n>>> ")

        if metodo in [1, 2, 3, 4]:
            funcion: Funcion = Funcion()
            funcion.set_funcion = input(Fore.LIGHTGREEN_EX + Style.NORMAL + "\nIndica la función a evaluar: ")

            while True:
                try:
                    lim_inf = float(input(Fore.LIGHTGREEN_EX + "Indica el límite inferior de la función: "))
                    break
                except:
                    print(Fore.LIGHTRED_EX + "\nNo puedes ingresar letras o caracteres especiales\nVuelve a intentarlo\n")

            while True:
                try:
                    lim_sup = float(input(Fore.LIGHTGREEN_EX + "Indica el límite superior de la función: "))
                    break
                except:
                    print(Fore.LIGHTRED_EX + "\nNo puedes ingresar letras o caracteres especiales\nVuelve a intentarlo\n")

            while True:
                try:
                    particiones = int(input(Fore.LIGHTGREEN_EX + "Indica el número de particiones que deseas realizar: "))
                    break
                except:
                    print(Fore.LIGHTRED_EX + "\nNo puedes ingresar letras o caracteres especiales\nVuelve a intentarlo\n")

            grafica = input("¿Quieres graficar la suma de Riemann?" + Fore.YELLOW + " s/n: ")
            grafica = True if grafica == 's'else False

            try:
                if metodo == 1:
                    area = Metodos.punto_izquierdo(funcion, lim_inf, lim_sup, particiones, grafica)
                elif metodo == 2:
                    area = Metodos.punto_derecho(funcion, lim_inf, lim_sup, particiones, grafica)
                elif metodo == 3:
                    area = Metodos.punto_medio(funcion, lim_inf, lim_sup, particiones, grafica)
                else:
                    area = Metodos.trapecio(funcion, lim_inf, lim_sup, particiones, grafica)

                print(Fore.LIGHTMAGENTA_EX + f"\nEl área bajo la curva de f(x) = {funcion.get_funcion} es de {area:6f} ua")

            except TypeError:
                print(Fore.LIGHTRED_EX + "\nError con la función introducida\nVuelve a intentarlo")
            
            input(Fore.LIGHTYELLOW_EX + "\nPresiona ENTER para continuar...")

        else:
            print(Fore.MAGENTA + Style.BRIGHT + "\nGracias por usar Sumas de Riemman")
            print("\nDesarrolado por: Erick Daniel Ortiz Cervantes")
            print("\nPara más programas como este visita nuestro repositorio de GitHub")
            print("\nLink:" + Fore.BLUE + " https://github.com/iMega34/Programas")
            input()
            break


main()