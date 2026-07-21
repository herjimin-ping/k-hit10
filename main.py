"""
연도별 소비 트렌드 키워드 뷰어 (2013~2026) - 단일 파일 버전
--------------------------------------------------------------
서울대 소비트렌드분석센터가 매년 발간하는 <트렌드 코리아> 시리즈의
연도별 10대 소비트렌드 키워드를 살펴보는 Streamlit 앱입니다.

<트렌드 코리아> 시리즈는 2007년(『트렌드 코리아 2009』가 첫 출간)부터
매년 12월 그 다음해 전망을 담아 출간되고 있습니다. 이 앱은 삼성경제연구소의
'10대 히트상품'(2000~2012) 조사가 끝난 2013년 이후를 이어서 다룹니다.

실행 방법 (로컬):
    pip install streamlit
    streamlit run trend-korea.py
"""

import json
import streamlit as st

st.title("요즘 뭐하텐?")

DATA_JSON = r"""{
  "2013": {
    "acronym": "COBRA TWIST",
    "source": "『트렌드 코리아 2013』(김난도 외, 미래의 창) - 2013년 계사년(뱀의 해) 10대 소비트렌드 키워드",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2013+COBRA+TWIST",
    "verified": true,
    "keywords": [
      {
        "rank": 1,
        "keyword": "City of hysterie",
        "keyword_kr": "날 선 사람들의 도시",
        "description": "불확실성과 경쟁이 심화되며 신경이 곤두선 채 살아가는 도시인들의 예민한 삶의 모습을 그린 키워드."
      },
      {
        "rank": 2,
        "keyword": "OTL... Nonsense!",
        "keyword_kr": "난센스의 시대",
        "description": "논리적으로 설명되지 않는 기발하고 엉뚱한 '병맛' 콘텐츠와 유머가 큰 인기를 끄는 현상."
      },
      {
        "rank": 3,
        "keyword": "Bravo, Scandimom",
        "keyword_kr": "'스칸디맘'이 몰려온다",
        "description": "북유럽(스칸디나비아) 스타일의 실용적이고 자연친화적인 육아·라이프스타일을 추구하는 엄마들의 트렌드."
      },
      {
        "rank": 4,
        "keyword": "Redefined ownership",
        "keyword_kr": "소유냐 향유냐",
        "description": "물건을 직접 소유하기보다 필요할 때 빌리고 나누어 쓰는 공유·향유 중심의 소비 방식이 확산되는 흐름."
      },
      {
        "rank": 5,
        "keyword": "Alone with lounging",
        "keyword_kr": "나홀로 라운징",
        "description": "1인 가구 증가와 함께, 혼자서도 고품격 휴식과 여가를 즐기려는 라운징 트렌드."
      },
      {
        "rank": 6,
        "keyword": "Taste your life out",
        "keyword_kr": "미각의 제국",
        "description": "팍팍한 현실 속에서 미식을 통해 삶의 풍요로움을 채우려는 사람들이 늘며 미식 문화가 확산되는 현상."
      },
      {
        "rank": 7,
        "keyword": "Whenever U want",
        "keyword_kr": "시즌의 상실",
        "description": "제철·시즌에 구애받지 않고 원하는 상품과 서비스를 사시사철 즐기고자 하는 소비 성향."
      },
      {
        "rank": 8,
        "keyword": "It's detox time",
        "keyword_kr": "디톡스가 필요한 시간",
        "description": "물질적·정신적 독소가 넘쳐나는 사회에서 몸과 마음을 정화하려는 디톡스 열풍."
      },
      {
        "rank": 9,
        "keyword": "Surviving burn-out society",
        "keyword_kr": "소진사회",
        "description": "경쟁과 과로에 지친 사람들이 스스로를 극한까지 소진시키게 되는 사회 현상에 대한 진단."
      },
      {
        "rank": 10,
        "keyword": "Trouble is welcomed",
        "keyword_kr": "적절한 불편",
        "description": "완벽하고 편리하기만 한 제품·서비스보다, 적당한 불편함이 오히려 매력으로 받아들여지는 소비 심리."
      }
    ]
  },
  "2014": {
    "acronym": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2014+키워드",
    "verified": false,
    "keywords": [
      {
        "rank": 1,
        "keyword": "(입력 필요: 2014년 1번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 2,
        "keyword": "(입력 필요: 2014년 2번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 3,
        "keyword": "(입력 필요: 2014년 3번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 4,
        "keyword": "(입력 필요: 2014년 4번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 5,
        "keyword": "(입력 필요: 2014년 5번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 6,
        "keyword": "(입력 필요: 2014년 6번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 7,
        "keyword": "(입력 필요: 2014년 7번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 8,
        "keyword": "(입력 필요: 2014년 8번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 9,
        "keyword": "(입력 필요: 2014년 9번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 10,
        "keyword": "(입력 필요: 2014년 10번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      }
    ]
  },
  "2015": {
    "acronym": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2015+키워드",
    "verified": false,
    "keywords": [
      {
        "rank": 1,
        "keyword": "(입력 필요: 2015년 1번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 2,
        "keyword": "(입력 필요: 2015년 2번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 3,
        "keyword": "(입력 필요: 2015년 3번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 4,
        "keyword": "(입력 필요: 2015년 4번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 5,
        "keyword": "(입력 필요: 2015년 5번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 6,
        "keyword": "(입력 필요: 2015년 6번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 7,
        "keyword": "(입력 필요: 2015년 7번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 8,
        "keyword": "(입력 필요: 2015년 8번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 9,
        "keyword": "(입력 필요: 2015년 9번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 10,
        "keyword": "(입력 필요: 2015년 10번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      }
    ]
  },
  "2016": {
    "acronym": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2016+키워드",
    "verified": false,
    "keywords": [
      {
        "rank": 1,
        "keyword": "(입력 필요: 2016년 1번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 2,
        "keyword": "(입력 필요: 2016년 2번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 3,
        "keyword": "(입력 필요: 2016년 3번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 4,
        "keyword": "(입력 필요: 2016년 4번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 5,
        "keyword": "(입력 필요: 2016년 5번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 6,
        "keyword": "(입력 필요: 2016년 6번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 7,
        "keyword": "(입력 필요: 2016년 7번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 8,
        "keyword": "(입력 필요: 2016년 8번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 9,
        "keyword": "(입력 필요: 2016년 9번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 10,
        "keyword": "(입력 필요: 2016년 10번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      }
    ]
  },
  "2017": {
    "acronym": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2017+키워드",
    "verified": false,
    "keywords": [
      {
        "rank": 1,
        "keyword": "(입력 필요: 2017년 1번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 2,
        "keyword": "(입력 필요: 2017년 2번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 3,
        "keyword": "(입력 필요: 2017년 3번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 4,
        "keyword": "(입력 필요: 2017년 4번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 5,
        "keyword": "(입력 필요: 2017년 5번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 6,
        "keyword": "(입력 필요: 2017년 6번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 7,
        "keyword": "(입력 필요: 2017년 7번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 8,
        "keyword": "(입력 필요: 2017년 8번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 9,
        "keyword": "(입력 필요: 2017년 9번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 10,
        "keyword": "(입력 필요: 2017년 10번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      }
    ]
  },
  "2018": {
    "acronym": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2018+키워드",
    "verified": false,
    "keywords": [
      {
        "rank": 1,
        "keyword": "(입력 필요: 2018년 1번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 2,
        "keyword": "(입력 필요: 2018년 2번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 3,
        "keyword": "(입력 필요: 2018년 3번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 4,
        "keyword": "(입력 필요: 2018년 4번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 5,
        "keyword": "(입력 필요: 2018년 5번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 6,
        "keyword": "(입력 필요: 2018년 6번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 7,
        "keyword": "(입력 필요: 2018년 7번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 8,
        "keyword": "(입력 필요: 2018년 8번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 9,
        "keyword": "(입력 필요: 2018년 9번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 10,
        "keyword": "(입력 필요: 2018년 10번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      }
    ]
  },
  "2019": {
    "acronym": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2019+키워드",
    "verified": false,
    "keywords": [
      {
        "rank": 1,
        "keyword": "(입력 필요: 2019년 1번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 2,
        "keyword": "(입력 필요: 2019년 2번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 3,
        "keyword": "(입력 필요: 2019년 3번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 4,
        "keyword": "(입력 필요: 2019년 4번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 5,
        "keyword": "(입력 필요: 2019년 5번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 6,
        "keyword": "(입력 필요: 2019년 6번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 7,
        "keyword": "(입력 필요: 2019년 7번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 8,
        "keyword": "(입력 필요: 2019년 8번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 9,
        "keyword": "(입력 필요: 2019년 9번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 10,
        "keyword": "(입력 필요: 2019년 10번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      }
    ]
  },
  "2020": {
    "acronym": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2020+키워드",
    "verified": false,
    "keywords": [
      {
        "rank": 1,
        "keyword": "(입력 필요: 2020년 1번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 2,
        "keyword": "(입력 필요: 2020년 2번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 3,
        "keyword": "(입력 필요: 2020년 3번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 4,
        "keyword": "(입력 필요: 2020년 4번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 5,
        "keyword": "(입력 필요: 2020년 5번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 6,
        "keyword": "(입력 필요: 2020년 6번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 7,
        "keyword": "(입력 필요: 2020년 7번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 8,
        "keyword": "(입력 필요: 2020년 8번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 9,
        "keyword": "(입력 필요: 2020년 9번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 10,
        "keyword": "(입력 필요: 2020년 10번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      }
    ]
  },
  "2021": {
    "acronym": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2021+키워드",
    "verified": false,
    "keywords": [
      {
        "rank": 1,
        "keyword": "(입력 필요: 2021년 1번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 2,
        "keyword": "(입력 필요: 2021년 2번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 3,
        "keyword": "(입력 필요: 2021년 3번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 4,
        "keyword": "(입력 필요: 2021년 4번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 5,
        "keyword": "(입력 필요: 2021년 5번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 6,
        "keyword": "(입력 필요: 2021년 6번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 7,
        "keyword": "(입력 필요: 2021년 7번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 8,
        "keyword": "(입력 필요: 2021년 8번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 9,
        "keyword": "(입력 필요: 2021년 9번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 10,
        "keyword": "(입력 필요: 2021년 10번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      }
    ]
  },
  "2022": {
    "acronym": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2022+키워드",
    "verified": false,
    "keywords": [
      {
        "rank": 1,
        "keyword": "(입력 필요: 2022년 1번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 2,
        "keyword": "(입력 필요: 2022년 2번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 3,
        "keyword": "(입력 필요: 2022년 3번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 4,
        "keyword": "(입력 필요: 2022년 4번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 5,
        "keyword": "(입력 필요: 2022년 5번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 6,
        "keyword": "(입력 필요: 2022년 6번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 7,
        "keyword": "(입력 필요: 2022년 7번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 8,
        "keyword": "(입력 필요: 2022년 8번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 9,
        "keyword": "(입력 필요: 2022년 9번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 10,
        "keyword": "(입력 필요: 2022년 10번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      }
    ]
  },
  "2023": {
    "acronym": "(확인 필요)",
    "source": "미확인 (데이터 입력 필요)",
    "source_url": "https://www.google.com/search?q=트렌드코리아+2023+키워드",
    "verified": false,
    "keywords": [
      {
        "rank": 1,
        "keyword": "(입력 필요: 2023년 1번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 2,
        "keyword": "(입력 필요: 2023년 2번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 3,
        "keyword": "(입력 필요: 2023년 3번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 4,
        "keyword": "(입력 필요: 2023년 4번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 5,
        "keyword": "(입력 필요: 2023년 5번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 6,
        "keyword": "(입력 필요: 2023년 6번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 7,
        "keyword": "(입력 필요: 2023년 7번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 8,
        "keyword": "(입력 필요: 2023년 8번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 9,
        "keyword": "(입력 필요: 2023년 9번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      },
      {
        "rank": 10,
        "keyword": "(입력 필요: 2023년 10번째 키워드)",
        "keyword_kr": "",
        "description": "아직 데이터가 입력되지 않았습니다. 『트렌드 코리아』 해당 연도 편을 확인해 채워주세요."
      }
    ]
  },
  "2024": {
    "acronym": "DRAGON EYES",
    "source": "『트렌드 코리아 2024』(김난도 외, 미래의 창) - 2024년 갑진년(청룡의 해) 10대 소비트렌드 키워드",
    "source_url": "https://www.korea.kr/news/policyNewsView.do?newsId=148925088",
    "verified": true,
    "keywords": [
      {
        "rank": 1,
        "keyword": "Don't Waste a Single Second: Time-Efficient Society",
        "keyword_kr": "분초사회",
        "description": "시간을 돈만큼 중요한 자원으로 여기며, 짧은 시간에 최대한의 밀도로 즐기고 소비하려는 사회 현상."
      },
      {
        "rank": 2,
        "keyword": "Rise of 'Homo Promptus'",
        "keyword_kr": "호모 프롬프트",
        "description": "생성형 AI에게 좋은 질문(프롬프트)을 던져 원하는 결과를 이끌어내는 능력이 중요해진 인간상을 뜻함."
      },
      {
        "rank": 3,
        "keyword": "Aspiring to Be a Hexagonal Human",
        "keyword_kr": "육각형 인간",
        "description": "외모·학력·자산·직업 등 모든 면에서 흠이 없는 '완벽한 인간'을 지향하는 사회적 압박과 동경을 표현."
      },
      {
        "rank": 4,
        "keyword": "Getting the Price Right: Variable Pricing",
        "keyword_kr": "버라이어티 가격 전략",
        "description": "동일 상품이라도 시간, 조건, 구매 방식에 따라 가격을 다르게 매기는 차별화된 가격 전략의 확산."
      },
      {
        "rank": 5,
        "keyword": "On Dopamine Farming",
        "keyword_kr": "도파밍",
        "description": "짧고 자극적인 재미(도파민)를 추구하며 콘텐츠를 소비하는 '기승전-재미'식 소비 행태."
      },
      {
        "rank": 6,
        "keyword": "Not Like Old Daddies, Millennial Hubbies",
        "keyword_kr": "요즘남편 없던아빠",
        "description": "가사와 육아에 적극 참여하는 밀레니얼 세대 아빠들의 변화한 역할과 태도를 가리키는 키워드."
      },
      {
        "rank": 7,
        "keyword": "Expanding Your Horizons: Spin-off Projects",
        "keyword_kr": "스핀오프 프로젝트",
        "description": "기존의 인기 콘텐츠나 브랜드에서 파생된 새로운 프로젝트가 잇따라 등장하는 현상."
      },
      {
        "rank": 8,
        "keyword": "You Choose, I'll Follow: Ditto Consumption",
        "keyword_kr": "디토소비",
        "description": "전문가나 인플루언서의 추천을 그대로 따라 구매하는 '나도(ditto)' 소비 성향."
      },
      {
        "rank": 9,
        "keyword": "ElastiCity, Liquidpolitan",
        "keyword_kr": "리퀴드폴리탄",
        "description": "지역 소멸 위기 속에서, 특정 지역의 매력에 따라 사람들이 유동적으로 모여드는 새로운 도시 현상."
      },
      {
        "rank": 10,
        "keyword": "Supporting One Another: Care-based Economy",
        "keyword_kr": "돌봄경제",
        "description": "고령화·1인가구 증가 속에서 돌봄이 복지를 넘어 하나의 산업이자 경제 영역으로 성장하는 흐름."
      }
    ]
  },
  "2025": {
    "acronym": "SNAKE SENSE",
    "source": "『트렌드 코리아 2025』(김난도 외, 미래의 창) - 2025년 을사년(푸른 뱀의 해) 10대 소비트렌드 키워드",
    "source_url": "https://www.korea.kr/news/customizedNewsView.do?newsId=148938716",
    "verified": true,
    "keywords": [
      {
        "rank": 1,
        "keyword": "Omnivore",
        "keyword_kr": "옴니보어",
        "description": "나이·소득·성별 등 고정관념의 경계를 넘어, 다양한 취향을 자유롭게 넘나드는 잡식성 소비자."
      },
      {
        "rank": 2,
        "keyword": "Nothing Out of the Ordinary: Very Ordinary Day",
        "keyword_kr": "#아보하",
        "description": "'아주 보통의 하루'의 줄임말로, 특별하지 않아도 평범한 일상 자체에 만족하는 삶의 태도."
      },
      {
        "rank": 3,
        "keyword": "Topping Economy",
        "keyword_kr": "토핑경제",
        "description": "기본 상품에 개인 취향에 맞는 요소를 선택적으로 추가하며 개성을 표현하는 소비 방식."
      },
      {
        "rank": 4,
        "keyword": "Facetech",
        "keyword_kr": "페이스테크",
        "description": "얼굴 인식·분석 등 안면 관련 기술이 결제, 헬스케어, 뷰티 등 다양한 산업에 접목되는 흐름."
      },
      {
        "rank": 5,
        "keyword": "Harm-free Preference",
        "keyword_kr": "무해력",
        "description": "타인이나 사회, 환경에 해를 끼치지 않는 것을 중요한 매력·가치로 여기는 소비 심리."
      },
      {
        "rank": 6,
        "keyword": "Gradation K",
        "keyword_kr": "그라데이션K",
        "description": "다문화 사회로 진입하며 '진정한 한국적인 것'에 대한 정의가 다양해지고 있음을 나타내는 키워드."
      },
      {
        "rank": 7,
        "keyword": "Physical Charm",
        "keyword_kr": "물성매력",
        "description": "디지털이 일상화될수록 오히려 만지고 느낄 수 있는 실물·아날로그적 매력이 재조명되는 현상."
      },
      {
        "rank": 8,
        "keyword": "Climate Sensitivity",
        "keyword_kr": "기후감수성",
        "description": "이상기후를 직접 체감하며 소비와 생활 전반에서 기후 변화에 민감하게 반응하는 태도."
      },
      {
        "rank": 9,
        "keyword": "Co-evolution Strategy",
        "keyword_kr": "공진화 전략",
        "description": "경쟁보다 협력을 통해 서로 함께 성장해나가는 파트너십 중심의 기업 전략."
      },
      {
        "rank": 10,
        "keyword": "One-point Up",
        "keyword_kr": "원포인트업",
        "description": "전면적인 변화 대신, 삶의 한 부분만 콕 집어 개선함으로써 작은 성공을 쌓아가려는 태도."
      }
    ]
  },
  "2026": {
    "acronym": "HORSE POWER",
    "source": "『트렌드 코리아 2026』(김난도 외, 미래의 창) - 2026년 병오년(붉은 말의 해) 10대 소비트렌드 키워드",
    "source_url": "https://www.ntoday.co.kr/news/articleView.html?idxno=119826",
    "verified": true,
    "keywords": [
      {
        "rank": 1,
        "keyword": "Human-in-the-loop",
        "keyword_kr": "휴먼인더루프",
        "description": "AI의 의사결정 과정에 인간의 판단을 반드시 포함시켜, 최종 결정은 사람이 내리는 인간-AI 협업 모델."
      },
      {
        "rank": 2,
        "keyword": "Oh, my feelings! (Feelconomy)",
        "keyword_kr": "필코노미",
        "description": "구매의 핵심 동인이 '기분'이 되어, 감정을 진단·관리·전환하기 위해 제품과 서비스를 소비하는 현상."
      },
      {
        "rank": 3,
        "keyword": "Zero Click",
        "keyword_kr": "제로클릭",
        "description": "AI 추천과 자동화로 인해 검색·클릭 과정 자체가 사라지고, 알고리즘이 소비자의 선택을 대신하는 흐름."
      },
      {
        "rank": 4,
        "keyword": "Ready-core",
        "keyword_kr": "레디코어",
        "description": "불확실한 시대에 스스로 정보를 갖추고 미리 대비하는 자기주도적 준비 역량을 중시하는 태도."
      },
      {
        "rank": 5,
        "keyword": "AX Organization",
        "keyword_kr": "AX조직",
        "description": "AI 전환(AI Transformation)에 맞춰 조직 구조와 업무 방식 자체를 재설계하는 기업들의 흐름."
      },
      {
        "rank": 6,
        "keyword": "Pixel Life",
        "keyword_kr": "픽셀라이프",
        "description": "디지털 화면 속 데이터와 이미지로 구성되는 삶의 영역이 확장되는 현상."
      },
      {
        "rank": 7,
        "keyword": "Price Decoding",
        "keyword_kr": "프라이스 디코딩",
        "description": "가격 구조와 원가를 스스로 파악하고 합리적으로 따지는, 더 똑똑해진 소비자들의 가격 해독 행태."
      },
      {
        "rank": 8,
        "keyword": "Health Quotient",
        "keyword_kr": "건강지능 HQ",
        "description": "단순한 건강 정보 습득을 넘어, 자신에게 맞는 건강 관리를 설계·실행하는 능력이 중시되는 흐름."
      },
      {
        "rank": 9,
        "keyword": "1.5-person Household",
        "keyword_kr": "1.5가구",
        "description": "1인 가구와 다인 가구의 경계에 있는, 반려동물·반려식물 등과 함께하는 새로운 가구 형태."
      },
      {
        "rank": 10,
        "keyword": "Returning to the Fundamentals",
        "keyword_kr": "근본이즘",
        "description": "AI가 모든 것을 생성·복제하는 시대에, 변치 않는 원조와 클래식의 가치를 다시 찾는 경향."
      }
    ]
  }
}"""

