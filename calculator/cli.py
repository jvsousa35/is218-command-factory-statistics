"""Command line interface."""
from calculator.commands import (
    CalculateCommand,
    ClearHistoryCommand,
    HelpCommand,
    HistoryCommand,
)
from calculator.factory import CalculationFactory
from calculator.session import CalculatorSession


def prepare_command(text, session):
    parts = text.split()

    if not parts:
        message = "Enter a command; "
        message += "use help for examples."
        raise ValueError(message)

    name, *arguments = parts
    name = name.lower()

    actions = {
        "history": HistoryCommand,
        "clear": ClearHistoryCommand,
    }

    if name in actions:
        if arguments:
            message = f"{name} does not "
            message += "accept values."
            raise ValueError(message)

        return actions[name](session)

    if name == "help":
        if arguments:
            message = "help does not "
            message += "accept values."
            raise ValueError(message)

        return HelpCommand()

    values = []
    options = {}

    for argument in arguments:
        if "=" in argument:
            key, value = argument.split(
                "=",
                1
            )

            if not key or key in options:
                message = "Options need "
                message += "unique names: "
                message += "key=value."
                raise ValueError(message)

            options[key] = value

        else:
            values.append(argument)

    calculation = CalculationFactory.create(
        name,
        *values,
        **options
    )

    return CalculateCommand(
        session,
        calculation
    )


def run() -> None:
    session = CalculatorSession()

    print("Calculator")
    print(HelpCommand().execute())

    while True:
        try:
            text = input("> ").strip()

            if text.lower() == "exit":
                break

            command = prepare_command(
                text,
                session
            )

            print(command.execute())

        except (
            EOFError,
            KeyboardInterrupt,
        ):
            print()
            break

        except (
            ValueError,
            OSError,
            ZeroDivisionError,
            OverflowError,
        ) as error:
            print(f"Error: {error}")

    print("Goodbye!")
