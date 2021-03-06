import pytest
import forecastvh

def test_search():
    w = forecastvh.get_weather('London', lang='ru')
    assert w.city == 'Лондон'

def test_search():
    w = forecastvh.get_weather('Londond')
    assert w.status == '404'

def test_search():
    w = forecastvh.get_weather('London', units='metri', lang='e') 
    assert w.status == '200'
