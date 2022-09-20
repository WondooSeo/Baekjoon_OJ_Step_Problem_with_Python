import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().rstrip().split())
    pokemon_dict = dict()

    for i in range(N):
        now_pokemon = sys.stdin.readline().rstrip()
        pokemon_dict[str(i+1)] = now_pokemon
        pokemon_dict[now_pokemon] = str(i+1)

    for _ in range(M):
        print(pokemon_dict[sys.stdin.readline().rstrip()])
