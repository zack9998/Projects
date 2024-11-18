# utils.py

def get_user_choice():
    """Prompt the user for a choice and return it in lowercase, stripped of whitespace."""
    return input("Please enter your choice (add/view/remove/exit): ").strip().lower()
