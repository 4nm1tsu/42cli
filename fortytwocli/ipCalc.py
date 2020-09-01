import re
import ipaddress

import click

from rich import print
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel


def calc():
    console = Console()
    buf = ''
    click.secho("press 'q' to quit", bg='white', fg='black')
    while True:
        print(">>> ", end='')
        buf = input()
        if buf.strip() == '':
            continue
        if re.compile(buf, re.IGNORECASE).fullmatch('q'):
            break
        try:
            ip = ipaddress.ip_network(buf, False)
        except ValueError:
            click.secho('invalid format.', fg='red')
            continue
        if ip.version == 6:
            click.secho('IPv6 is not available.', fg='red')
            continue

        renderables = list()
        if (ip.num_addresses - 2) > 0:
            renderables.append('[cyan]Usable Host IP Range[/cyan]\n{}'.format(
                str(ip.network_address + 1) + ' ~ ' + str(ip.broadcast_address - 1)))
        else:
            renderables.append('[cyan]Usable Host IP Range[/cyan]\nNothing.')
        renderables.append(
            '[violet]Network Address[/violet]\n{}'.format(str(ip.network_address)))
        renderables.append(
            '[blue]Broadcast Address[/blue]\n{}'.format(str(ip.broadcast_address)))
        if (ip.num_addresses - 2) > 0:
            renderables.append(
                '[green]Number of Usable Hosts[/green]\n{}'.format(str(ip.num_addresses - 2)))
        else:
            renderables.append('[green]Number of Usable Hosts[/green]\nNothing.')
        renderables.append(
            '[magenta]Total Number of Hosts[/magenta]\n{}'.format(str(ip.num_addresses)))
        renderables.append(
            '[yellow]Subnet Mask[/yellow]\n{}'.format(str(ip.netmask)))
        panels = [Panel(renderable, expand=True) for renderable in renderables]
        console.print(Columns(panels))
