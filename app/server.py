import socket

def calcular_fatorial(n):
    if n == 0:
        return 1
    return n * calcular_fatorial(n - 1)


def main():
    HOST = '0.0.0.0'
    PORT = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print(f"{addr}")
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
                elif opcao == '5':
                    print('bye.')
                    break
                else:
                    conn.sendall("invel.".encode())

if __name__ == "__main__":
    main()


