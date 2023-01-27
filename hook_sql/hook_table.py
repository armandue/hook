from hook_data_access import HookDataAccess
from hook_query_util import IdQuery, UrlQuery, DateQuery, RatingQuery


class HookTable:

    table_name = 'hook_table'
    id_queries = []
    url_queries = []
    date_queries = []
    rating_queries = []
    hook_data_access = HookDataAccess()

    def query_id(self, smaller=None, bigger=None, equal=None, inside=None, not_inside=None):
        if smaller is not None:
            self.id_queries.append(IdQuery.smaller(id_=smaller))
        if bigger is not None:
            self.id_queries.append(IdQuery.bigger(id_=bigger))
        if equal is not None:
            self.id_queries.append(IdQuery.equal(id_=equal))
        if inside is not None:
            self.id_queries.append(IdQuery.inside(ids=inside))
        if not_inside is not None:
            self.id_queries.append(IdQuery.not_inside(ids=not_inside))

        return self

    def query_date(self, smaller=None, bigger=None, equal=None):
        if smaller is not None:
            self.date_queries.append(DateQuery.smaller(date=smaller))
        if bigger is not None:
            self.date_queries.append(DateQuery.bigger(date=bigger))
        if equal is not None:
            self.date_queries.append(DateQuery.equal(date=equal))

        return self

    def query_rating(self, smaller=None, bigger=None, equal=None):
        if smaller is not None:
            self.rating_queries.append(RatingQuery.smaller(rating=smaller))
        if bigger is not None:
            self.rating_queries.append(RatingQuery.bigger(rating=bigger))
        if equal is not None:
            self.rating_queries.append(RatingQuery.equal(rating=equal))

        return self

    def query_url(self, equal=None):
        if equal is not None:
            self.url_queries.append(UrlQuery.equal(equal))

        return self

    def execute(self):
        queries = self.id_queries + self.url_queries + self.date_queries + self.rating_queries
        return self.hook_data_access.execute(self.table_name, queries)

    def reset(self):
        self.id_queries = []
        self.url_queries = []
        self.date_queries = []
        self.rating_queries = []


