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
                opcao_bytes = conn.recv(1024)
                opcao = opcao_bytes.decode().strip()
                print("Opção recebida no servidor:", opcao)
                if not opcao:
                    break
                if opcao == '1':
                    conn.sendall("Digite o número para calcular o fatorial: ".encode())
                    num_bytes = conn.recv(1024)
                    num = int(num_bytes.decode().strip())
                    print("Número recebido no servidor para fatorial:", num)
                    resultado = calcular_fatorial(num)
                    conn.sendall(str(resultado).encode())
                elif opcao == '2':
                    conn.sendall("Digite o valor de n para calcular a combinação: ".encode())
                    n_bytes = conn.recv(1024)
                    n = int(n_bytes.decode().strip())
                    conn.sendall("Digite o valor de k para calcular a combinação: ".encode())
                    k_bytes = conn.recv(1024)
                    k = int(k_bytes.decode().strip())
                    print("Valores recebidos no servidor para combinação:", n, k)
                    resultado = calcular_combinacao(n, k)
                    conn.sendall(str(resultado).encode())
                elif opcao == '3':
                    conn.sendall("Digite o valor de n para calcular a permutação: ".encode())
                    n_bytes = conn.recv(1024)
                    n = int(n_bytes.decode().strip())
                    conn.sendall("Digite o valor de k para calcular a permutação: ".encode())
                    k_bytes = conn.recv(1024)
                    k = int(k_bytes.decode().strip())
                    print("Valores recebidos no servidor para permutação:", n, k)
                    resultado = calcular_permutacao(n, k)
                    conn.sendall(str(resultado).encode())
                elif opcao == '4':
                    conn.sendall("Digite o valor de n para calcular o arranjo: ".encode())
                    n_bytes = conn.recv(1024)
                    n = int(n_bytes.decode().strip())
                    conn.sendall("Digite o valor de k para calcular o arranjo: ".encode())
                    k_bytes = conn.recv(1024)
                    k = int(k_bytes.decode().strip())
                    print("Valores recebidos no servidor para arranjo:", n, k)
                    resultado = calcular_arranjo(n, k)
                    conn.sendall(str(resultado).encode())
                elif opcao == '5':
                    print('Conexão encerrada.')
                    break
                else:
                    conn.sendall("Opção inválida.".encode())

if __name__ == "__main__":
    main()
