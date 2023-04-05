from flask import Blueprint, request, jsonify
from pybo.models import Search_Keyword_list

bp = Blueprint('chatbot', __name__, url_prefix='/chatbot')

@bp.route('/search', methods=('POST',))
def search():
    request_json = request.get_json()
    keyword = request_json['keyword']

    # 검색어 DB에서 검색
    search_result = Search_Keyword_list.query.filter(Search_Keyword_list.keyword.like(f'%{keyword}%')).all()
    
    # 검색결과가 없을 경우
    if not search_result:
        return jsonify(result='fail', message='검색 결과가 없습니다.')
    
    # 검색결과가 있을 경우
    response_list = []
    for item in search_result:
        temp_dict = {}
        temp_dict['keyword'] = item.keyword
        temp_dict['category'] = item.category
        response_list.append(temp_dict)

    return jsonify(result='success', data=response_list)
