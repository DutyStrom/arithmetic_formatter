# Arithmetic Formatter
# first Python project from freecodecamp.org website

# author: Petr Boček
# mail: Bocek2@seznam.cz
# Discord: Seth_Cz#8510
# GitHub: https://github.com/DutyStrom

# repo: https://github.com/DutyStrom/arithmetic_formatter.git

# --------------------------------------------------------

def arithmetic_arranger(
                        problems: list[str],
                        show_answers: bool = False
                        ) -> str:
    """
    Arrange a list of one-line mathematical problems into a vertical 
    format.

    Parameters:
    -----------
    problems : list(str)
        a list of mathemtical problems as strings
    show_answers : bool
        a print switch of mathematical problems results (default False)

    Returns:
    --------
    return verticaly arranged mathematical problems or appropriate error
    """
    
    separated_problems = [problem.split() for problem in problems]

    if len(problems) > 5:
        return f"Error: Too many problems."
    elif any(len(operand) > 4 
             for problem in separated_problems 
             for operand in problem):
        return f"Error: Numbers cannot be more than four digits."
    elif any(operator 
             in problem for problem in problems 
             for operator in ("/", "*")):
        return f"Error: Operator must be '+' or '-'."
    elif any(not problem.isdigit()
             for problems in separated_problems
             for problem in (problems[0], problems[2])):
        return f"Error: Numbers must only contain digits."
    else:
        first_line = ""
        second_line = ""
        third_line = ""
        result_line = ""

        for problem in separated_problems:
            alignment = max([len(operand) for operand in problem]) + 2

            first_line += f"{problem[0]:>{alignment}}{" " * 4}"
            second_line += (
                f"{problem[1]:<} {problem[2]:>{alignment-2}}"
                f"{" " * 4}"
            )
            third_line += f"{"-" * alignment}{" " * 4}"
            result_line += (
                f"{str(eval(" ".join(problem))):>{alignment}}"
                f"{" " * 4}"
            )

    return (
        f"{first_line.rstrip()}\n"
        f"{second_line.rstrip()}\n"
        f"{third_line.rstrip()}\n"
        f"{result_line.rstrip()}"
    ) if show_answers else (
        f"{first_line.rstrip()}\n"
        f"{second_line.rstrip()}\n"
        f"{third_line.rstrip()}"
    )
