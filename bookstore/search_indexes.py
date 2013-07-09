from haystack import indexes

from bookstore.models import Author, Book

class BookIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document = True, use_template=True)
	author = indexes.CharField(model_attr = 'author')

	def get_model(self):
		return Book
	
	def index_queryset(self, using = None):
		"""
			Used when the entire index for model is updated.
		"""
		return self.get_model().objects.all()
