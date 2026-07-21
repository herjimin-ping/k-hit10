"""
대한민국 연도별 소비 타임라인 (2000~2026) - 단일 파일 버전
--------------------------------------------------------------
한 해를 대표하는 소비 트렌드를 연도별로 이어서 보여주는 Streamlit 앱입니다.

- 2000~2012년: 삼성경제연구소(SERI)의 '10대 히트상품'
  (SERI가 2010년경 대외활동을 중단하며 2012년을 끝으로 조사 종료)
- 2013~2026년: 서울대 소비트렌드분석센터 <트렌드 코리아> 시리즈의
  연도별 10대 소비트렌드 키워드
  (<트렌드 코리아>는 2007년부터 축적, 첫 출간은 『트렌드 코리아 2009』)

즉 두 자료를 이어 붙여 2000년부터 2026년까지 끊김 없이 살펴볼 수 있습니다.

실행 방법 (로컬):
    pip install streamlit
    streamlit run consumption-timeline.py
"""

import json
import streamlit as st

DATA_JSON = r"""{
  "2000": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2000년 10대 히트상품 (전자신문 2000.12.30 보도, SERI 홈페이지 seri.org 발표 내용 인용)",
    "source_url": "https://www.etnews.com/200012280217",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "아이러브스쿨",
        "name_en": null,
        "description": "동창 찾기 웹사이트로, 온라인을 통해 옛 동창을 찾고 오프라인 동창회 문화를 확산시킨 한국 초기 SNS의 원조 격 서비스였다.",
        "link": "https://www.google.com/search?q=2000+삼성경제연구소+10대+히트상품+아이러브스쿨"
      },
      {
        "rank": 2,
        "name": "애니콜 듀얼폴더",
        "name_en": null,
        "description": "삼성 애니콜 브랜드의 폴더형 휴대폰으로, 폴더 디자인 유행을 이끈 인기 모델이었다.",
        "link": "https://www.google.com/search?q=2000+삼성경제연구소+10대+히트상품+애니콜 듀얼폴더"
      },
      {
        "rank": 3,
        "name": "허준(드라마)",
        "name_en": null,
        "description": "조선시대 명의 허준의 일대기를 그린 MBC 드라마로, 방영 내내 폭발적인 시청률을 기록했다.",
        "link": "https://www.google.com/search?q=2000+삼성경제연구소+10대+히트상품+허준(드라마)"
      },
      {
        "rank": 4,
        "name": "신용카드",
        "name_en": null,
        "description": "카드 사용 활성화 정책과 맞물려 신용카드 발급과 사용이 크게 늘며 소비 문화를 바꿔놓았다.",
        "link": "https://www.google.com/search?q=2000+삼성경제연구소+10대+히트상품+신용카드"
      },
      {
        "rank": 5,
        "name": "공동경비구역 JSA(영화)",
        "name_en": null,
        "description": "박찬욱 감독의 영화로, 판문점 공동경비구역을 배경으로 남북 분단의 비극을 그려 큰 흥행을 거뒀다.",
        "link": "https://www.google.com/search?q=2000+삼성경제연구소+10대+히트상품+공동경비구역 JSA(영화)"
      },
      {
        "rank": 6,
        "name": "웅진 초록매실(음료)",
        "name_en": null,
        "description": "매실을 활용한 음료로, 웅진식품이 내놓아 큰 인기를 끌며 과실음료 시장의 대표 상품이 되었다.",
        "link": "https://www.google.com/search?q=2000+삼성경제연구소+10대+히트상품+웅진 초록매실(음료)"
      },
      {
        "rank": 7,
        "name": "킥보드",
        "name_en": null,
        "description": "접이식 킥보드가 어린이와 청소년들 사이에서 새로운 놀이 도구로 선풍적인 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2000+삼성경제연구소+10대+히트상품+킥보드"
      },
      {
        "rank": 8,
        "name": "만도위니아 딤채",
        "name_en": null,
        "description": "세계 최초의 김치냉장고 브랜드로, 발효 음식 문화에 맞춘 전용 가전으로 큰 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2000+삼성경제연구소+10대+히트상품+만도위니아 딤채"
      },
      {
        "rank": 9,
        "name": "SK 엔크린 보너스카드",
        "name_en": null,
        "description": "SK주유소 이용 시 포인트를 적립해주는 보너스카드로, 초기 포인트 마케팅의 대표 사례였다.",
        "link": "https://www.google.com/search?q=2000+삼성경제연구소+10대+히트상품+SK 엔크린 보너스카드"
      },
      {
        "rank": 10,
        "name": "한국통신 메가패스",
        "name_en": null,
        "description": "한국통신(현 KT)의 초고속인터넷 브랜드로, 국내 초고속인터넷 대중화를 이끌었다.",
        "link": "https://www.google.com/search?q=2000+삼성경제연구소+10대+히트상품+한국통신 메가패스"
      }
    ]
  },
  "2001": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2001년 10대 히트상품 (마케팅 사례 연구 블로그 '꿈꾸는섬' 인용 기사 기반, 권성용 연구원 코멘트 포함)",
    "source_url": "https://happist.com/page/465?I=n&l=es&m=0&mid=Internet&page=1",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "영화 \"친구\"",
        "name_en": null,
        "description": "곽경택 감독의 영화로, 전국 820만 관객을 동원해 당시 '쉬리', 'JSA' 등을 뛰어넘는 최고 흥행 기록을 세웠다. 2001년 최고의 히트상품으로 꼽혔다.",
        "link": "https://www.google.com/search?q=2001+삼성경제연구소+10대+히트상품+영화 \"친구\""
      },
      {
        "rank": 2,
        "name": "OK캐쉬백",
        "name_en": null,
        "description": "SK가 선보인 포인트 적립·통합 서비스로, 다양한 제휴사에서 포인트를 모으고 쓸 수 있게 하며 큰 인기를 끌었다. (※원문에 2위 이하 순위 숫자가 명시되지 않아, 기사에 나열된 순서를 따랐습니다.)",
        "link": "https://www.google.com/search?q=2001+삼성경제연구소+10대+히트상품+OK캐쉬백"
      },
      {
        "rank": 3,
        "name": "롯데 자일리톨껌",
        "name_en": null,
        "description": "충치 예방 기능성을 앞세운 무설탕 껌으로, 제과업계 최초로 월 매출 100억원을 돌파하며 시장 점유율을 크게 끌어올렸다.",
        "link": "https://www.google.com/search?q=2001+삼성경제연구소+10대+히트상품+롯데 자일리톨껌"
      },
      {
        "rank": 4,
        "name": "삼성전자 콤보",
        "name_en": null,
        "description": "비디오테이프(VCR)와 DVD 재생 기능을 하나로 합친 복합 가전제품으로, 두 매체가 공존하던 과도기에 큰 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2001+삼성경제연구소+10대+히트상품+삼성전자 콤보"
      },
      {
        "rank": 5,
        "name": "TV 홈쇼핑",
        "name_en": null,
        "description": "TV 방송을 통해 상품을 소개하고 즉시 구매할 수 있는 홈쇼핑 채널이 새로운 유통 서비스로 자리잡았다.",
        "link": "https://www.google.com/search?q=2001+삼성경제연구소+10대+히트상품+TV 홈쇼핑"
      },
      {
        "rank": 6,
        "name": "르노삼성자동차 SM5",
        "name_en": null,
        "description": "르노삼성자동차가 선보인 중형 세단으로, 안정적인 성능과 디자인으로 국내 자동차 시장에서 큰 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2001+삼성경제연구소+10대+히트상품+르노삼성자동차 SM5"
      },
      {
        "rank": 7,
        "name": "대형평면TV",
        "name_en": null,
        "description": "기존 브라운관 TV보다 화면이 평평하고 커진 대형 평면 TV가 새로운 가전 트렌드로 떠올랐다.",
        "link": "https://www.google.com/search?q=2001+삼성경제연구소+10대+히트상품+대형평면TV"
      },
      {
        "rank": 8,
        "name": "아바타",
        "name_en": null,
        "description": "인터넷 커뮤니티·채팅 서비스에서 자신을 표현하는 캐릭터인 아바타를 꾸미는 서비스가 큰 인기를 끌며 인터넷 서비스 시장의 새로운 수익모델이 되었다.",
        "link": "https://www.google.com/search?q=2001+삼성경제연구소+10대+히트상품+아바타"
      },
      {
        "rank": 9,
        "name": "종신보험",
        "name_en": null,
        "description": "경제 불확실성이 커지며 평생 보장을 내세운 종신보험 등 금융·보험 상품에 대한 수요가 크게 늘었다.",
        "link": "https://www.google.com/search?q=2001+삼성경제연구소+10대+히트상품+종신보험"
      },
      {
        "rank": 10,
        "name": "브랜드쌀",
        "name_en": null,
        "description": "산지와 품질을 브랜드화한 프리미엄 쌀 상품들이 등장하며 쌀 시장에도 브랜드 경쟁이 시작되었다.",
        "link": "https://www.google.com/search?q=2001+삼성경제연구소+10대+히트상품+브랜드쌀"
      }
    ]
  },
  "2002": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2002년 10대 히트상품 (블로그 정리 이미지 자료 기반)",
    "source_url": "https://blog.naver.com/pooh1387/130154011523",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "월드컵",
        "name_en": null,
        "description": "2002 한일 월드컵에서 한국 축구대표팀이 4강 신화를 쓰며 전국을 붉게 물들인 해였다. (기타 화제: 요가, 반신욕, 소형 SUV, 드라마 '이순신' 등)",
        "link": "https://www.google.com/search?q=2002+삼성경제연구소+10대+히트상품+월드컵"
      },
      {
        "rank": 2,
        "name": "컬러휴대폰",
        "name_en": null,
        "description": "흑백 액정이 대세이던 시절, 컬러 디스플레이를 탑재한 휴대폰이 새로운 표준으로 떠올랐다. (기타 화제: 요가, 반신욕, 소형 SUV, 드라마 '이순신' 등)",
        "link": "https://www.google.com/search?q=2002+삼성경제연구소+10대+히트상품+컬러휴대폰"
      },
      {
        "rank": 3,
        "name": "메이드인차이나",
        "name_en": null,
        "description": "저렴한 중국산 제품들이 국내 시장에 본격적으로 유입되기 시작했다. (기타 화제: 요가, 반신욕, 소형 SUV, 드라마 '이순신' 등)",
        "link": "https://www.google.com/search?q=2002+삼성경제연구소+10대+히트상품+메이드인차이나"
      },
      {
        "rank": 4,
        "name": "주상복합아파트",
        "name_en": null,
        "description": "주거와 상업시설을 한 건물에 결합한 주상복합 아파트가 인기 주거 형태로 떠올랐다. (기타 화제: 요가, 반신욕, 소형 SUV, 드라마 '이순신' 등)",
        "link": "https://www.google.com/search?q=2002+삼성경제연구소+10대+히트상품+주상복합아파트"
      },
      {
        "rank": 5,
        "name": "홈시어터",
        "name_en": null,
        "description": "가정에서 극장 같은 음향·영상을 즐기는 홈시어터 시스템이 인기를 끌었다. (기타 화제: 요가, 반신욕, 소형 SUV, 드라마 '이순신' 등)",
        "link": "https://www.google.com/search?q=2002+삼성경제연구소+10대+히트상품+홈시어터"
      },
      {
        "rank": 6,
        "name": "영어학습",
        "name_en": null,
        "description": "영어 조기교육 열풍과 함께 다양한 영어학습 상품·서비스가 확산되었다. (기타 화제: 요가, 반신욕, 소형 SUV, 드라마 '이순신' 등)",
        "link": "https://www.google.com/search?q=2002+삼성경제연구소+10대+히트상품+영어학습"
      },
      {
        "rank": 7,
        "name": "테이크아웃점",
        "name_en": null,
        "description": "커피 등을 포장해 들고 가는 테이크아웃 매장 문화가 확산되기 시작했다. (기타 화제: 요가, 반신욕, 소형 SUV, 드라마 '이순신' 등)",
        "link": "https://www.google.com/search?q=2002+삼성경제연구소+10대+히트상품+테이크아웃점"
      },
      {
        "rank": 8,
        "name": "변형명품(짝퉁)",
        "name_en": null,
        "description": "유명 브랜드를 모방한 이미테이션(짝퉁) 제품 거래가 크게 늘었다. (기타 화제: 요가, 반신욕, 소형 SUV, 드라마 '이순신' 등)",
        "link": "https://www.google.com/search?q=2002+삼성경제연구소+10대+히트상품+변형명품(짝퉁)"
      },
      {
        "rank": 9,
        "name": "책책책 책을 읽읍시다",
        "name_en": null,
        "description": "TV 프로그램을 계기로 독서 캠페인이 확산되며 베스트셀러 열풍을 일으켰다. (기타 화제: 요가, 반신욕, 소형 SUV, 드라마 '이순신' 등)",
        "link": "https://www.google.com/search?q=2002+삼성경제연구소+10대+히트상품+책책책 책을 읽읍시다"
      },
      {
        "rank": 10,
        "name": "한방제품",
        "name_en": null,
        "description": "한방 성분을 활용한 화장품·건강식품 등이 새로운 소비 트렌드로 떠올랐다. (기타 화제: 요가, 반신욕, 소형 SUV, 드라마 '이순신' 등)",
        "link": "https://www.google.com/search?q=2002+삼성경제연구소+10대+히트상품+한방제품"
      }
    ]
  },
  "2003": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2003년 10대 히트상품 (블로그 정리 이미지 자료 기반)",
    "source_url": "https://blog.naver.com/pooh1387/130154011523",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "디지털포토",
        "name_en": null,
        "description": "디지털카메라가 대중화되며 사진을 찍고 인화하는 방식이 크게 바뀌었다. (기타 화제: iPod 등)",
        "link": "https://www.google.com/search?q=2003+삼성경제연구소+10대+히트상품+디지털포토"
      },
      {
        "rank": 2,
        "name": "로또",
        "name_en": null,
        "description": "복권 '로또'가 처음 도입되며 전 국민적인 열풍을 일으켰다. (기타 화제: iPod 등)",
        "link": "https://www.google.com/search?q=2003+삼성경제연구소+10대+히트상품+로또"
      },
      {
        "rank": 3,
        "name": "신가전",
        "name_en": null,
        "description": "기존과 다른 새로운 개념의 가전제품들이 잇따라 출시되며 주목받았다. (기타 화제: iPod 등)",
        "link": "https://www.google.com/search?q=2003+삼성경제연구소+10대+히트상품+신가전"
      },
      {
        "rank": 4,
        "name": "웰빙상품",
        "name_en": null,
        "description": "건강과 삶의 질을 중시하는 '웰빙' 트렌드가 확산되며 관련 상품이 크게 늘었다. (기타 화제: iPod 등)",
        "link": "https://www.google.com/search?q=2003+삼성경제연구소+10대+히트상품+웰빙상품"
      },
      {
        "rank": 5,
        "name": "퓨전사극",
        "name_en": null,
        "description": "기존 정통 사극과 다른 새로운 형식의 퓨전 사극 드라마들이 인기를 끌었다. (기타 화제: iPod 등)",
        "link": "https://www.google.com/search?q=2003+삼성경제연구소+10대+히트상품+퓨전사극"
      },
      {
        "rank": 6,
        "name": "재테크서적",
        "name_en": null,
        "description": "개인 재테크에 대한 관심이 높아지며 관련 서적들이 큰 인기를 끌었다. (기타 화제: iPod 등)",
        "link": "https://www.google.com/search?q=2003+삼성경제연구소+10대+히트상품+재테크서적"
      },
      {
        "rank": 7,
        "name": "수입차",
        "name_en": null,
        "description": "수입 자동차의 국내 진입이 확대되며 대중화의 문이 열렸다. (기타 화제: iPod 등)",
        "link": "https://www.google.com/search?q=2003+삼성경제연구소+10대+히트상품+수입차"
      },
      {
        "rank": 8,
        "name": "지하철 신문",
        "name_en": null,
        "description": "무료로 배포되는 지하철 신문이 통근·통학 시민들의 필수 아이템이 되었다. (기타 화제: iPod 등)",
        "link": "https://www.google.com/search?q=2003+삼성경제연구소+10대+히트상품+지하철 신문"
      },
      {
        "rank": 9,
        "name": "지식검색",
        "name_en": null,
        "description": "네이버 지식iN 등 이용자 참여형 지식검색 서비스가 큰 인기를 끌었다. (기타 화제: iPod 등)",
        "link": "https://www.google.com/search?q=2003+삼성경제연구소+10대+히트상품+지식검색"
      },
      {
        "rank": 10,
        "name": "이민상품",
        "name_en": null,
        "description": "해외 이민에 대한 관심이 높아지며 관련 상품·서비스 문의가 늘었다. (기타 화제: iPod 등)",
        "link": "https://www.google.com/search?q=2003+삼성경제연구소+10대+히트상품+이민상품"
      }
    ]
  },
  "2004": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2004년 10대 히트상품 (블로그 정리 이미지 자료 기반)",
    "source_url": "https://blog.naver.com/pooh1387/130154011523",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "싸이월드",
        "name_en": null,
        "description": "미니홈피 기반의 소셜 서비스 싸이월드가 폭발적인 인기를 끌며 1인 미디어 시대를 열었다. (기타 화제: 초슬림 휴대폰 등)",
        "link": "https://www.google.com/search?q=2004+삼성경제연구소+10대+히트상품+싸이월드"
      },
      {
        "rank": 2,
        "name": "복합기능휴대폰",
        "name_en": null,
        "description": "카메라, MP3 재생 등 다양한 기능을 갖춘 복합기능 휴대폰이 대세로 떠올랐다. (기타 화제: 초슬림 휴대폰 등)",
        "link": "https://www.google.com/search?q=2004+삼성경제연구소+10대+히트상품+복합기능휴대폰"
      },
      {
        "rank": 3,
        "name": "비타500",
        "name_en": null,
        "description": "비타민 음료 '비타500'이 출시되며 건강음료 시장에서 큰 히트를 기록했다. (기타 화제: 초슬림 휴대폰 등)",
        "link": "https://www.google.com/search?q=2004+삼성경제연구소+10대+히트상품+비타500"
      },
      {
        "rank": 4,
        "name": "한류스타(욘사마)",
        "name_en": null,
        "description": "배용준 등 한류 스타들이 일본을 비롯한 해외에서 폭발적인 인기를 끌었다. (기타 화제: 초슬림 휴대폰 등)",
        "link": "https://www.google.com/search?q=2004+삼성경제연구소+10대+히트상품+한류스타(욘사마)"
      },
      {
        "rank": 5,
        "name": "대용량 MP3",
        "name_en": null,
        "description": "저장 용량이 크게 늘어난 MP3플레이어가 음악 감상 문화를 바꿔놓았다. (기타 화제: 초슬림 휴대폰 등)",
        "link": "https://www.google.com/search?q=2004+삼성경제연구소+10대+히트상품+대용량 MP3"
      },
      {
        "rank": 6,
        "name": "저가화장품",
        "name_en": null,
        "description": "미샤 등 저가형 화장품 브랜드들이 등장하며 화장품 시장의 판도를 바꿨다. (기타 화제: 초슬림 휴대폰 등)",
        "link": "https://www.google.com/search?q=2004+삼성경제연구소+10대+히트상품+저가화장품"
      },
      {
        "rank": 7,
        "name": "파리의연인",
        "name_en": null,
        "description": "SBS 드라마 '파리의 연인'이 신드롬급 인기를 끌며 명대사 열풍을 낳았다. (기타 화제: 초슬림 휴대폰 등)",
        "link": "https://www.google.com/search?q=2004+삼성경제연구소+10대+히트상품+파리의연인"
      },
      {
        "rank": 8,
        "name": "마법천자문",
        "name_en": null,
        "description": "한자를 재미있게 배우는 학습만화 '마법천자문'이 어린이들 사이에서 큰 인기를 끌었다. (기타 화제: 초슬림 휴대폰 등)",
        "link": "https://www.google.com/search?q=2004+삼성경제연구소+10대+히트상품+마법천자문"
      },
      {
        "rank": 9,
        "name": "주택장기대출",
        "name_en": null,
        "description": "장기주택담보대출 상품이 확산되며 내 집 마련의 새로운 방법으로 자리잡았다. (기타 화제: 초슬림 휴대폰 등)",
        "link": "https://www.google.com/search?q=2004+삼성경제연구소+10대+히트상품+주택장기대출"
      },
      {
        "rank": 10,
        "name": "매운음식",
        "name_en": null,
        "description": "불닭 등 매운맛을 강조한 음식들이 큰 유행을 일으켰다. (기타 화제: 초슬림 휴대폰 등)",
        "link": "https://www.google.com/search?q=2004+삼성경제연구소+10대+히트상품+매운음식"
      }
    ]
  },
  "2005": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2005년 10대 히트상품 (블로그 정리 이미지 자료 기반)",
    "source_url": "https://blog.naver.com/pooh1387/130154011523",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "청계천",
        "name_en": null,
        "description": "서울 도심 한복판에 복원된 하천으로, 콘크리트 복개도로를 걷어내고 자연을 되살린 대표적 도시재생 사례. 응답자 특성과 무관하게 폭넓은 지지를 얻어 1위를 차지했다. (기타 화제: 블랙 컬러 휴대폰 등)",
        "link": "https://www.google.com/search?q=2005+삼성경제연구소+10대+히트상품+청계천"
      },
      {
        "rank": 2,
        "name": "블루오션 전략",
        "name_en": null,
        "description": "경쟁이 치열한 기존 시장(레드오션) 대신 경쟁이 없는 미개척 시장을 창출해 고수익을 노리는 전략을 제시한 경영서적. (기타 화제: 블랙 컬러 휴대폰 등)",
        "link": "https://www.google.com/search?q=2005+삼성경제연구소+10대+히트상품+블루오션 전략"
      },
      {
        "rank": 3,
        "name": "위성DMB폰",
        "name_en": null,
        "description": "이동 중에도 위성을 통해 멀티미디어 방송을 시청할 수 있게 한 휴대전화. (기타 화제: 블랙 컬러 휴대폰 등)",
        "link": "https://www.google.com/search?q=2005+삼성경제연구소+10대+히트상품+위성DMB폰"
      },
      {
        "rank": 4,
        "name": "주식형 간접투자상품(펀드)",
        "name_en": null,
        "description": "개인이 직접 주식에 투자하는 대신 펀드를 통해 간접적으로 투자하는 방식이 대중화되며 큰 인기를 끌었다. (기타 화제: 블랙 컬러 휴대폰 등)",
        "link": "https://www.google.com/search?q=2005+삼성경제연구소+10대+히트상품+주식형 간접투자상품(펀드)"
      },
      {
        "rank": 5,
        "name": "이종격투기 K-1",
        "name_en": null,
        "description": "복싱, 레슬링, 태권도 등 다양한 격투기술이 혼합된 스포츠 엔터테인먼트로, TV 중계를 통해 폭넓은 인기를 얻었다. (기타 화제: 블랙 컬러 휴대폰 등)",
        "link": "https://www.google.com/search?q=2005+삼성경제연구소+10대+히트상품+이종격투기 K-1"
      },
      {
        "rank": 6,
        "name": "억척녀 주인공 TV드라마(금순이,삼순이,맹순이)",
        "name_en": null,
        "description": "기존의 공주풍·순종적 여성 캐릭터와 달리, 솔직하고 생활력 강한 여성 주인공을 내세운 드라마들이 큰 반향을 일으켰다. (기타 화제: 블랙 컬러 휴대폰 등)",
        "link": "https://www.google.com/search?q=2005+삼성경제연구소+10대+히트상품+억척녀 주인공 TV드라마(금순이,삼순이,맹순이)"
      },
      {
        "rank": 7,
        "name": "카트라이더",
        "name_en": null,
        "description": "넥슨의 온라인 캐주얼 레이싱 게임. 남녀노소 누구나 즐길 수 있는 가벼운 재미로 선풍적 인기를 끌었다. (기타 화제: 블랙 컬러 휴대폰 등)",
        "link": "https://www.google.com/search?q=2005+삼성경제연구소+10대+히트상품+카트라이더"
      },
      {
        "rank": 8,
        "name": "네비게이션",
        "name_en": null,
        "description": "차량용 위성항법장치(GPS 내비게이션)가 대중화되며 새로운 디지털 라이프스타일 제품으로 인기를 끌었다. (기타 화제: 블랙 컬러 휴대폰 등)",
        "link": "https://www.google.com/search?q=2005+삼성경제연구소+10대+히트상품+네비게이션"
      },
      {
        "rank": 9,
        "name": "영화 \"웰컴 투 동막골\"",
        "name_en": null,
        "description": "한국전쟁 중 강원도 산골 마을을 배경으로 남북 병사들의 우정을 그린 영화. 평화와 온정을 주제로 큰 흥행을 거뒀다. (기타 화제: 블랙 컬러 휴대폰 등)",
        "link": "https://www.google.com/search?q=2005+삼성경제연구소+10대+히트상품+영화 \"웰컴 투 동막골\""
      },
      {
        "rank": 10,
        "name": "블로그",
        "name_en": null,
        "description": "개인이 손쉽게 글과 사진을 올리고 소통할 수 있는 1인 미디어 '블로그'가 확산되며 디지털 라이프스타일의 상징으로 떠올랐다. (기타 화제: 블랙 컬러 휴대폰 등)",
        "link": "https://www.google.com/search?q=2005+삼성경제연구소+10대+히트상품+블로그"
      }
    ]
  },
  "2006": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2006년 10대 히트상품 (블로그 정리 이미지 자료 기반)",
    "source_url": "https://blog.naver.com/pooh1387/130154011523",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "판교아파트",
        "name_en": null,
        "description": "판교신도시 아파트 분양이 전국적인 관심을 모으며 청약 열풍을 일으켰다. (기타 화제: UCC, 친환경)",
        "link": "https://www.google.com/search?q=2006+삼성경제연구소+10대+히트상품+판교아파트"
      },
      {
        "rank": 2,
        "name": "슬림휴대폰",
        "name_en": null,
        "description": "얇고 슬림한 디자인을 강조한 휴대폰들이 새로운 트렌드로 떠올랐다. (기타 화제: UCC, 친환경)",
        "link": "https://www.google.com/search?q=2006+삼성경제연구소+10대+히트상품+슬림휴대폰"
      },
      {
        "rank": 3,
        "name": "저도수 소주",
        "name_en": null,
        "description": "알코올 도수를 낮춘 순한 소주 제품들이 잇따라 출시되며 시장을 재편했다. (기타 화제: UCC, 친환경)",
        "link": "https://www.google.com/search?q=2006+삼성경제연구소+10대+히트상품+저도수 소주"
      },
      {
        "rank": 4,
        "name": "왕의 남자, 괴물",
        "name_en": null,
        "description": "두 편의 한국영화가 잇따라 흥행 돌풍을 일으키며 한국영화 흥행 기록을 새로 썼다. (기타 화제: UCC, 친환경)",
        "link": "https://www.google.com/search?q=2006+삼성경제연구소+10대+히트상품+왕의 남자, 괴물"
      },
      {
        "rank": 5,
        "name": "고구려사극(주몽,연개소문,대조영)",
        "name_en": null,
        "description": "고구려를 배경으로 한 대작 사극 드라마들이 동시에 인기를 끌었다. (기타 화제: UCC, 친환경)",
        "link": "https://www.google.com/search?q=2006+삼성경제연구소+10대+히트상품+고구려사극(주몽,연개소문,대조영)"
      },
      {
        "rank": 6,
        "name": "웰빙차음료",
        "name_en": null,
        "description": "옥수수수염차 등 건강을 강조한 차 음료들이 새로운 음료 트렌드로 떠올랐다. (기타 화제: UCC, 친환경)",
        "link": "https://www.google.com/search?q=2006+삼성경제연구소+10대+히트상품+웰빙차음료"
      },
      {
        "rank": 7,
        "name": "이승엽",
        "name_en": null,
        "description": "야구선수 이승엽이 일본 진출 등에서 맹활약하며 국민적 인기를 얻었다. (기타 화제: UCC, 친환경)",
        "link": "https://www.google.com/search?q=2006+삼성경제연구소+10대+히트상품+이승엽"
      },
      {
        "rank": 8,
        "name": "비보이(B-Boy)",
        "name_en": null,
        "description": "브레이크댄스 그룹 비보이가 국제대회 우승 등으로 세계적인 인기를 끌었다. (기타 화제: UCC, 친환경)",
        "link": "https://www.google.com/search?q=2006+삼성경제연구소+10대+히트상품+비보이(B-Boy)"
      },
      {
        "rank": 9,
        "name": "스키니 패션",
        "name_en": null,
        "description": "몸에 딱 붙는 스키니진 등 타이트한 스타일의 패션이 크게 유행했다. (기타 화제: UCC, 친환경)",
        "link": "https://www.google.com/search?q=2006+삼성경제연구소+10대+히트상품+스키니 패션"
      },
      {
        "rank": 10,
        "name": "평판TV(LCD,PDP)",
        "name_en": null,
        "description": "얇고 벽걸이가 가능한 LCD·PDP 평판 TV가 브라운관 TV를 대체하며 대중화됐다. (기타 화제: UCC, 친환경)",
        "link": "https://www.google.com/search?q=2006+삼성경제연구소+10대+히트상품+평판TV(LCD,PDP)"
      }
    ]
  },
  "2007": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2007년 10대 히트상품 (블로그 정리 이미지 자료 기반)",
    "source_url": "https://blog.naver.com/pooh1387/130154011523",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "UCC",
        "name_en": null,
        "description": "사용자가 직접 제작한 동영상 콘텐츠(UCC)가 인터넷을 뜨겁게 달궜다.",
        "link": "https://www.google.com/search?q=2007+삼성경제연구소+10대+히트상품+UCC"
      },
      {
        "rank": 2,
        "name": "차이나펀드",
        "name_en": null,
        "description": "중국 증시에 투자하는 차이나펀드가 국내 투자자들 사이에서 큰 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2007+삼성경제연구소+10대+히트상품+차이나펀드"
      },
      {
        "rank": 3,
        "name": "국가대표(김연아,박태환)",
        "name_en": null,
        "description": "피겨스케이팅 김연아, 수영 박태환 등 젊은 스포츠 스타들이 국민적 사랑을 받았다.",
        "link": "https://www.google.com/search?q=2007+삼성경제연구소+10대+히트상품+국가대표(김연아,박태환)"
      },
      {
        "rank": 4,
        "name": "대조영",
        "name_en": null,
        "description": "고구려 유민의 발해 건국을 다룬 사극 드라마 '대조영'이 큰 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2007+삼성경제연구소+10대+히트상품+대조영"
      },
      {
        "rank": 5,
        "name": "CMA",
        "name_en": null,
        "description": "종합자산관리계좌(CMA)가 높은 금리를 앞세워 대중적인 금융상품으로 떠올랐다.",
        "link": "https://www.google.com/search?q=2007+삼성경제연구소+10대+히트상품+CMA"
      },
      {
        "rank": 6,
        "name": "무한도전",
        "name_en": null,
        "description": "MBC 예능 '무한도전'이 다양한 도전 콘텐츠로 폭넓은 사랑을 받았다.",
        "link": "https://www.google.com/search?q=2007+삼성경제연구소+10대+히트상품+무한도전"
      },
      {
        "rank": 7,
        "name": "옥수수 수염차",
        "name_en": null,
        "description": "건강 음료로 각광받은 옥수수수염차가 음료 시장에서 큰 히트를 기록했다.",
        "link": "https://www.google.com/search?q=2007+삼성경제연구소+10대+히트상품+옥수수 수염차"
      },
      {
        "rank": 8,
        "name": "원더걸스",
        "name_en": null,
        "description": "걸그룹 원더걸스가 데뷔하며 걸그룹 전성시대의 신호탄을 쏘아 올렸다.",
        "link": "https://www.google.com/search?q=2007+삼성경제연구소+10대+히트상품+원더걸스"
      },
      {
        "rank": 9,
        "name": "BB(Blemish Balm)크림",
        "name_en": null,
        "description": "잡티와 피부 결점을 가려주는 비비크림이 화장품 시장에서 크게 유행했다.",
        "link": "https://www.google.com/search?q=2007+삼성경제연구소+10대+히트상품+BB(Blemish Balm)크림"
      },
      {
        "rank": 10,
        "name": "와인",
        "name_en": null,
        "description": "와인 소비가 대중화되며 다양한 가격대의 와인이 널리 소비되기 시작했다.",
        "link": "https://www.google.com/search?q=2007+삼성경제연구소+10대+히트상품+와인"
      }
    ]
  },
  "2008": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2008년 10대 히트상품 (블로그 정리 이미지 자료 기반)",
    "source_url": "https://blog.naver.com/pooh1387/130154011523",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "터치 폰(햅틱)",
        "name_en": null,
        "description": "삼성 햅틱폰 등 터치스크린 방식의 휴대폰이 새로운 대세로 떠올랐다.",
        "link": "https://www.google.com/search?q=2008+삼성경제연구소+10대+히트상품+터치 폰(햅틱)"
      },
      {
        "rank": 2,
        "name": "베이징올림픽 스타",
        "name_en": null,
        "description": "2008 베이징 올림픽에서 활약한 국가대표 선수들이 큰 사랑을 받았다.",
        "link": "https://www.google.com/search?q=2008+삼성경제연구소+10대+히트상품+베이징올림픽 스타"
      },
      {
        "rank": 3,
        "name": "교통요금제(하이패스,교통카드)",
        "name_en": null,
        "description": "고속도로 하이패스와 대중교통 통합 요금 시스템이 널리 보급되었다.",
        "link": "https://www.google.com/search?q=2008+삼성경제연구소+10대+히트상품+교통요금제(하이패스,교통카드)"
      },
      {
        "rank": 4,
        "name": "인터넷 토론방",
        "name_en": null,
        "description": "온라인 토론방과 커뮤니티를 통한 여론 형성이 활발해졌다.",
        "link": "https://www.google.com/search?q=2008+삼성경제연구소+10대+히트상품+인터넷 토론방"
      },
      {
        "rank": 5,
        "name": "베토벤 바이러스",
        "name_en": null,
        "description": "괴팍한 지휘자와 오케스트라 단원들의 이야기를 그린 드라마가 큰 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2008+삼성경제연구소+10대+히트상품+베토벤 바이러스"
      },
      {
        "rank": 6,
        "name": "리얼 버라이어티(패밀리가 떴다/우리 결혼했어요)",
        "name_en": null,
        "description": "출연자들의 실제 상황을 담은 리얼리티 예능 프로그램들이 큰 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2008+삼성경제연구소+10대+히트상품+리얼 버라이어티(패밀리가 떴다/우리 결혼했어요)"
      },
      {
        "rank": 7,
        "name": "닌텐도 Wii",
        "name_en": null,
        "description": "몸을 움직여 즐기는 체감형 게임기 닌텐도 Wii가 가족 게임기로 큰 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2008+삼성경제연구소+10대+히트상품+닌텐도 Wii"
      },
      {
        "rank": 8,
        "name": "넷북",
        "name_en": null,
        "description": "저렴하고 가벼운 소형 노트북인 넷북이 새로운 PC 카테고리로 대중화됐다.",
        "link": "https://www.google.com/search?q=2008+삼성경제연구소+10대+히트상품+넷북"
      },
      {
        "rank": 9,
        "name": "기부(유명연예인 기부,기부사이트)",
        "name_en": null,
        "description": "유명 연예인들의 기부 활동과 온라인 기부 플랫폼이 기부 문화 확산을 이끌었다.",
        "link": "https://www.google.com/search?q=2008+삼성경제연구소+10대+히트상품+기부(유명연예인 기부,기부사이트)"
      },
      {
        "rank": 10,
        "name": "소비자고발 프로그램",
        "name_en": null,
        "description": "소비자 권익을 다루는 고발 프로그램들이 큰 화제와 사회적 반향을 일으켰다.",
        "link": "https://www.google.com/search?q=2008+삼성경제연구소+10대+히트상품+소비자고발 프로그램"
      }
    ]
  },
  "2009": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2009년 10대 히트상품 (블로그 정리 이미지 자료 기반)",
    "source_url": "https://blog.naver.com/pooh1387/130154011523",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "막걸리",
        "name_en": null,
        "description": "웰빙 붐과 함께 전통주 막걸리가 재조명받으며 폭발적인 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2009+삼성경제연구소+10대+히트상품+막걸리"
      },
      {
        "rank": 2,
        "name": "신종플루 대응상품",
        "name_en": null,
        "description": "신종플루(H1N1) 유행으로 손소독제·마스크 등 방역 관련 제품 수요가 급증했다.",
        "link": "https://www.google.com/search?q=2009+삼성경제연구소+10대+히트상품+신종플루 대응상품"
      },
      {
        "rank": 3,
        "name": "김연아",
        "name_en": null,
        "description": "피겨스케이팅 선수 김연아가 세계적 활약을 펼치며 국민적 인기를 얻었다.",
        "link": "https://www.google.com/search?q=2009+삼성경제연구소+10대+히트상품+김연아"
      },
      {
        "rank": 4,
        "name": "LED TV",
        "name_en": null,
        "description": "기존 LCD TV보다 얇고 화질이 개선된 LED 백라이트 TV가 새로운 대세로 떠올랐다.",
        "link": "https://www.google.com/search?q=2009+삼성경제연구소+10대+히트상품+LED TV"
      },
      {
        "rank": 5,
        "name": "스마트폰",
        "name_en": null,
        "description": "아이폰 국내 출시 등을 계기로 스마트폰이 본격적으로 대중화되기 시작했다.",
        "link": "https://www.google.com/search?q=2009+삼성경제연구소+10대+히트상품+스마트폰"
      },
      {
        "rank": 6,
        "name": "선덕여왕",
        "name_en": null,
        "description": "신라 최초 여왕의 일대기를 그린 MBC 드라마로 높은 화제성과 시청률을 기록했다.",
        "link": "https://www.google.com/search?q=2009+삼성경제연구소+10대+히트상품+선덕여왕"
      },
      {
        "rank": 7,
        "name": "Girl 그룹",
        "name_en": null,
        "description": "소녀시대 등 걸그룹들이 대거 등장하며 가요계의 새로운 트렌드를 이끌었다.",
        "link": "https://www.google.com/search?q=2009+삼성경제연구소+10대+히트상품+Girl 그룹"
      },
      {
        "rank": 8,
        "name": "도보체험관광",
        "name_en": null,
        "description": "제주올레길 등 걸으며 즐기는 여행 코스가 인기를 끌며 도보관광 붐이 일었다.",
        "link": "https://www.google.com/search?q=2009+삼성경제연구소+10대+히트상품+도보체험관광"
      },
      {
        "rank": 9,
        "name": "보금자리주택",
        "name_en": null,
        "description": "정부가 추진한 서민용 공공주택 공급 정책으로 청약 열기가 뜨거웠다.",
        "link": "https://www.google.com/search?q=2009+삼성경제연구소+10대+히트상품+보금자리주택"
      },
      {
        "rank": 10,
        "name": "KT 국(QOOK)",
        "name_en": null,
        "description": "KT가 유무선 통합 브랜드로 선보인 '쿡(QOOK)' 서비스가 널리 알려졌다.",
        "link": "https://www.google.com/search?q=2009+삼성경제연구소+10대+히트상품+KT 국(QOOK)"
      }
    ]
  },
  "2010": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2010년 10대 히트상품 (블로그 정리 이미지 자료 기반)",
    "source_url": "https://blog.naver.com/pooh1387/130154011523",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "스마트폰",
        "name_en": null,
        "description": "아이폰과 갤럭시S 등의 등장으로 스마트폰이 본격적인 대중화 원년을 맞았다.",
        "link": "https://www.google.com/search?q=2010+삼성경제연구소+10대+히트상품+스마트폰"
      },
      {
        "rank": 2,
        "name": "슈퍼스타K2",
        "name_en": null,
        "description": "Mnet의 오디션 프로그램 시즌2로, 허각 등 스타를 배출하며 큰 화제를 모았다.",
        "link": "https://www.google.com/search?q=2010+삼성경제연구소+10대+히트상품+슈퍼스타K2"
      },
      {
        "rank": 3,
        "name": "여자 국가대표 축구팀",
        "name_en": null,
        "description": "여자 축구 국가대표팀의 활약이 이 해 큰 화제와 관심을 받았다.",
        "link": "https://www.google.com/search?q=2010+삼성경제연구소+10대+히트상품+여자 국가대표 축구팀"
      },
      {
        "rank": 4,
        "name": "소셜미디어",
        "name_en": null,
        "description": "트위터·페이스북 등 SNS가 국내에서 본격적으로 확산되기 시작했다.",
        "link": "https://www.google.com/search?q=2010+삼성경제연구소+10대+히트상품+소셜미디어"
      },
      {
        "rank": 5,
        "name": "태블릿 PC",
        "name_en": null,
        "description": "아이패드 등 태블릿PC가 새로운 IT 기기 카테고리로 등장해 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2010+삼성경제연구소+10대+히트상품+태블릿 PC"
      },
      {
        "rank": 6,
        "name": "기아자동차 K시리즈",
        "name_en": null,
        "description": "기아차의 K5, K7 등 'K 시리즈' 세단이 디자인과 판매에서 큰 성공을 거뒀다.",
        "link": "https://www.google.com/search?q=2010+삼성경제연구소+10대+히트상품+기아자동차 K시리즈"
      },
      {
        "rank": 7,
        "name": "아바타",
        "name_en": null,
        "description": "제임스 카메론 감독의 영화 '아바타'가 3D 영화 붐을 일으켰다.",
        "link": "https://www.google.com/search?q=2010+삼성경제연구소+10대+히트상품+아바타"
      },
      {
        "rank": 8,
        "name": "블루베리",
        "name_en": null,
        "description": "항산화 효능이 알려지며 블루베리를 활용한 건강식품·음료가 유행했다.",
        "link": "https://www.google.com/search?q=2010+삼성경제연구소+10대+히트상품+블루베리"
      },
      {
        "rank": 9,
        "name": "발열의류",
        "name_en": null,
        "description": "유니클로 히트텍 등 기능성 발열 내의가 겨울철 필수템으로 자리잡았다.",
        "link": "https://www.google.com/search?q=2010+삼성경제연구소+10대+히트상품+발열의류"
      },
      {
        "rank": 10,
        "name": "제빵왕 김탁구",
        "name_en": null,
        "description": "KBS 드라마로 방영 내내 높은 시청률을 기록하며 큰 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2010+삼성경제연구소+10대+히트상품+제빵왕 김탁구"
      }
    ]
  },
  "2011": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2011년 10대 히트상품 (블로그 정리 이미지 자료 기반)",
    "source_url": "https://blog.naver.com/pooh1387/130154011523",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "꼬꼬면",
        "name_en": null,
        "description": "한국야쿠르트가 출시한 하얀 국물 라면으로, 라면업계에 새로운 트렌드를 만들었다.",
        "link": "https://www.google.com/search?q=2011+삼성경제연구소+10대+히트상품+꼬꼬면"
      },
      {
        "rank": 2,
        "name": "스티브 잡스",
        "name_en": null,
        "description": "애플 창업자 스티브 잡스의 별세와 함께 그의 혁신적 삶이 재조명받았다.",
        "link": "https://www.google.com/search?q=2011+삼성경제연구소+10대+히트상품+스티브 잡스"
      },
      {
        "rank": 3,
        "name": "카카오톡",
        "name_en": null,
        "description": "무료 모바일 메신저로 급속히 확산되며 '국민 메신저'로 자리잡았다.",
        "link": "https://www.google.com/search?q=2011+삼성경제연구소+10대+히트상품+카카오톡"
      },
      {
        "rank": 4,
        "name": "나는 가수다",
        "name_en": null,
        "description": "MBC의 서바이벌 음악 예능으로, 가수들의 재해석 무대가 큰 화제를 모았다.",
        "link": "https://www.google.com/search?q=2011+삼성경제연구소+10대+히트상품+나는 가수다"
      },
      {
        "rank": 5,
        "name": "갤럭시 S2",
        "name_en": null,
        "description": "삼성전자의 스마트폰으로 국내외에서 큰 판매 호조를 보였다.",
        "link": "https://www.google.com/search?q=2011+삼성경제연구소+10대+히트상품+갤럭시 S2"
      },
      {
        "rank": 6,
        "name": "K-Pop",
        "name_en": null,
        "description": "한류 열풍이 아시아를 넘어 전 세계로 확산되며 K-Pop이라는 용어가 자리잡았다.",
        "link": "https://www.google.com/search?q=2011+삼성경제연구소+10대+히트상품+K-Pop"
      },
      {
        "rank": 7,
        "name": "연금복권",
        "name_en": null,
        "description": "매월 일정 금액을 연금 형태로 지급하는 새로운 복권 상품이 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2011+삼성경제연구소+10대+히트상품+연금복권"
      },
      {
        "rank": 8,
        "name": "도가니",
        "name_en": null,
        "description": "사회적 약자에 대한 폭력을 다룬 영화로, 사회적 공분과 제도 개선 움직임을 이끌었다.",
        "link": "https://www.google.com/search?q=2011+삼성경제연구소+10대+히트상품+도가니"
      },
      {
        "rank": 9,
        "name": "평창 동계올림픽 유치",
        "name_en": null,
        "description": "2018년 동계올림픽 개최지로 평창이 확정되며 국민적 관심을 모았다.",
        "link": "https://www.google.com/search?q=2011+삼성경제연구소+10대+히트상품+평창 동계올림픽 유치"
      },
      {
        "rank": 10,
        "name": "통큰·반값 PB상품",
        "name_en": null,
        "description": "대형마트의 '통큰치킨' 등 초저가 자체브랜드(PB) 상품이 화제를 모았다.",
        "link": "https://www.google.com/search?q=2011+삼성경제연구소+10대+히트상품+통큰·반값 PB상품"
      }
    ]
  },
  "2012": {
    "type": "hit",
    "title": null,
    "source": "삼성경제연구소(SERI) 2012년 10대 히트상품 (블로그 정리 이미지 자료 기반)",
    "source_url": "https://blog.naver.com/pooh1387/130154011523",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "강남스타일(싸이)",
        "name_en": null,
        "description": "가수 싸이의 '강남스타일'이 유튜브를 통해 전 세계적인 신드롬을 일으켰다.",
        "link": "https://www.google.com/search?q=2012+삼성경제연구소+10대+히트상품+강남스타일(싸이)"
      },
      {
        "rank": 2,
        "name": "애니팡",
        "name_en": null,
        "description": "카카오톡 기반 모바일 퍼즐 게임으로 남녀노소 즐기는 '국민 게임'이 되었다.",
        "link": "https://www.google.com/search?q=2012+삼성경제연구소+10대+히트상품+애니팡"
      },
      {
        "rank": 3,
        "name": "갤럭시 2012 시리즈",
        "name_en": null,
        "description": "갤럭시 S3, 갤럭시 노트2 등 2012년 출시된 삼성 스마트폰들이 큰 인기를 끌었다.",
        "link": "https://www.google.com/search?q=2012+삼성경제연구소+10대+히트상품+갤럭시 2012 시리즈"
      },
      {
        "rank": 4,
        "name": "차량용 블랙박스",
        "name_en": null,
        "description": "사고 상황을 기록하는 차량용 영상기록장치가 필수품으로 빠르게 보급되었다.",
        "link": "https://www.google.com/search?q=2012+삼성경제연구소+10대+히트상품+차량용 블랙박스"
      },
      {
        "rank": 5,
        "name": "런던 올림픽 스타",
        "name_en": null,
        "description": "2012년 런던 올림픽에서 활약한 국가대표 선수들이 큰 사랑을 받았다.",
        "link": "https://www.google.com/search?q=2012+삼성경제연구소+10대+히트상품+런던 올림픽 스타"
      },
      {
        "rank": 6,
        "name": "에너지 음료",
        "name_en": null,
        "description": "카페인을 강화한 고카페인 에너지 음료가 새로운 음료 카테고리로 유행했다.",
        "link": "https://www.google.com/search?q=2012+삼성경제연구소+10대+히트상품+에너지 음료"
      },
      {
        "rank": 7,
        "name": "LTE 서비스",
        "name_en": null,
        "description": "4세대 이동통신 LTE 서비스가 본격 확산되며 빠른 데이터 속도를 앞세웠다.",
        "link": "https://www.google.com/search?q=2012+삼성경제연구소+10대+히트상품+LTE 서비스"
      },
      {
        "rank": 8,
        "name": "고급형 인스턴트 커피",
        "name_en": null,
        "description": "카누 등 프리미엄 원두커피 믹스 제품이 인스턴트 커피 시장을 재편했다.",
        "link": "https://www.google.com/search?q=2012+삼성경제연구소+10대+히트상품+고급형 인스턴트 커피"
      },
      {
        "rank": 9,
        "name": "관객 1억 시대의 한국영화",
        "name_en": null,
        "description": "한국 영화 연간 총 관객수가 사상 처음 1억 명을 돌파했다.",
        "link": "https://www.google.com/search?q=2012+삼성경제연구소+10대+히트상품+관객 1억 시대의 한국영화"
      },
      {
        "rank": 10,
        "name": "캠핑상품",
        "name_en": null,
        "description": "레저 문화 확산과 함께 텐트·캠핑용품 등 캠핑 관련 상품 수요가 급증했다.",
        "link": "https://www.google.com/search?q=2012+삼성경제연구소+10대+히트상품+캠핑상품"
      }
    ]
  },
  "2013": {
    "type": "trend",
    "title": "COBRA TWIST",
    "source": "『트렌드 코리아 2013』(김난도 외, 미래의 창) - 2013년 계사년(뱀의 해) 10대 소비트렌드 키워드",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2013+COBRA+TWIST",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "날 선 사람들의 도시",
        "name_en": "City of hysterie",
        "description": "불확실성과 경쟁이 심화되며 신경이 곤두선 채 살아가는 도시인들의 예민한 삶의 모습을 그린 키워드.",
        "link": null
      },
      {
        "rank": 2,
        "name": "난센스의 시대",
        "name_en": "OTL... Nonsense!",
        "description": "논리적으로 설명되지 않는 기발하고 엉뚱한 '병맛' 콘텐츠와 유머가 큰 인기를 끄는 현상.",
        "link": null
      },
      {
        "rank": 3,
        "name": "'스칸디맘'이 몰려온다",
        "name_en": "Bravo, Scandimom",
        "description": "북유럽(스칸디나비아) 스타일의 실용적이고 자연친화적인 육아·라이프스타일을 추구하는 엄마들의 트렌드.",
        "link": null
      },
      {
        "rank": 4,
        "name": "소유냐 향유냐",
        "name_en": "Redefined ownership",
        "description": "물건을 직접 소유하기보다 필요할 때 빌리고 나누어 쓰는 공유·향유 중심의 소비 방식이 확산되는 흐름.",
        "link": null
      },
      {
        "rank": 5,
        "name": "나홀로 라운징",
        "name_en": "Alone with lounging",
        "description": "1인 가구 증가와 함께, 혼자서도 고품격 휴식과 여가를 즐기려는 라운징 트렌드.",
        "link": null
      },
      {
        "rank": 6,
        "name": "미각의 제국",
        "name_en": "Taste your life out",
        "description": "팍팍한 현실 속에서 미식을 통해 삶의 풍요로움을 채우려는 사람들이 늘며 미식 문화가 확산되는 현상.",
        "link": null
      },
      {
        "rank": 7,
        "name": "시즌의 상실",
        "name_en": "Whenever U want",
        "description": "제철·시즌에 구애받지 않고 원하는 상품과 서비스를 사시사철 즐기고자 하는 소비 성향.",
        "link": null
      },
      {
        "rank": 8,
        "name": "디톡스가 필요한 시간",
        "name_en": "It's detox time",
        "description": "물질적·정신적 독소가 넘쳐나는 사회에서 몸과 마음을 정화하려는 디톡스 열풍.",
        "link": null
      },
      {
        "rank": 9,
        "name": "소진사회",
        "name_en": "Surviving burn-out society",
        "description": "경쟁과 과로에 지친 사람들이 스스로를 극한까지 소진시키게 되는 사회 현상에 대한 진단.",
        "link": null
      },
      {
        "rank": 10,
        "name": "적절한 불편",
        "name_en": "Trouble is welcomed",
        "description": "완벽하고 편리하기만 한 제품·서비스보다, 적당한 불편함이 오히려 매력으로 받아들여지는 소비 심리.",
        "link": null
      }
    ]
  },
  "2014": {
    "type": "trend",
    "title": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2014+키워드",
    "verified": false,
    "entries": [
      {
        "rank": 1,
        "name": "(입력 필요: 2014년 1번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 2,
        "name": "(입력 필요: 2014년 2번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 3,
        "name": "(입력 필요: 2014년 3번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 4,
        "name": "(입력 필요: 2014년 4번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 5,
        "name": "(입력 필요: 2014년 5번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 6,
        "name": "(입력 필요: 2014년 6번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 7,
        "name": "(입력 필요: 2014년 7번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 8,
        "name": "(입력 필요: 2014년 8번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 9,
        "name": "(입력 필요: 2014년 9번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 10,
        "name": "(입력 필요: 2014년 10번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      }
    ]
  },
  "2015": {
    "type": "trend",
    "title": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2015+키워드",
    "verified": false,
    "entries": [
      {
        "rank": 1,
        "name": "(입력 필요: 2015년 1번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 2,
        "name": "(입력 필요: 2015년 2번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 3,
        "name": "(입력 필요: 2015년 3번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 4,
        "name": "(입력 필요: 2015년 4번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 5,
        "name": "(입력 필요: 2015년 5번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 6,
        "name": "(입력 필요: 2015년 6번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 7,
        "name": "(입력 필요: 2015년 7번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 8,
        "name": "(입력 필요: 2015년 8번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 9,
        "name": "(입력 필요: 2015년 9번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 10,
        "name": "(입력 필요: 2015년 10번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      }
    ]
  },
  "2016": {
    "type": "trend",
    "title": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2016+키워드",
    "verified": false,
    "entries": [
      {
        "rank": 1,
        "name": "(입력 필요: 2016년 1번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 2,
        "name": "(입력 필요: 2016년 2번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 3,
        "name": "(입력 필요: 2016년 3번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 4,
        "name": "(입력 필요: 2016년 4번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 5,
        "name": "(입력 필요: 2016년 5번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 6,
        "name": "(입력 필요: 2016년 6번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 7,
        "name": "(입력 필요: 2016년 7번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 8,
        "name": "(입력 필요: 2016년 8번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 9,
        "name": "(입력 필요: 2016년 9번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 10,
        "name": "(입력 필요: 2016년 10번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      }
    ]
  },
  "2017": {
    "type": "trend",
    "title": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2017+키워드",
    "verified": false,
    "entries": [
      {
        "rank": 1,
        "name": "(입력 필요: 2017년 1번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 2,
        "name": "(입력 필요: 2017년 2번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 3,
        "name": "(입력 필요: 2017년 3번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 4,
        "name": "(입력 필요: 2017년 4번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 5,
        "name": "(입력 필요: 2017년 5번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 6,
        "name": "(입력 필요: 2017년 6번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 7,
        "name": "(입력 필요: 2017년 7번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 8,
        "name": "(입력 필요: 2017년 8번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 9,
        "name": "(입력 필요: 2017년 9번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 10,
        "name": "(입력 필요: 2017년 10번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      }
    ]
  },
  "2018": {
    "type": "trend",
    "title": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2018+키워드",
    "verified": false,
    "entries": [
      {
        "rank": 1,
        "name": "(입력 필요: 2018년 1번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 2,
        "name": "(입력 필요: 2018년 2번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 3,
        "name": "(입력 필요: 2018년 3번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 4,
        "name": "(입력 필요: 2018년 4번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 5,
        "name": "(입력 필요: 2018년 5번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 6,
        "name": "(입력 필요: 2018년 6번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 7,
        "name": "(입력 필요: 2018년 7번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 8,
        "name": "(입력 필요: 2018년 8번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 9,
        "name": "(입력 필요: 2018년 9번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 10,
        "name": "(입력 필요: 2018년 10번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      }
    ]
  },
  "2019": {
    "type": "trend",
    "title": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2019+키워드",
    "verified": false,
    "entries": [
      {
        "rank": 1,
        "name": "(입력 필요: 2019년 1번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 2,
        "name": "(입력 필요: 2019년 2번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 3,
        "name": "(입력 필요: 2019년 3번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 4,
        "name": "(입력 필요: 2019년 4번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 5,
        "name": "(입력 필요: 2019년 5번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 6,
        "name": "(입력 필요: 2019년 6번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 7,
        "name": "(입력 필요: 2019년 7번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 8,
        "name": "(입력 필요: 2019년 8번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 9,
        "name": "(입력 필요: 2019년 9번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 10,
        "name": "(입력 필요: 2019년 10번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      }
    ]
  },
  "2020": {
    "type": "trend",
    "title": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2020+키워드",
    "verified": false,
    "entries": [
      {
        "rank": 1,
        "name": "(입력 필요: 2020년 1번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 2,
        "name": "(입력 필요: 2020년 2번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 3,
        "name": "(입력 필요: 2020년 3번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 4,
        "name": "(입력 필요: 2020년 4번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 5,
        "name": "(입력 필요: 2020년 5번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 6,
        "name": "(입력 필요: 2020년 6번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 7,
        "name": "(입력 필요: 2020년 7번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 8,
        "name": "(입력 필요: 2020년 8번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 9,
        "name": "(입력 필요: 2020년 9번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 10,
        "name": "(입력 필요: 2020년 10번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      }
    ]
  },
  "2021": {
    "type": "trend",
    "title": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2021+키워드",
    "verified": false,
    "entries": [
      {
        "rank": 1,
        "name": "(입력 필요: 2021년 1번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 2,
        "name": "(입력 필요: 2021년 2번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 3,
        "name": "(입력 필요: 2021년 3번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 4,
        "name": "(입력 필요: 2021년 4번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 5,
        "name": "(입력 필요: 2021년 5번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 6,
        "name": "(입력 필요: 2021년 6번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 7,
        "name": "(입력 필요: 2021년 7번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 8,
        "name": "(입력 필요: 2021년 8번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 9,
        "name": "(입력 필요: 2021년 9번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 10,
        "name": "(입력 필요: 2021년 10번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      }
    ]
  },
  "2022": {
    "type": "trend",
    "title": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2022+키워드",
    "verified": false,
    "entries": [
      {
        "rank": 1,
        "name": "(입력 필요: 2022년 1번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 2,
        "name": "(입력 필요: 2022년 2번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 3,
        "name": "(입력 필요: 2022년 3번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 4,
        "name": "(입력 필요: 2022년 4번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 5,
        "name": "(입력 필요: 2022년 5번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 6,
        "name": "(입력 필요: 2022년 6번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 7,
        "name": "(입력 필요: 2022년 7번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 8,
        "name": "(입력 필요: 2022년 8번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 9,
        "name": "(입력 필요: 2022년 9번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 10,
        "name": "(입력 필요: 2022년 10번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      }
    ]
  },
  "2023": {
    "type": "trend",
    "title": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2023+키워드",
    "verified": false,
    "entries": [
      {
        "rank": 1,
        "name": "(입력 필요: 2023년 1번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 2,
        "name": "(입력 필요: 2023년 2번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 3,
        "name": "(입력 필요: 2023년 3번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 4,
        "name": "(입력 필요: 2023년 4번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 5,
        "name": "(입력 필요: 2023년 5번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 6,
        "name": "(입력 필요: 2023년 6번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 7,
        "name": "(입력 필요: 2023년 7번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 8,
        "name": "(입력 필요: 2023년 8번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 9,
        "name": "(입력 필요: 2023년 9번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      },
      {
        "rank": 10,
        "name": "(입력 필요: 2023년 10번째 키워드)",
        "name_en": null,
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요.",
        "link": null
      }
    ]
  },
  "2024": {
    "type": "trend",
    "title": "DRAGON EYES",
    "source": "『트렌드 코리아 2024』(김난도 외, 미래의 창) - 2024년 갑진년(청룡의 해) 10대 소비트렌드 키워드",
    "source_url": "https://www.korea.kr/news/policyNewsView.do?newsId=148925088",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "분초사회",
        "name_en": "Don't Waste a Single Second: Time-Efficient Society",
        "description": "시간을 돈만큼 중요한 자원으로 여기며, 짧은 시간에 최대한의 밀도로 즐기고 소비하려는 사회 현상.",
        "link": null
      },
      {
        "rank": 2,
        "name": "호모 프롬프트",
        "name_en": "Rise of 'Homo Promptus'",
        "description": "생성형 AI에게 좋은 질문(프롬프트)을 던져 원하는 결과를 이끌어내는 능력이 중요해진 인간상을 뜻함.",
        "link": null
      },
      {
        "rank": 3,
        "name": "육각형 인간",
        "name_en": "Aspiring to Be a Hexagonal Human",
        "description": "외모·학력·자산·직업 등 모든 면에서 흠이 없는 '완벽한 인간'을 지향하는 사회적 압박과 동경을 표현.",
        "link": null
      },
      {
        "rank": 4,
        "name": "버라이어티 가격 전략",
        "name_en": "Getting the Price Right: Variable Pricing",
        "description": "동일 상품이라도 시간, 조건, 구매 방식에 따라 가격을 다르게 매기는 차별화된 가격 전략의 확산.",
        "link": null
      },
      {
        "rank": 5,
        "name": "도파밍",
        "name_en": "On Dopamine Farming",
        "description": "짧고 자극적인 재미(도파민)를 추구하며 콘텐츠를 소비하는 '기승전-재미'식 소비 행태.",
        "link": null
      },
      {
        "rank": 6,
        "name": "요즘남편 없던아빠",
        "name_en": "Not Like Old Daddies, Millennial Hubbies",
        "description": "가사와 육아에 적극 참여하는 밀레니얼 세대 아빠들의 변화한 역할과 태도를 가리키는 키워드.",
        "link": null
      },
      {
        "rank": 7,
        "name": "스핀오프 프로젝트",
        "name_en": "Expanding Your Horizons: Spin-off Projects",
        "description": "기존의 인기 콘텐츠나 브랜드에서 파생된 새로운 프로젝트가 잇따라 등장하는 현상.",
        "link": null
      },
      {
        "rank": 8,
        "name": "디토소비",
        "name_en": "You Choose, I'll Follow: Ditto Consumption",
        "description": "전문가나 인플루언서의 추천을 그대로 따라 구매하는 '나도(ditto)' 소비 성향.",
        "link": null
      },
      {
        "rank": 9,
        "name": "리퀴드폴리탄",
        "name_en": "ElastiCity, Liquidpolitan",
        "description": "지역 소멸 위기 속에서, 특정 지역의 매력에 따라 사람들이 유동적으로 모여드는 새로운 도시 현상.",
        "link": null
      },
      {
        "rank": 10,
        "name": "돌봄경제",
        "name_en": "Supporting One Another: Care-based Economy",
        "description": "고령화·1인가구 증가 속에서 돌봄이 복지를 넘어 하나의 산업이자 경제 영역으로 성장하는 흐름.",
        "link": null
      }
    ]
  },
  "2025": {
    "type": "trend",
    "title": "SNAKE SENSE",
    "source": "『트렌드 코리아 2025』(김난도 외, 미래의 창) - 2025년 을사년(푸른 뱀의 해) 10대 소비트렌드 키워드",
    "source_url": "https://www.korea.kr/news/customizedNewsView.do?newsId=148938716",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "옴니보어",
        "name_en": "Omnivore",
        "description": "나이·소득·성별 등 고정관념의 경계를 넘어, 다양한 취향을 자유롭게 넘나드는 잡식성 소비자.",
        "link": null
      },
      {
        "rank": 2,
        "name": "#아보하",
        "name_en": "Nothing Out of the Ordinary: Very Ordinary Day",
        "description": "'아주 보통의 하루'의 줄임말로, 특별하지 않아도 평범한 일상 자체에 만족하는 삶의 태도.",
        "link": null
      },
      {
        "rank": 3,
        "name": "토핑경제",
        "name_en": "Topping Economy",
        "description": "기본 상품에 개인 취향에 맞는 요소를 선택적으로 추가하며 개성을 표현하는 소비 방식.",
        "link": null
      },
      {
        "rank": 4,
        "name": "페이스테크",
        "name_en": "Facetech",
        "description": "얼굴 인식·분석 등 안면 관련 기술이 결제, 헬스케어, 뷰티 등 다양한 산업에 접목되는 흐름.",
        "link": null
      },
      {
        "rank": 5,
        "name": "무해력",
        "name_en": "Harm-free Preference",
        "description": "타인이나 사회, 환경에 해를 끼치지 않는 것을 중요한 매력·가치로 여기는 소비 심리.",
        "link": null
      },
      {
        "rank": 6,
        "name": "그라데이션K",
        "name_en": "Gradation K",
        "description": "다문화 사회로 진입하며 '진정한 한국적인 것'에 대한 정의가 다양해지고 있음을 나타내는 키워드.",
        "link": null
      },
      {
        "rank": 7,
        "name": "물성매력",
        "name_en": "Physical Charm",
        "description": "디지털이 일상화될수록 오히려 만지고 느낄 수 있는 실물·아날로그적 매력이 재조명되는 현상.",
        "link": null
      },
      {
        "rank": 8,
        "name": "기후감수성",
        "name_en": "Climate Sensitivity",
        "description": "이상기후를 직접 체감하며 소비와 생활 전반에서 기후 변화에 민감하게 반응하는 태도.",
        "link": null
      },
      {
        "rank": 9,
        "name": "공진화 전략",
        "name_en": "Co-evolution Strategy",
        "description": "경쟁보다 협력을 통해 서로 함께 성장해나가는 파트너십 중심의 기업 전략.",
        "link": null
      },
      {
        "rank": 10,
        "name": "원포인트업",
        "name_en": "One-point Up",
        "description": "전면적인 변화 대신, 삶의 한 부분만 콕 집어 개선함으로써 작은 성공을 쌓아가려는 태도.",
        "link": null
      }
    ]
  },
  "2026": {
    "type": "trend",
    "title": "HORSE POWER",
    "source": "『트렌드 코리아 2026』(김난도 외, 미래의 창) - 2026년 병오년(붉은 말의 해) 10대 소비트렌드 키워드",
    "source_url": "https://www.ntoday.co.kr/news/articleView.html?idxno=119826",
    "verified": true,
    "entries": [
      {
        "rank": 1,
        "name": "휴먼인더루프",
        "name_en": "Human-in-the-loop",
        "description": "AI의 의사결정 과정에 인간의 판단을 반드시 포함시켜, 최종 결정은 사람이 내리는 인간-AI 협업 모델.",
        "link": null
      },
      {
        "rank": 2,
        "name": "필코노미",
        "name_en": "Oh, my feelings! (Feelconomy)",
        "description": "구매의 핵심 동인이 '기분'이 되어, 감정을 진단·관리·전환하기 위해 제품과 서비스를 소비하는 현상.",
        "link": null
      },
      {
        "rank": 3,
        "name": "제로클릭",
        "name_en": "Zero Click",
        "description": "AI 추천과 자동화로 인해 검색·클릭 과정 자체가 사라지고, 알고리즘이 소비자의 선택을 대신하는 흐름.",
        "link": null
      },
      {
        "rank": 4,
        "name": "레디코어",
        "name_en": "Ready-core",
        "description": "불확실한 시대에 스스로 정보를 갖추고 미리 대비하는 자기주도적 준비 역량을 중시하는 태도.",
        "link": null
      },
      {
        "rank": 5,
        "name": "AX조직",
        "name_en": "AX Organization",
        "description": "AI 전환(AI Transformation)에 맞춰 조직 구조와 업무 방식 자체를 재설계하는 기업들의 흐름.",
        "link": null
      },
      {
        "rank": 6,
        "name": "픽셀라이프",
        "name_en": "Pixel Life",
        "description": "디지털 화면 속 데이터와 이미지로 구성되는 삶의 영역이 확장되는 현상.",
        "link": null
      },
      {
        "rank": 7,
        "name": "프라이스 디코딩",
        "name_en": "Price Decoding",
        "description": "가격 구조와 원가를 스스로 파악하고 합리적으로 따지는, 더 똑똑해진 소비자들의 가격 해독 행태.",
        "link": null
      },
      {
        "rank": 8,
        "name": "건강지능 HQ",
        "name_en": "Health Quotient",
        "description": "단순한 건강 정보 습득을 넘어, 자신에게 맞는 건강 관리를 설계·실행하는 능력이 중시되는 흐름.",
        "link": null
      },
      {
        "rank": 9,
        "name": "1.5가구",
        "name_en": "1.5-person Household",
        "description": "1인 가구와 다인 가구의 경계에 있는, 반려동물·반려식물 등과 함께하는 새로운 가구 형태.",
        "link": null
      },
      {
        "rank": 10,
        "name": "근본이즘",
        "name_en": "Returning to the Fundamentals",
        "description": "AI가 모든 것을 생성·복제하는 시대에, 변치 않는 원조와 클래식의 가치를 다시 찾는 경향.",
        "link": null
      }
    ]
  }
}"""

