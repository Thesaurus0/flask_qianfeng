import click
import os

from App import create_app

envionment = os.environ.get("FLASK_ENV")
if envionment.find('dev') >= 0:
    env = 'dev'
elif envionment.find('uat') >= 0:
    env = 'uat'
elif envionment.find('prod') >= 0:
    env='prod'
else:
    raise 'the FLASK_ENV is incorrect: ' + envionment
print('env:' + env)

app = create_app(env)


@app.cli.command('dbinit', help='db creating')
def db_init():
    print('db init')


# @app.cli.command('runs')
@click.command('run-ser')
@click.option('--port', type=click.INT, help='port number', default=8080)
@click.option('--debug', type=click.BOOL, help='debug mode', default=True)
def run_server(port, debug):
    app.run(port=port, debug=debug)


if __name__ == '__main__':
    run_server()
    # from waitress import serve
    # serve(app, host='0.0.0.0', port=8080)
    # python app.py

    # Deploy to Production
    # https: // flask.palletsprojects.com / en / 1.1.x / tutorial / deploy /
