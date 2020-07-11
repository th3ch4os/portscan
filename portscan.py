import  socket , sys , os
#===============================================
# PortScan - Simples feito em Python3 by TH3 CH4OS
#===============================================

#-----------------Rascunho ---------------------
"""
portscan ip porta --opcoes [ 0,1,2,3]

"""
#---------------- Sintaxe ---------------------
"""

python portscan.py ip porta [--opcoes]

ip    - endereço de pesquisa
porta - que irá ser verificada
--opções podem ser : 
--completo - Scan de portas num range maior
--básico   - Scan de portas definidas
""         - Scan


"""

#-------------- ToDo List -----------------------
"""

*Todo List
[ X ] Implementar uma função para verificar se um value existe na lista
[ X ] Melhorar lógica de interação com o Script
[   ] Deixar o códigos mais simples
[   ] Melhorar as funções 
[ X ] Implementar um dicionario de portas personalizadas e utilzar em uma função 

"""
#----------- Verificador de Sintaxe ---------------

def list_check_value(value,lista):
  """[Verifica se um Value na List existe ou não]

  Args:
      value ([int]): [Index da lista]
      lista ([list]): [Lista Desejada]

  Returns:
      [bool]: [True ou False]
  """
  try:
    if (lista[int(value)] in lista):
      return True
  except IndexError:
    return False

#- Verifica se os parametros estão vazio , se tiver resolve



if ( list_check_value(2,sys.argv) == False):
  sys.argv.insert(2,"80")

if ( list_check_value(3,sys.argv) == False):
  sys.argv.insert(3,"")

print(sys.argv)

if ( sys.argv[2]== "--completo") and ( sys.argv[3]==""):
  sys.argv.remove("")
  sys.argv.remove("--completo")
  sys.argv.insert(2,"")
  sys.argv.insert(3,"--completo")


#---------- Parâmetros do Script ------------------ 

p_ip     = sys.argv[1]  #ip do usuário 
p_porta  = sys.argv[2]  #porta
p_opcoes = sys.argv[3]  #opcoes
 
#--------   Problemas   -----------------------------

""" 
Problemas : 

[X] portscan 192.168.0.1 porta
[X] portscan 192.168.0.1 
    - Rodar scan completo


"""



print(sys.argv)

#------------  Funções  ----------------------------------------

def header():
  os.system("cls")
  print("# PortScaner by TH3 CH4OS")



def scanner(port):
  try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if ( s.connect_ex((p_ip, port)) ) == 0: 
      return True
    else:
      return False
  except Exception:
    pass


def scan_completo():
  os.system("cls")
  print("#PortScanner ")
  print("IP: {0}".format(str(p_ip)))
  print("Modo : Completo , Portas de 1-99999")
  for portNumber in range(1,99999):   
    if ( scanner(portNumber) == True ) :
      print("[+] Porta {0} | ABERTA".format(str(portNumber)))
    else:
      print("[-] Porta {0} | FECHADA".format(str(portNumber)))

def scan_basico(): # Scan utilizando uma lista de portas pre-definida
  header();print()
  portas = {

  "FTP":21,"SSH":22,"TELNET":23,"SMTP":25,'Http':80,"IRC":194,
  "HTTPS":443  

  }
  for service , portNumber in portas.items():   
    if ( scanner(portNumber) == True ) :
      print("[+] Porta {1} {0} ".format(str(portNumber),str(service)))
    else:
      print("[-] Porta {1} {0} ".format(str(portNumber),str(service)))
      
def scan(): # Scanei apenas uma porta
  for portNumber in range(int(p_porta),int(p_porta)+1):   
    if ( scanner(portNumber) == True ) :
      print("[+] Porta {0} | ABERTA".format(str(portNumber)))
    else:
      print("[-] Porta {0} | FECHADA".format(str(portNumber)))

#--------      Opções    -------------------------------------

if (  p_opcoes == "--completo"):
  scan_completo()
if (  p_opcoes == "--basico") or ( p_opcoes == ""):
  scan_basico()




# Verifica portas abertas netstat -an |find /i "listening"
        



