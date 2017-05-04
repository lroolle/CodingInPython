"""Customized filters
"""
import django_filters

from django.db.models import Value
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import FloatField, Case, When, F
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.compat import distinct

from ..utils.name_cut import get_name_cut


class SimilarSearchFilterMixin(object):
    """name_cut TrigramSimilarity search mixin
    For example:
        >>> class MyFilter(django_filters.FilterSet, SimilarSearchFilterMixin):
        >>>     similar_search = django_filters.MethodFilter(action='similar_search')

    """
    cut_field = 'name_cut'
    similarity = 0.1
    order_by = ('-similarity', )

    def similar_search(self, queryset, value):
        value_cut = get_name_cut(value)
        if not value_cut:
            return queryset

        filtered_similar = queryset.annotate(
            similarity=TrigramSimilarity(self.cut_field, value_cut)
        ).filter(
            similarity__gte=self.similarity
        ).order_by(*self.order_by)

        return filtered_similar[:10]


class NameSearchFilter(SearchFilter):
    """检索 Name 的时候，contains 结合 similar search
    """
    def get_search_terms(self, request):
        """
        Search terms are set by a ?search=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        name = request.query_params.get('name', None)
        similar_search = request.query_params.get('similar_search', None)
        params = request.query_params.get(self.search_param, '')
        return name or similar_search or params

    def filter_queryset(self, request, queryset, view):
        """Return queryset annotate s as Similarity

        similarity=TrigramSimilarity('name_cut', name_cut),
        s = 0.25 / similarity if name__startswith name
        s = 0.5 / similarity if name__contains name
        s = 1.0 / similarity if name_cut similar name_cut
        """
        name = self.get_search_terms(request)
        name_cut = get_name_cut(name)

        if not name or not name_cut:
            return queryset.annotate(s=Value(0.0, FloatField()))

        base = queryset
        queryset = queryset.annotate(
            similarity=TrigramSimilarity('name_cut', name_cut),
        ).annotate(
            s=Case(
                When(name__startswith=name, then=0.25 / (F('similarity') + 0.01)),
                When(name__contains=name, then=0.5 / (F('similarity') + 0.01)),
                default=1.0 / (F('similarity') + 0.01),
                output_field=FloatField(),
            )
        ).filter(s__lt=9).order_by('s')

        return distinct(queryset, base)


class DistinctOrderingFilter(OrderingFilter):
    """
    distinct field => in table => order by create_time
    """
    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        if request.query_params.get('distinct') == 'one':
            queryset = queryset.filter(
                id__in=queryset.values_list('id')
            ).distinct()

        if ordering:
            queryset = queryset.order_by(*ordering)

        return queryset
