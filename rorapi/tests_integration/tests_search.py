import os
import requests

from django.test import SimpleTestCase

BASE_URL = '{}/organizations'.format(
    os.environ.get('ROR_BASE_URL', 'http://localhost'))


class QueryTestCase(SimpleTestCase):

    def test_exact(self):
        items = requests.get(
            BASE_URL, {'query': 'Centro Universitário do Maranhão'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query': 'Julius-Maximilians-Universität Würzburg'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_lowercase(self):
        items = requests.get(
            BASE_URL, {'query': 'centro universitário do maranhão'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query': 'julius-maximilians-universität würzburg'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_accents_stripped(self):
        items = requests.get(
            BASE_URL, {'query': 'centro universitario do maranhao'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query': 'julius-maximilians-universitat wurzburg'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_extra_word(self):
        items = requests.get(
            BASE_URL,
            {'query': 'Centro Universitário do Maranhão School'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query': 'Julius-Maximilians-Universität Würzburg School'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')


class QueryFuzzyTestCase(SimpleTestCase):

    def test_exact(self):
        items = requests.get(
            BASE_URL, {'query': 'Centro~ Universitário~ do~ Maranhão~'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query': 'Julius~ Maximilians~ Universität~ Würzburg~'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_lowercase(self):
        items = requests.get(
            BASE_URL, {'query': 'centro~ universitário~ do~ maranhão~'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query': 'julius~ maximilians~ universität~ würzburg~'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_accents_stripped(self):
        items = requests.get(
            BASE_URL, {'query': 'centro~ universitario~ do~ maranhao~'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query': 'julius~ maximilians~ universitat~ wurzburg~'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_typos(self):
        items = requests.get(
            BASE_URL, {'query': 'centre~ universitario~ do~ marahao~'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query': 'julius~ maximilian~ universitat~ wuerzburg~'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_extra_word(self):
        items = requests.get(
            BASE_URL,
            {'query': 'Centro~ Universitário~ do~ Maranhão~ School~'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query':
             'Julius~ Maximilians~ Universität~ Würzburg~ School~'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')


class QueryNameTestCase(SimpleTestCase):

    def test_exact(self):
        items = requests.get(
            BASE_URL,
            {'query.name': 'Centro Universitário do Maranhão'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

    def test_lowercase(self):
        items = requests.get(
            BASE_URL,
            {'query.name': 'centro universitário do maranhão'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

    def test_accents_stripped(self):
        items = requests.get(
            BASE_URL,
            {'query.name': 'centro universitario do maranhao'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

    def test_typos(self):
        items = requests.get(
            BASE_URL, {'query.name': 'centre universitario do marahao'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

    def test_extra_word(self):
        items = requests.get(
            BASE_URL,
            {'query.name': 'Centro Universitário do Maranhão School'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')


class QueryNamesTestCase(SimpleTestCase):

    def test_exact(self):
        items = requests.get(
            BASE_URL,
            {'query.names': 'Centro Universitário do Maranhão'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query.names': 'Julius-Maximilians-Universität Würzburg'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_lowercase(self):
        items = requests.get(
            BASE_URL,
            {'query.names': 'centro universitário do maranhão'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query.names': 'julius-maximilians-universität würzburg'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_accents_stripped(self):
        items = requests.get(
            BASE_URL,
            {'query.names': 'centro universitario do maranhao'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query.names': 'julius-maximilians-universitat wurzburg'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_typos(self):
        items = requests.get(
            BASE_URL,
            {'query.names': 'centre universitario do marahao'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query.names': 'julius maximilian universitat wuerzburg'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_extra_word(self):
        items = requests.get(
            BASE_URL,
            {'query.names': 'Centro Universitário do Maranhão School'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query.names':
             'Julius-Maximilians-Universität Würzburg School'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')


class QueryUITestCase(SimpleTestCase):

    def test_exact(self):
        items = requests.get(
            BASE_URL,
            {'query.ui': 'Centro Universitário do Maranhão'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query.ui': 'Julius-Maximilians-Universität Würzburg'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_lowercase(self):
        items = requests.get(
            BASE_URL,
            {'query.ui': 'centro universitário do maranhão'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query.ui': 'julius-maximilians-universität würzburg'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_accents_stripped(self):
        items = requests.get(
            BASE_URL,
            {'query.ui': 'centro universitario do maranhao'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query.ui': 'julius-maximilians-universitat wurzburg'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_typos(self):
        items = requests.get(
            BASE_URL, {'query.ui': 'centre universitario do marahao'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query.ui': 'julius maximilian universitat wuerzburg'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')

    def test_extra_word(self):
        items = requests.get(
            BASE_URL,
            {'query.ui': 'Centro Universitário do Maranhão School'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/044g0p936')

        items = requests.get(
            BASE_URL,
            {'query.ui':
             'Julius-Maximilians-Universität Würzburg School'}).json()
        self.assertTrue(items['number_of_results'] > 0)
        self.assertEquals(items['items'][0]['id'], 'https://ror.org/00fbnyb24')
