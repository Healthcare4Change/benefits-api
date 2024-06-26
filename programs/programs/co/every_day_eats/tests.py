from django.test import TestCase
from programs.programs.every_day_eats.calculator import EveryDayEats
from screener.models import Screen, HouseholdMember, IncomeStream


class TestEveryDayEatsPension(TestCase):
    def setUp(self):
        self.screen1 = Screen.objects.create(
            agree_to_tos=True,
            zipcode="80205",
            county="Denver County",
            household_size=1,
            household_assets=0,
        )
        self.person1 = HouseholdMember.objects.create(
            screen=self.screen1,
            relationship="headOfHousehold",
            age=60,
            student=False,
            student_full_time=False,
            pregnant=False,
            unemployed=False,
            worked_in_last_18_mos=True,
            visually_impaired=False,
            disabled=False,
            veteran=False,
            has_income=False,
            has_expenses=False,
        )

    def test_every_day_eats_visually_impaired_is_eligible(self):
        ede = EveryDayEats(self.screen1)
        eligibility = ede.eligibility

        self.assertTrue(eligibility["eligible"])

    def test_every_day_eats_failed_all_conditions(self):
        income = IncomeStream.objects.create(
            screen=self.screen1, household_member=self.person1, type="wages", amount=3000, frequency="monthly"
        )
        self.person1.age = 30
        self.person1.save()

        ede = EveryDayEats(self.screen1)
        eligibility = ede.eligibility

        self.assertFalse(eligibility["eligible"])
