from utils import extract_sqft, process_property, numbers_only, extract_pcm
from PIL import Image
import PIL
import re
import glob
import pytest

fileformat_pattern = r'(/)(\d+)(.)'
file_without_case = re.compile(fileformat_pattern, re.IGNORECASE)


def test_numbers_only():
    assert numbers_only('abc123') == '123'
    assert numbers_only(999) == '999'
    assert numbers_only('') == ''
    assert numbers_only('$£3758324.jdfj1') == '3758324.1'


def test_extract_pcm():
    assert extract_pcm('£2,800 (pcm)') == '2800'
    assert extract_pcm('£2,500 pcm') == '2500'


def test_extract_pcm_bad_input():
    with pytest.raises(Exception):
        extract_pcm('£2,500') == '£2,500'


def test_extract_sqft():
    for filename in glob.glob('test_floorplans/*.*'):
        target_sqft = int(file_without_case.findall(filename)[0][1])
        print(f'target: {target_sqft}')

        parsed_sqft = extract_sqft(Image.open(filename))
        print(f"parsed: {parsed_sqft}")

        assert target_sqft == parsed_sqft


def test_crawl_end():
    pass
