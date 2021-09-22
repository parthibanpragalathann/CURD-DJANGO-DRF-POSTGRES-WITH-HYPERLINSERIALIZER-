from rest_framework.pagination import CursorPagination
from rest_framework import pagination

class CustomPageNumberPageination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = "count"
    max_page_size = 6
    page_query_param = 'p'

class CursorPaginationWithOrdering(CursorPagination):
    # order based on id
    ordering = 'id'