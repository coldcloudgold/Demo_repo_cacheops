from django.test import TestCase


class DjangoPgReturningTest(TestCase):
    expected_error = ("'NoneType' object has no attribute 'lower'",)

    def test_import_abstract_model_with_app(self):
        """Importing an abstract model that has an application."""

        from .models import TestAbstractModel
        from cacheops.conf import model_profile

        self.assertEqual(model_profile(TestAbstractModel), None)

    def test_import_abstract_model_without_app(self):
        """Importing an abstract model that does not have an application.

        A model that does not have an application is expected to cause an error.
        """

        from .models import TestAbstractModel
        from cacheops.conf import model_profile

        TestAbstractModel._meta.app_label = None

        with self.assertRaises(AttributeError) as error:
            model_profile(TestAbstractModel)

        self.assertEqual(error.exception.args, self.expected_error)

    def test_import_update_returning_model(self):
        """Importing an abstract model that does not have an application.

        When using func bulk_update_or_create from the django_pg_bulk_update package,
        the django_pg_returning package is dynamically imported,
        which in turn imports the UpdateReturningModel. This model has no application.
        """

        with self.assertRaises(AttributeError) as error:
            from django_pg_returning.models import UpdateReturningModel

        self.assertEqual(error.exception.args, self.expected_error)
