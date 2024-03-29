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
                if not data:
                    break
                opcao, *valores = data.decode().strip().split(',')
                if opcao == '1':
                    num = int(valores[0])
                    print("Número recebido no servidor para fatorial:", num)
                    resultado = calcular_fatorial(num)
                    conn.sendall(str(resultado).encode())
                elif opcao == '2':
                    n, k = map(int, valores)
                    print("Valores recebidos no servidor para combinação:", n, k)
                    resultado = calcular_combinacao(n, k)
                    conn.sendall(str(resultado).encode())
                elif opcao == '3':
                    n, k = map(int, valores)
                    print("Valores recebidos no servidor para permutação:", n, k)
                    resultado = calcular_permutacao(n, k)
                    conn.sendall(str(resultado).encode())
                elif opcao == '4':
                    n, k = map(int, valores)
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
