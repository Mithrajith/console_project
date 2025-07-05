def parse_date(date_string):
    from datetime import datetime
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return None

def format_date(date_object):
    return date_object.strftime("%Y-%m-%d")

def validate_input(input_value, valid_options):
    if input_value not in valid_options:
        raise ValueError(f"Invalid input: {input_value}. Valid options are: {valid_options}")

def generate_unique_id():
    import uuid
    return str(uuid.uuid4())