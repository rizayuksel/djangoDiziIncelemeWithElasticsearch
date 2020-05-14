from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from TvShow.models import TvShow

@registry.register_document
class TvShowDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'tvshow'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = TvShow # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id',
            'keywords',
            'title',
            'issue',
            'year',
            'season',
            'kind',
            'director',
            'performer',
            'imdbPoint',
        ]