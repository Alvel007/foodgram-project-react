from rest_framework.pagination import PageNumberPagination

from foodgram.settings import PAGINATION_SIZE


class CustomPagination(PageNumberPagination):
    page_size = PAGINATION_SIZE
    page_size_query_param = 'limit'
