from typing import List


class Program:
    """
    A class that represents a Program.

    Attributes:
        name (str): The name of the program.
        channel (str): The channel where the program is aired.
        published_at (str): The publication date of the program.
        duration (str): The duration of the program.
        summary (str): The summary of the program.
    """

    def __init__(self, unparsed_program: str) -> None:
        """
        Constructs all the necessary attributes for the Program object.

        Args:
            unparsed_program (str): Unparsed string containing program information.
        """
        parsed_program: List[str] = unparsed_program.split("; ")

        self.name: str = parsed_program.pop(0).strip()

        if "Chaîne" in parsed_program[0]:
            self.channel = parsed_program.pop(0).split(":")[1].strip()
        else:
            self.channel = None

        if "Diffusée ou publiée le" in parsed_program[0]:
            self.published_at = parsed_program.pop(0).split(":")[1].strip()
        else:
            self.published_at = None

        if "Durée" in parsed_program[0]:
            self.duration = parsed_program.pop(0).split(":")[1].strip()
        else:
            self.duration = None

        if "Résumé" in parsed_program[0]:
            self.summary = parsed_program.pop(0).split(":")[1].strip()
        else:
            self.summary = None

    def __str__(self) -> str:
        """
        Returns the string representation of the Program object.

        Returns:
            str: String representation of the Program object.
        """
        return f"Program: {self.name}, Channel: {self.channel}, Published At: {self.published_at}, Duration: {self.duration}, Summary: {self.summary}"

    def __repr__(self) -> str:
        """
        Returns the official string representation of the Program object.

        Returns:
            str: Official string representation of the Program object.
        """
        return f"Program('{self.name}', '{self.channel}', '{self.published_at}', '{self.duration}', '{self.summary}')"
