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
        conn, addr = s.accept()
        with conn:
            print(f"Conexão estabelecida por {addr}")
            while True:
                opcao_bytes = conn.recv(1024)
                opcao = opcao_bytes.decode().strip()
                if not opcao:
                    break
                if opcao == '1':
                    num_bytes = conn.recv(1024)
                    num = int(num_bytes.decode())
                    resultado = calcular_fatorial(num)
                    conn.sendall(str(resultado).encode())
                elif opcao in ['2', '3', '4']:
                    valores = conn.recv(1024).decode().split(',')
                    n = int(valores[0])
                    k = int(valores[1])
                    if opcao == '2':
                        resultado = calcular_combinacao(n, k)
                    elif opcao == '3':
                        resultado = calcular_permutacao(n, k)
                    elif opcao == '4':
                        resultado = calcular_arranjo(n, k)
                    conn.sendall(str(resultado).encode())
                elif opcao == '5':
                    print('Conexão encerrada.')
                    break
                else:
                    conn.sendall("Opção inválida.".encode())

if __name__ == "__main__":
    main()
