def run_script(script_name):
    """
    Runs a Python script as a module.

    Args:
    script_name (str): The name of the script without the '.py' extension.

    Returns:
    bool: True if the script ran successfully, False otherwise.
    """
    try:
        module = __import__(script_name)
        return True
    except Exception as e:
        print(f"Error running {script_name}.py: {e}")
        return False

def main():
    if run_script('web_dish'):
        if run_script('merge'):
            run_script('return_json')
        else:
            print("merge.py failed to execute.")
    else:
        print("web_dish.py failed to execute.")

if __name__ == "__main__":
    main()