DATA = json.loads(DATA_JSON)

st.set_page_config(
    page_title="연도별 소비 트렌드 (트렌드 코리아)",
    page_icon="\U0001F4C8",
    layout="centered",
)

years = sorted(DATA.keys(), key=lambda y: int(y), reverse=True)

st.sidebar.title("\U0001F4C8 소비 트렌드")
st.sidebar.caption("서울대 소비트렌드분석센터 <트렌드 코리아> 시리즈 · 2013~2026년")

selected_year = st.sidebar.selectbox("연도를 선택하세요", years, index=0)
keyword_search = st.sidebar.text_input("\U0001F50D 키워드 검색 (전체 연도)")

st.sidebar.divider()
st.sidebar.markdown(
    "**데이터가 비어 있나요?**\n\n"
    "이 파일 안의 `DATA_JSON` 부분에서 해당 연도를 찾아 "
    "`keyword`, `keyword_kr`, `description` 값을 직접 채워 넣으면 됩니다."
)

if keyword_search.strip():
    st.title(f"\U0001F50D '{keyword_search}' 검색 결과")
    found_any = False
    for year in years:
        year_data = DATA[year]
        matches = [
            kw for kw in year_data["keywords"]
            if keyword_search.lower() in kw["keyword"].lower()
            or keyword_search.lower() in kw.get("keyword_kr", "").lower()
            or keyword_search.lower() in kw["description"].lower()
        ]
        if matches:
            found_any = True
            st.subheader(f"{year}년 ({year_data.get('acronym', '')})")
            for kw in matches:
                with st.container(border=True):
                    label = kw["keyword"]
                    if kw.get("keyword_kr"):
                        label += f" · {kw['keyword_kr']}"
                    st.markdown(f"**{kw['rank']}. {label}**")
                    st.write(kw["description"])
    if not found_any:
        st.info("검색 결과가 없습니다. 다른 키워드를 입력해보세요.")
