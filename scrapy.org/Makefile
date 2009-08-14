export PYTHONPATH =: .

SETTINGS = export DJANGO_SETTINGS_MODULE=scrapyorg.settings

.PHONY : all build tests

all : build tests

tests :
	$(SETTINGS); \
	django-admin.py test