DATA = json.loads(DATA_JSON)

st.set_page_config(
    page_title="대한민국 연도별 소비 타임라인",
    page_icon="\U0001F4C5",
    layout="centered",
)

years = sorted(DATA.keys(), key=lambda y: int(y), reverse=True)

TYPE_LABEL = {
    "hit": "\U0001F3C6 10대 히트상품 (삼성경제연구소)",
    "trend": "\U0001F4C8 소비 트렌드 (트렌드 코리아)",
}

st.sidebar.title("\U0001F4C5 연도별 소비 타임라인")
st.sidebar.caption("2000~2012 히트상품(SERI) · 2013~2026 소비트렌드(트렌드코리아)")

selected_year = st.sidebar.selectbox("연도를 선택하세요", years, index=0)
keyword_search = st.sidebar.text_input("\U0001F50D 키워드 검색 (전체 연도)")

st.sidebar.divider()
st.sidebar.markdown(
    "**데이터가 비어 있나요?**\n\n"
    "이 파일 안의 `DATA_JSON` 부분에서 해당 연도를 찾아 "
    "`name`, `description` 값을 직접 채워 넣으면 됩니다."
)


def render_entry(entry, show_link=True):
    with st.container(border=True):
        label = f"{entry['rank']}. {entry['name']}"
        if entry.get("name_en"):
            label += f" ({entry['name_en']})"
        st.markdown(f"### {label}")
        st.write(entry["description"])
        if show_link and entry.get("link"):
            st.link_button("관련 자료/기사 보러가기 \U0001F517", entry["link"])


