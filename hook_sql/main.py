from hook_table import HookTable

if __name__ == '__main__':
    hook_table = HookTable()

    hook_table.execute()

    hook_table.query_id(smaller='id_smaller').query_url(equal='url_equal').execute()

    hook_table.reset()

    hook_table\
        .query_id(inside=['id_1', 'id_2', 'id_3'])\
        .query_date(equal='date_equal')\
        .query_rating(smaller='rating_smaller')\
        .execute()
