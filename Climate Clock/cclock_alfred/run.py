#PYTHON SCRIPT

from build.climate_clock_info_retrieve import get_info
from build.info_format_and_show import show_info
import json
import sys

def main():
    """
    This method is used to call climate clock api to retrieve info and put the info on the terminal.

    Returns:
        int: 0 Always for Success.1 for Failure.
    """
    try:
        list_info = get_info()
        vars = show_info(list_info)
        output_json = json.dumps({
            "items": vars
             }, indent=2)
        sys.stdout.write(output_json)
    except Exception as e:
        print("Error : \n{}".format(e))
        return 1

    return 0

if __name__ == "__main__":
    main()