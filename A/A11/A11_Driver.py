from War import War


def main():
    game = War()
    game.add_dealingPile()
    game.deal()
    while game.currentState:        # The program will run until one player runs out of cards
        game.make_move()
        print()

if __name__ == "__main__":
    main()
