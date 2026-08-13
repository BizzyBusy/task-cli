def isValidOp(input):
    """
    Returns True if the user's input is a valid operation, and False otherwise.
    
    The parameter input is a list containing the arguments provided by the user, starting at input[1] (input is the direct result of sys.argv function called during app startup, and thus input[0] does not contain relevant information).
    """

    if len(input) < 2:
        return False

    first_op = input[1].casefold()
    if first_op not in {"list", "add", "delete", "update", "mark-done", "mark-in-progress"}:
        return False

    try:
        second_op = input[2]
    except IndexError:
        if first_op == "list":
            return True
        return False

    if first_op != "update" and len(input) > 3:
        return False

    if first_op == "list":
        if second_op.casefold() not in {"done", "todo", "in-progress"}:
            return False
        return True
    elif first_op == "add":
        return True
    elif first_op in {"delete", "mark-done", "mark-in-progress", "update"}:
        try:
            #If we can't cast the second argument to an int, then it is not a number and is therefore invalid.
            int(second_op)
        except ValueError:
            return False

        if first_op != "update" or len(input) == 4:
            return True
        return False
   


#TODO 3: write functions that update JSON file (and creates it if it doesn't exist) based on the actions defined above

    # Add, Update, and Delete tasks: add, update, delete

    # Mark a task as in progress or done: mark-in-progress, mark-done

    # List all tasks: list

    # List all tasks that are done: list done

    # List all tasks that are not started: list todo

    # List all tasks that are in progress: list in-progress