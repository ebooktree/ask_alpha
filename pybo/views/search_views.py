from datetime import datetime

from flask import Blueprint, render_template, request, url_for, g, flash, jsonify
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import SearchForm
from pybo.models import Search_Keyword_list, Search_Result_list

import json # 감정컬러 버튼 생성용 추가
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

bp = Blueprint('search', __name__, url_prefix='/search')

# 데이터 베이스에서 검색어 정보를 가져옴
@bp.route('/detail/')
def search_detail():
    form = SearchForm()
    with open(os.path.join(BASE_DIR, '..', 'data/emotion_2depth_colorrange.json'), 'r') as f:
        color_ranges = json.load(f)
    return render_template('search/search_detail.html', form=form, color_ranges=color_ranges)

# Added bp.route for search_form view
@bp.route('/search_form')
def search_form_route():
    form = SearchForm()
    return render_template('search/search_form.html', form=form)


# 검색 결과를 반환하는 함수 - 테스트
def get_search_results(input_keyword):
    with open(os.path.join(BASE_DIR, '..', 'data/book_happy_test.xlsx'), 'rb') as f:
        book_data = pd.read_excel(f, header=0)
    search_results = []
    input_keyword = input_keyword.lower()
    for index, column in book_data.iterrows():
        if input_keyword in column['emotion'].lower() and column['typeName'] == '도서':
            # cover_image = column['coverNo'].lower() +'.jpg'
            image_path = os.path.join(BASE_DIR, '..', 'data/book_happy_test', column['coverNo'] + '.jpg')
            search_results.append(
                {'emotion_keyword': column['emotion'], 'cover_number': column['coverNo'], 'book_name': column['titleInfo'], 'kind': column['typeName'], 'place': column['licText'], 'cover_image': column['coverNo'] + '.jpg'}
            )
    return search_results

# Modified search_result to a route function # #페이지 부분들 삭제하면, 동작함
@bp.route('/search_result', methods=['GET', 'POST'])
def search_result():
    form = SearchForm()
    search_results = []
    if request.method == 'POST' and form.validate_on_submit():
        keyword = form.keyword.data
        print(f"Input keyword: {keyword}")  # Debugging print statement
        search_results = get_search_results(keyword)
        print(f"Search results: {search_results}") # Debugging
    return render_template('search/search_result.html', form=form, search_results=search_results)

# "form" variable added to the function parameter
@bp.route('/emotion_buttons/')
def emotion_buttons():
    form = SearchForm()
    with open(os.path.join(BASE_DIR, '..', 'data/emotion_2depth_colorrange.json'), 'r') as f:
        color_ranges = json.load(f)
    return render_template('search/search_detail.html', form=form, color_ranges=color_ranges)