else:
    year_data = DATA[selected_year]
    st.title(f"{selected_year}년 소비 트렌드")

    if not year_data.get("verified", False):
        st.warning(
            f"\u26A0\uFE0F {selected_year}년 데이터는 아직 검증되지 않은 입력 틀입니다. "
            "실제 『트렌드 코리아』 원서를 확인해 채워 넣어주세요."
        )

    if year_data.get("acronym") and year_data["acronym"] != "(확인 필요)":
        st.subheader(f"핵심 키워드: {year_data['acronym']}")

    st.caption(f"출처: {year_data['source']}")
    st.link_button("출처 확인하기 \U0001F517", year_data["source_url"])
    st.divider()

    for kw in sorted(year_data["keywords"], key=lambda x: x["rank"]):
        with st.container(border=True):
            label = kw["keyword"]
            if kw.get("keyword_kr"):
                label += f" · {kw['keyword_kr']}"
            st.markdown(f"### {kw['rank']}. {label}")
            st.write(kw["description"])

st.divider()
st.caption(
    "<트렌드 코리아>는 서울대 소비트렌드분석센터(김난도 교수 외)가 매년 발간하는 "
    "소비 트렌드 전망서입니다. 이 앱의 내용은 요약·정리한 것으로, 정확한 원문은 "
    "해당 연도의 『트렌드 코리아』 책을 참고하세요."
)
