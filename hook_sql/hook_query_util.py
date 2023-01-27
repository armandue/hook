class IdQuery:

    @staticmethod
    def bigger(id_: str):
        return 'id > ' + id_

    @staticmethod
    def smaller(id_: str):
        return 'id < ' + id_

    @staticmethod
    def equal(id_: str):
        return 'id = ' + id_

    @staticmethod
    def inside(ids: [str]):
        return 'id IN (' + ','.join(ids) + ')'

    @staticmethod
    def not_inside(ids: [str]):
        return 'id NOT IN (' + ','.join(ids) + ')'


class UrlQuery:

    @staticmethod
    def equal(url: str):
        return 'url = ' + url


class DateQuery:

    @staticmethod
    def bigger(date: str):
        return 'date > ' + date

    @staticmethod
    def smaller(date: str):
        return 'date < ' + date

    @staticmethod
    def equal(date: str):
        return 'date = ' + date


class RatingQuery:

    @staticmethod
    def bigger(rating: str):
        return 'rating > ' + rating

    @staticmethod
    def smaller(rating: str):
        return 'rating < ' + rating

    @staticmethod
    def equal(rating: str):
        return 'rating = ' + rating
