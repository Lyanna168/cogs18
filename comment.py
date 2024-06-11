"""Script to run some part of my project."""

"""
Manage user comments or feedback.
"""

def add_comment(user, comment):
    """
    Add a comment from the user.
    
    Parameters:
    user (User): The user object.
    comment (str): The comment text.
    
    Returns:
    str: Confirmation of comment addition.
    """
    # Example comment logic
    return f"Comment added for {user.name}: {comment}"
