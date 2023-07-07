import subprocess

def check_centos_updates():
    command = 'dnf check-update -q'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode().strip()

def install_updates():
    command = 'dnf upgrade -y'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    return process.returncode

#Verificar actualizaciones disponibles
updates_output = check_centos_updates()

if updates_output:
    print("Actualizaciones disponibles:")
    print(updates_output)
    response = input("¿Desea instalar las actualizaciones? (s/n): ")
    if response.lower() == 's':
        return_code = install_updates()
        if return_code == 0:
            print("Las actualizaciones se instalaron correctamente.")
        else:
            print("Error al instalar las actualizaciones.")
    else:
        print("No se instalarán las actualizaciones.")
else:
    print("No hay actualizaciones disponibles.")

exit()  # Finalizar la ejecución del programa después de mostrar los resultados