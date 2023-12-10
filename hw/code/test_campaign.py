import pytest
from ui.pages.campaign_page import CampaignPage
from base import BaseCase


class TestCampaign(BaseCase):
    @pytest.mark.parametrize(
        'tab_name,tab_url',
        [
            pytest.param(CampaignPage.CAMPAIGN_TAB, 'https://ads.vk.com/hq/dashboard/ad_plans'),
            pytest.param(CampaignPage.GROUPS_TAB, 'https://ads.vk.com/hq/dashboard/ad_groups'),
            pytest.param(CampaignPage.ADS_TAB, 'https://ads.vk.com/hq/dashboard/ads'),
        ]
    )
    def test_tab_navigation(self, campaign_page, tab_name, tab_url):
        campaign_page.go_to_tab(tab_name)
        campaign_page.check_url(tab_url)

    def test_plan_creation_modal_open(self, campaign_page):
        campaign_page.click(campaign_page.locators.PLAN_CREATION_BTN)

