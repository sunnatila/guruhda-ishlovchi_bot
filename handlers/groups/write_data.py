import json

file_path = "data/groups/group_1.json"


def get_users(filename: str = file_path) -> list:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            if data:
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        with open(filename, 'w') as f:
            return []


def get_user(user_id: int, filename: str = file_path) -> list:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            if data:
                response = list(filter(lambda user: user['id'] == user_id, data))
                return response
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        with open(filename, 'w') as f:
            return []


def write_user(data: dict, filename: str = file_path) -> None:
    user_data = get_user(data['id'], filename)
    all_data = get_users(filename)
    if user_data:
        for user in user_data:
            all_data.remove(user)
    all_data.append(data)
    with open(filename, 'w') as f:
        json.dump(all_data, f, indent=4)


def clear_data(filename: str = file_path) -> None:
    try:
        with open(filename, 'w') as f:
            json.dump([], f, indent=4)
    except:
        return
