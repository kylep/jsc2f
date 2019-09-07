"""jstf cli driven by click"""
import click

import jsc2f.lib as jsc2f


@click.option('--upload/--download', required=True, help='Upload or download')
@click.option('--filename', required=True)
@click.option('--db-ip', required=True)
@click.option('--db-port', required=False, default=3306)
@click.option('--db-user', required=True)
@click.option('--db-password', required=True)
@click.option('--db-name', required=True)
@click.option('--column', required=True)
@click.option('--table', required=True)
@click.option('--where', required=False, default='')
@click.command()
def cli(upload, filename, db_ip, db_port, db_user, db_password, db_name,
        column, table, where):
    """Upload/Download JSON SQL Cell from/to a local file"""
    if upload:
        jsc2f.update_from_file(filename=filename, host=db_ip, user=db_user,
                               password=db_password, database=db_name,
                               column=column, table=table, where=where,
                               port=db_port)
        click.echo('Uploaded JSON data to {}.{}'.format(db_name, table))
    else:
        jsc2f.save_to_file(filename=filename, host=db_ip, user=db_user,
                           password=db_password, database=db_name,
                           column=column, table=table, where=where,
                           port=db_port)
        click.echo('Saved JSON data to {}'.format(filename))
