from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    HIGH_BUDGET_CAMPAIGN = 5000.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.HIGH_BUDGET_CAMPAIGN, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        return engagement_rate >= self.required_engagement * 1.2

