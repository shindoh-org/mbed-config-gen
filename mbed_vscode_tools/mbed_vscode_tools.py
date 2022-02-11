import click
import pathlib


@click.group()
def cmd():
    pass


@cmd.command()
@click.argument('toolchain', type=click.Choice(['GCC_ARM', 'ARM']))
@click.argument('mbed-target', type=str)
@click.option(
    '--profile',
    type=click.Choice(['debug', 'develop', 'release']),
    default='develop', show_default=True,
    help='Choose a build profile.')
@click.option(
    '--program-path',
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True,
        resolve_path=True, path_type=pathlib.Path),
    default=pathlib.Path().cwd(), show_default=True,
    help='Path to an mbed program directory. '
         'If not specified, it\'s set to your working directory.')
def configure(
        toolchain: str, mbed_target: str,
        profile: str, program_path: pathlib.Path) -> None:
    """Configure build settings.

    [TOOLCHAIN] The toolchain you are using to build your mbed application.
    Choose \'GCC_ARM\' or \'ARM\'.

    [MBED_TARGET] A build target for an mbed-enabled device (e.g. DISCO_L072CZ_LRWAN1).
    """
    click.echo(toolchain)
    click.echo(mbed_target)
    click.echo(profile)
    click.echo(type(program_path))


@cmd.command()
def update():
    click.echo('update')


def main():
    cmd()


if __name__ == '__main__':
    main()
