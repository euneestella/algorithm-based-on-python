def delete_nth(order,max_e):
    return [val for idx, val in enumerate(order) if order[:idx].count(val)<max_e]