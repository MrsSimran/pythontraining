def validate_eligibility(age, income, is_member):
    """
    Validate eligibility based on age, income, and membership status.

    Parameters:
        age (int): Age of the individual.
        income (float): Monthly income of the individual.
        is_member (bool): Whether the individual is a member or not.

    Returns:
        str: Eligibility result.
    """
    # Define the eligibility criteria
    min_age = 18
    max_age = 60
    min_income = 20000  # Minimum monthly income in currency
    required_membership = True

    # Check eligibility
    if age < min_age or age > max_age:
        return "Not eligible: Age criteria not met."
    if income < min_income:
        return "Not eligible: Income criteria not met."
    if required_membership and not is_member:
        return "Not eligible: Membership required."

    return "Congratulations! You are eligible."


# Example usage
if __name__ == "__main__":
    # Input data
    age = int(input("Enter your age: "))
    income = float(input("Enter your monthly income: "))
    is_member = input("Are you a member? (yes/no): ").strip().lower() == 'yes'

    # Validate and display result
    result = validate_eligibility(age, income, is_member)
    print(result)
