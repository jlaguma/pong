import click
import sys

from pong import pong, __version__
from .decorators import add_custom_help


@click.command()
@click.version_option(__version__, "-V", "--version", message="%(version)s")
@click.option(
    '--player1',
    '-p1',
    default='Player 1',
    help='Name of Player 1.',
)
@click.option(
    '--player2',
    '-p2',
    default='Player 2',
    help='Name of Player 2.',
)
@click.option(
    '--color1',
    '-c1',
    default='white',
    help='Color of player 1.',
)
@click.option(
    '--color2',
    '-c2',
    default='white',
    help='Color of player 2.',
)
@add_custom_help
def main(player1, player2, color1, color2):
    game = pong.Pong(player_1_name=player1,
                     player_1_color=color1,
                     player_2_name=player2,
                     player_2_color=color2)
    try:
        game.play()
    except:
        sys.exit()


if __name__ == '__main__':
    main()
