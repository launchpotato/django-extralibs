from django.test import TestCase

from launchpotato_extralibs.phone import phone_format


class PhoneFormatTestCase(TestCase):

    def test_phone_format_method(self):

        with self.subTest("Test passing None value"):
            result = phone_format('xxx-xxx-xxxx', None)
            self.assertEqual(result, '')

        with self.subTest("Test passing blank value"):
            result = phone_format('xxx-xxx-xxxx', '')
            self.assertEqual(result, '-   -')

        with self.subTest("Test passing correct value and 'xxx-xxx-xxxx'"):
            result = phone_format('xxx-xxx-xxxx', '8881234567')
            self.assertEqual(result, '888-123-4567')

        with self.subTest("Test passing correct value and '(xxx) xxx-xxxx'"):
            result = phone_format('(xxx) xxx-xxxx', '8881234567')
            self.assertEqual(result, '(888) 123-4567')

        with self.subTest("Test passing correct value and '(xxx) xxx-xxxx'"):
            result = phone_format('xxxxxxxxxx', '8881234567')
            self.assertEqual(result, '8881234567')

    def test_phone_format_filter(self):

        import django
        django.setup()
        from django.template import Template, Context

        context = Context({'phone': '8881234567'})

        with self.subTest('Test {{ phone|phone_format:"xxx-xxx-xxxx" }} formatting'):
            template = Template('{% load phone_tags %}phone: {{ phone|phone_format:"xxx-xxx-xxxx" }}')
            result = template.render(context)
            self.assertEqual(result, 'phone: 888-123-4567')

        with self.subTest('Test {{ phone|phone_format:"(xxx) xxx xxxx" }} formatting'):
            template = Template('{% load phone_tags %}phone: {{ phone|phone_format:"(xxx) xxx xxxx" }}')
            result = template.render(context)
            self.assertEqual(result, 'phone: (888) 123 4567')

        with self.subTest('Test {{ phone|phone_format:"xxxxxxxxxx" }} formatting'):
            template = Template('{% load phone_tags %}phone: {{ phone|phone_format:"xxxxxxxxxx" }}')
            result = template.render(context)
            self.assertEqual(result, 'phone: 8881234567')

        with self.subTest('Test {{ phone|phone_format:"xxx xxx xxxx" }} formatting'):
            template = Template('{% load phone_tags %}phone: {{ phone|phone_format:"xxx xxx xxxx" }}')
            result = template.render(context)
            self.assertEqual(result, 'phone: 888 123 4567')
