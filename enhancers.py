def enhance_query_with_device_info(query, device_info):
    """
    Enhance the search query with additional device information.
    
    Parameters:
    query (str): The original query from the user.
    device_info (dict): The device information to enhance the query with.
    
    Returns:
    str: The enhanced query.
    """
    enhanced_query = f"{query} model: {device_info['model']}, year: {device_info['year']}".lower()
    print(f"DEBUG: enhanced_query = {enhanced_query}")
    return enhanced_query
