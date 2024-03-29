import socket

def calcular_fatorial(n):
    if n == 0:
        return 1
    return n * calcular_fatorial(n - 1)

def calcular_combinacao(n, k):
    return calcular_fatorial(n) // (calcular_fatorial(k) * calcular_fatorial(n - k))

def calcular_permutacao(n, k):
    return calcular_fatorial(n) // calcular_fatorial(n - k)

def calcular_arranjo(n, k):
    return calcular_permutacao(n, k)

def main():
    HOST = '0.0.0.0'
    PORT = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(10)
        print(f"Servidor funcionando em {HOST}:{PORT}")

        conn, addr = s.accept()
        with conn:
            print(f"Conexão estabelecida por {addr}")
            while True:
                data = conn.recv(1024)
                #print("data no servidor", data)
                opcao = data.decode().strip()
                #print("Opção recebida:", opcao)
                
                if opcao == '1':
                    #print("Opção 1 selecionada.")
                    num = int(conn.recv(1024).decode())
                    print("Número recebido no servidor para fatorial:", num)
                    resultado = calcular_fatorial(num)
                    conn.sendall(str(resultado).encode())
                    #print("Resultado enviado:", resultado)
                    #print("Fatorial calculado.")
                elif opcao == '2':
                    #print("Opcao 2 selecionada.")
                    n = int(conn.recv(1024).decode())
                    k = int(conn.recv(1024).decode())
                    print("Valores recebidos no servidor para combinação:", n, k)
                    resultado = calcular_combinacao(n, k)
                    conn.sendall(str(resultado).encode())
                    #print("Resultado enviado:", resultado)
                    #print("comb calculada")
                elif opcao == '3':
                    #print("Opcao 3 selecionada.")
                    n = int(conn.recv(1024).decode())
                    k = int(conn.recv(1024).decode())
                    print("Valores recebidos no servidor para permutação:", n, k)
                    resultado = calcular_permutacao(n, k)
                    conn.sendall(str(resultado).encode())
                    #print("Resultado enviado:", resultado)
                    #print("permutação calculada")
                elif opcao == '4':
                    #print("Opcao 4 selecionada.")
                    n = int(conn.recv(1024).decode())
                    k = int(conn.recv(1024).decode())
                    print("Valores recebidos no servidor para arranjo:", n, k)
                    resultado = calcular_arranjo(n, k)
                    conn.sendall(str(resultado).encode())
                    #print("Resultado enviado:", resultado)
                    #print("arranjo calculado")
                elif opcao == '5':
                    print('Conexão encerrada.')
                    break
                else:
                    conn.sendall("Opção inválida.".encode())
                    #print("Opção inválida:", opcao)

if __name__ == "__main__":
    main()
