import typer, json
import requests

app = typer.Typer()

@app.command()
def github_activity(username: str):
    url = f'https://api.github.com/users/{username}/events'

    response = requests.get(url)
    print(f'Status: {response.status_code}')
    print(f'Response: {response.json()}')

    if response.status_code == 200:
        typer.echo(f'Githun activity error: {response.json()}')
        raise typer.Exit(code=1)
    
    if response.status_code == 404:
        typer.echo(f'User {username} not found')
        raise typer.Exit(code=1)
    
    events = response.json()

    if not events:
        typer.echo(f'No recent activity')
        return
    
    for event in events[:10]:
        event_type = event['type']
        repo = event['repo']['name']

        typer.echo(f'{event_type} at {repo}')

if __name__ == "__main__":
    app()