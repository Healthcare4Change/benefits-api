import programs.programs.messages as messages


def calculate_lifeline(screen, data):
    eligibility = eligibility_lifeline(screen)
    value = value_lifeline(screen)

    calculation = {
        'eligibility': eligibility,
        'value': value
    }

    return calculation


def eligibility_lifeline(screen):

    eligibility = {
        "eligible": True,
        "passed": [],
        "failed": []
    }

    # Variables that may change over time
    # household size : income limit
    income_bands = {
        1: 18347,
        2: 24719,
        3: 31091,
        4: 37463,
        5: 43835,
        6: 50207,
        7: 56579,
        8: 62951
    }
    frequency = "yearly"

    income_limit = income_bands[screen.household_size]

    # INCOME TEST -- you can apply to Lifeline with only pay stubs,
    # so we limit to wages here
    income_types = ['all']
    lifeline_income = screen.calc_gross_income(frequency, income_types)

    if lifeline_income > income_limit:
        eligibility["eligible"] = False
        eligibility["failed"].append(messages.income(lifeline_income, income_limit))
    else:
        eligibility["passed"].append(messages.income(lifeline_income, income_limit))

    return eligibility


def value_lifeline(screen):
    value = 9.25 * 12

    return value