if keyword_search.strip():
    st.title(f"\U0001F50D '{keyword_search}' 검색 결과")
    found_any = False
    for year in years:
        year_data = DATA[year]
        matches = [
            e for e in year_data["entries"]
            if keyword_search.lower() in e["name"].lower()
            or keyword_search.lower() in (e.get("name_en") or "").lower()
            or keyword_search.lower() in e["description"].lower()
        ]
        if matches:
            found_any = True
            st.subheader(f"{year}년 · {TYPE_LABEL[year_data['type']]}")
            for e in matches:
                render_entry(e)
    if not found_any:
        st.info("검색 결과가 없습니다. 다른 키워드를 입력해보세요.")
else:
    year_data = DATA[selected_year]
    st.title(f"{selected_year}년")
    st.caption(TYPE_LABEL[year_data["type"]])

    if not year_data.get("verified", False):
        st.warning(
            f"\u26A0\uFE0F {selected_year}년 데이터는 아직 검증되지 않은 입력 틀입니다. "
            "실제 원문 자료를 확인해 채워 넣어주세요."
        )

    if year_data.get("title"):
        st.subheader(f"핵심 키워드: {year_data['title']}")

    st.caption(f"출처: {year_data['source']}")
    st.link_button("출처 확인하기 \U0001F517", year_data["source_url"])
    st.divider()

    for e in sorted(year_data["entries"], key=lambda x: x["rank"]):
        render_entry(e)

st.divider()
st.caption(
    "2000~2012년은 삼성경제연구소(SERI) '10대 히트상품', 2013~2026년은 서울대 "
    "소비트렌드분석센터 <트렌드 코리아> 시리즈를 기반으로 정리했습니다. 이미지는 "
    "저작권 문제로 표시하지 않았으며, 정확한 원문은 각 출처를 확인하세요."
)
