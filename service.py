from models import AlcStatsModel

class AlcStatsService:
    def __init__(self):
        self.model = AlcStatsModel()

    def create(self, params):
        return self.model.create(params)

    def list(self):
        response = self.model.list_items()
        return response