# map con inmutabilidad
teams = [
  {
    'team': 'liverpool',
    'money': 200,
  },
  {
    'team': 'city',
    'money': 500,
  },
  {
    'team': 'chelsea',
    'money': 400,
  }
]

def add_transfer(team):
  new_team = team.copy()
  new_team['transfer_expenses'] = new_team['money'] - .18
  return new_team

new_teams = list(map(add_transfer, teams))
print('New list')
print(new_teams)
print('Old list')
print(teams)