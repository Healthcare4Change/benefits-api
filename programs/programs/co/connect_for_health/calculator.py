from programs.programs.calc import ProgramCalculator, Eligibility
from programs.programs.helpers import medicaid_eligible
import programs.programs.messages as messages
from integrations.services.sheets import GoogleSheetsCache


class CFHCache(GoogleSheetsCache):
    default = {}
    sheet_id = "1SuOhwX5psXsipMS_G5DE_f9jLS2qWxf6temxY445EQg"
    range_name = "'2023 report'!A2:B65"

    def update(self):
        data = super().update()

        return {d[0].strip() + " County": float(d[1].replace(",", "")) for d in data}


class ConnectForHealth(ProgramCalculator):
    percent_of_fpl = 4
    dependencies = ["insurance", "income_amount", "income_frequency", "county", "household_size"]
    county_values = CFHCache()

    def eligible(self) -> Eligibility:
        e = Eligibility()

        # Medicade eligibility
        e.condition(not medicaid_eligible(self.data), messages.must_not_have_benefit("Medicaid"))

        # Someone has no health insurance
        has_no_hi = self.screen.has_insurance_types(("none", "private"))
        e.condition(has_no_hi, messages.has_no_insurance())

        # HH member has no va insurance
        e.member_eligibility(
            self.screen.household_members.all(),
            [(lambda m: not m.insurance.has_insurance_types(("va", "private")), messages.must_not_have_benefit("VA"))],
        )

        # Income
        fpl = self.program.fpl.as_dict()
        income_band = int(fpl[self.screen.household_size] / 12 * ConnectForHealth.percent_of_fpl)
        gross_income = int(self.screen.calc_gross_income("yearly", ("all",)) / 12)
        e.condition(gross_income < income_band, messages.income(gross_income, income_band))

        return e

    def value(self, eligible_members: int):
        values = self.county_values.fetch()
        return values[self.screen.county] * 12
