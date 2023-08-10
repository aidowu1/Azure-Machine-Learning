import argparse
from typing import Any
from pprint import pprint

NEW_LINE = "\n"
LINE_DIVIDER = "*****" * 6

class DemoUseOfArgParse(object):
    """
    Demos the use of argparse
    Argparse is used to facilitate the parametization of input arguments to python scripts
    """

    @staticmethod
    def reportPersonalDetails(
            first_name: str,
            second_name: str,
            address: str,
            age: int
    ) -> str:
        """
        Function used to create a report of user personal details
        :param first_name: First name
        :param second_name: Second Name
        :param address: Address
        :param age: Age
        :return: User personal report
        """
        report = f"Name: {first_name} {second_name}{NEW_LINE}"
        report = report + f"Address: {address}{NEW_LINE}"
        report = report + f"Age: {age}"
        return report

    @staticmethod
    def parseArgs() -> Any:
        """
        Parses the script input arguments
        :return:
        """
        # setup arg parser
        parser = argparse.ArgumentParser()

        # add arguments
        parser.add_argument(
            "--user_first_name",
            dest='user_first_name',
            type=str
        )

        parser.add_argument(
            "--user_surname",
            dest='user_surname',
            type=str
        )

        parser.add_argument(
            "--user_address",
            dest='user_address',
            type=str
        )

        parser.add_argument(
            "--user_age",
            dest='user_age',
            type=int
        )

        # parse args
        args = parser.parse_args()

        # return args
        return args

    @staticmethod
    def main():
        """
        Entry point
        :return: Main entry point used to execute the report
        """
        args = DemoUseOfArgParse.parseArgs()
        report = DemoUseOfArgParse.reportPersonalDetails(
            first_name=args.user_first_name,
            second_name=args.user_surname,
            address=args.user_address,
            age=args.user_age
        )
        print(f"The user personal report is:{NEW_LINE}")
        pprint(report)
        print(LINE_DIVIDER)
        print(NEW_LINE)


if __name__ == "__main__":
    DemoUseOfArgParse.main()