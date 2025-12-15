import colorama
import os

colorama.init(autoreset=True)

class C :
    R = colorama.Fore.RED
    G = colorama.Fore.GREEN
    B = colorama.Fore.BLUE
    Y = colorama.Fore.YELLOW
    X = colorama.Style.RESET_ALL


def clear():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_tabu(tabu: list):
    print(f"""
     {C.Y}{tabu[0]}{C.X} | {C.Y}{tabu[1]}{C.X} | {C.Y}{tabu[2]}{C.X}
    ——— ——— ———
     {C.Y}{tabu[3]}{C.X} | {C.Y}{tabu[4]}{C.X} | {C.Y}{tabu[5]}{C.X}
    ——— ——— ———
     {C.Y}{tabu[6]}{C.X} | {C.Y}{tabu[7]}{C.X} | {C.Y}{tabu[8]}{C.X}
    """)


def ver_win(tabu, simbolo) -> bool:
    combinacoes = [
        (0,1,2), (3,4,5), (6,7,8),  # linhas
        (0,3,6), (1,4,7), (2,5,8),  # colunas
        (0,4,8), (2,4,6)            # diagonais
    ]
    return any(tabu[a] == tabu[b] == tabu[c] == simbolo for a, b, c in combinacoes)


def minimax(board, occupied, is_ia_turn, player_sym, ia_sym):
    # Checa terminal
    if ver_win(board, ia_sym):
        return 1
    if ver_win(board, player_sym):
        return -1
    if all(occupied):
        return 0

    # IA maximiza, jogador minimiza
    if is_ia_turn:
        best = -2
        for i in range(9):
            if not occupied[i]:
                occupied[i] = True
                board[i] = ia_sym
                score = minimax(board, occupied, False, player_sym, ia_sym)
                occupied[i] = False
                board[i] = str(i+1)
                if score > best:
                    best = score
        return best
    else:
        best = 2
        for i in range(9):
            if not occupied[i]:
                occupied[i] = True
                board[i] = player_sym
                score = minimax(board, occupied, True, player_sym, ia_sym)
                occupied[i] = False
                board[i] = str(i+1)
                if score < best:
                    best = score
        return best


def get_move(occupied: list) -> int:
    while True:
        try:
            pos = int(input('Escolha onde quer jogar [1-9]: ').strip())
            if 1 <= pos <= 9 and not occupied[pos - 1]:
                return pos - 1
        except ValueError:
            pass
        print(f"    {C.R}[ ! ] Opção inválida{C.X}")


def play(single_player: bool = False) -> None:
    clear()
    simbolos = [f'{C.B}O{C.X}', f'{C.R}X{C.X}']
    print('Escolha seu símbolo:')
    print(f" [0] {simbolos[0]}  [1] {simbolos[1]}")

    while True:
        try:
            player_idx = int(input('>>> ').strip())
            if player_idx in (0, 1):
                break
        except ValueError:
            pass
        print(f"    {C.R}[ ! ] Opção inválida{C.X}")

    board = [str(i) for i in range(1, 10)]
    occupied = [False] * 9
    current_idx = player_idx
    ia_sym = simbolos[1 - player_idx]
    player_sym = simbolos[player_idx]

    while True:
        show_tabu(board)

        # Jogada do jogador / você 🫵
        idx = get_move(occupied)
        board[idx] = player_sym
        occupied[idx] = True

        if ver_win(board, player_sym):
            show_tabu(board)
            print(f"{C.G}Jogador venceu!{C.X}")
            return

        if all(occupied):
            show_tabu(board)
            print(f"{C.Y}Empate!{C.X}")
            return

        # Jogada da IA ou alternância dos jogadores
        if single_player :
            # Minimax para escolher melhor jogada
            best_score = -2
            best_move = None
            for i in range(9):
                if not occupied[i]:
                    occupied[i] = True
                    board[i] = ia_sym
                    score = minimax(board, occupied, False, player_sym, ia_sym)
                    occupied[i] = False
                    board[i] = str(i+1)
                    if score > best_score:
                        best_score = score
                        best_move = i

            idx = best_move
            board[idx] = ia_sym
            occupied[idx] = True

            if ver_win(board, ia_sym):
                show_tabu(board)
                print(f"{C.R}IA venceu!{C.X}")
                return

            if all(occupied):
                show_tabu(board)
                print(f"{C.Y}Empate!{C.X}")
                return
    else:
        # Dois jogadores alternam símbolos
        print('opa')
        current_idx = 1 - current_idx


def main():
    while True:
        clear()
        print('''Escolha uma opção:
 [0] Sair
 [1] Dois jogadores
 [2] Um jogador\n''')
        op = input('>>> ').strip()

        if op == '0':
            clear()
            print(f"{C.Y}PROGRAMA ENCERRADO{C.X}")
            break
        elif op == '1':
            play()
            input('Pressione Enter para voltar ao menu...')
        elif op == '2':
            play(single_player=True)
            input('Pressione Enter para voltar ao menu...')
        else:
            print(f"    {C.R}[ ! ] Opção inválida{C.X}")
            input('Pressione Enter para continuar...')

if _name_ == '_main_':
    main() # a main( ) 🙌