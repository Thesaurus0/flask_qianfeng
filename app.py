import click

from App import create_app

app = create_app()


@click.command('run-ser')
@click.option('--port', type=click.INT, help='port number', default=8080, prompt='please provide port number:')
@click.option('--debug', type=click.BOOL, help='debug mode', default=True, prompt='debug or not:')
def run_server(port, debug):
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    run_server()
