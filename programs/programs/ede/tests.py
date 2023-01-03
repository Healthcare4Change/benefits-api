from django.test import TestCase
from programs.programs.ede.ede import Ede
from screener.models import Screen, HouseholdMember, IncomeStream
from django.conf import settings


class TestEdePension(TestCase):
    def setUp(self):
        self.screen1 = Screen.objects.create(
            agree_to_tos=True,
            zipcode='80205',
            county='Denver County',
            household_size=1,
            household_assets=0,
        )
        self.person1 = HouseholdMember.objects.create(
            screen=self.screen1,
            relationship='headOfHousehold',
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

    def test_ede_visualy_impaired_is_eligible(self):
        ede = Ede(self.screen1)
        eligibility = ede.eligibility

        self.assertTrue(eligibility["eligible"])
        self.assertIn(
            f"Must have someone older that {Ede.min_age} in the house",
            eligibility['passed'])
        self.assertIn(
            f"Gross income of $0 must be less than ${1.3 * settings.FPL2022[1]}",
            eligibility['passed'])
        self.assertEqual(len(eligibility['failed']), 0)

    def test_ede_failed_all_conditions(self):
        income = IncomeStream.objects.create(
            screen=self.screen1,
            household_member=self.person1,
            type='wages',
            amount=3000,
            frequency='monthly'
        )
        self.person1.age = 30
        self.person1.save()

        ede = Ede(self.screen1)
        eligibility = ede.eligibility

        self.assertFalse(eligibility["eligible"])
        self.assertIn(
            f"Must have someone older that {Ede.min_age} in the house",
            eligibility['failed'])
        self.assertIn(
            f"Gross income of $36000.00 must be less than ${1.3 * settings.FPL2022[1]}",
            eligibility['failed'])
        self.assertEqual(len(eligibility['passed']), 0)
