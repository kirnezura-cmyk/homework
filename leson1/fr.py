from loguru import logger

def get_multiplier() -> int | None:
    """
    Purpose: Ask user to get multiplicator
    :return: int value
    """
    question_to_user = "Enter a number only int: "
    user_input = input(question_to_user)

    if user_input.isdecimal():
        logger.info(f"User selected {user_input}")
        return int(user_input)

    logger.info(f"User selected wrong value = {user_input}")
    return None


def perform_multiplication_on_list(user_list: list[int], mult: int) -> list[int]:
    """
    Perform main task of homework
    :param user_list: list of user numbers
    :param mult: multiplicator type int
    :return: multiplied list
    """

    #  Variant I
    # for item in enumerate(user_list):
    #     index = item[0]
    #     value = item[1] * mult
    #     user_list[index] = value

    # Variant II
    new_list = [item * mult for item in user_list]

    # Variant III
    # result = list(map(lambda item: item * mult, user_list))

    return new_list



"""
 Homework
 Use list and each value multiply by given number
 1. List
 2. Multiplier
"""
if __name__ == '__main__':

    user_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    mult = get_multiplier()
    if mult is not None:
        searched_list = perform_multiplication_on_list(user_list, mult)
        logger.info(f"New list: {searched_list}")