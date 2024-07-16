from typing import Dict

from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    @property
    def team_data(self):
        expenses: int = 250_000
        sponsors: Dict[str, Dict[int, int]] = {
                                                "Oracle": {1: 1_500_000, 2: 800_000},
                                                "Honda": {8: 20_000, 10: 10_000}
                                                }
        return expenses, sponsors
